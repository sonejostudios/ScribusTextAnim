#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

try:
    import scribus
except ImportError,err:
    print "This Python script is written for the Scribus scripting interface."
    print "It can only be run from within Scribus."
    sys.exit(1)



#############################################################




def main(argv):

    # check if "textanim" object exists, if not check selection
    global text_selection

    if scribus.objectExists("textanim"):
        text_selection = "textanim"

    else:
        # get selected object
        text_selection = scribus.getSelectedObject(0)

        # cancel if no object is selected or if it is not a text frame
        if text_selection == "":
            scribus.messageBox("Text frame needed", "Please select a text frame first.\nIf a text frame named 'textanim' exists, it will automatically be used.")
            sys.exit()
        else:
            selection_type = scribus.getObjectType(text_selection)
            if selection_type != "TextFrame":
                scribus.messageBox("Text frame needed", "This is not a text frame, please select a text frame first.")
                sys.exit()



    global export_dir
    export_dir = scribus.fileDialog("Select export directory", "", haspreview=False, issave=False, isdir=True)
    if export_dir == "":
        sys.exit()


    # ask to proceed
    ready = scribus.valueDialog("Scribus TextAnim", "This will export one image for each character.\n"
                                                    "This will produce a lot of files and therefore take a lot of time!\n\n"
                                                    "Do you want to proceed?", "yes")
    # exit if cancelled or not yes
    if ready != "yes":
        sys.exit()


    # set linespacing mode to "Fixed Linespacing"
    scribus.setLineSpacingMode(0, text_selection)


    # get text properties
    mytext = scribus.getText(text_selection)
    mytext_color = scribus.getTextColor(text_selection)
    mytext_font = scribus.getFont(text_selection)
    mytext_font_size = scribus.getFontSize(text_selection)
    mytext_linespacing = scribus.getLineSpacing(text_selection)



    # encode text to unicode
    mytext = unicode(mytext)

    # get text length
    text_length = len(mytext)

    # create copy of text
    newtext = mytext


    # status bar
    scribus.messagebarText("Exporting frames...")
    # set progressbar total
    scribus.progressTotal(text_length)


    for frame in range(text_length):
        scribus.progressSet(frame)

        # reverse frame count for filename
        frame_number = text_length - frame

        # export frame
        export_image(frame_number)

        # delete the whole text
        scribus.deleteText(text_selection)

        # remove last letter
        newtext = newtext[:-1]

        # re-insert new text
        renew_text(newtext, mytext_color, mytext_font, mytext_font_size, mytext_linespacing)


    # re-insert the whole text
    renew_text(mytext, mytext_color, mytext_font, mytext_font_size, mytext_linespacing)
    #scribus.messageBox("okay", mytext[:-1])




def renew_text(newtext, mytext_color, mytext_font, mytext_font_size, mytext_linespacing):
    scribus.setText(newtext, text_selection)
    scribus.setTextColor(mytext_color, text_selection)
    scribus.setFont(mytext_font, text_selection)
    scribus.setFontSize(mytext_font_size, text_selection)
    scribus.setLineSpacing(mytext_linespacing, text_selection)



def export_image(number):
    i = scribus.ImageExport()
    i.type = 'PNG'
    i.scale = 100
    i.quality = 100
    i.dpi = 72
    i.transparentBkgnd = True

    if len(str(number)) == 1:
        filename = "000" + str(number)
    if len(str(number)) == 2:
        filename = "00" + str(number)
    if len(str(number)) == 3:
        filename = "0" + str(number)
    if len(str(number)) == 4:
        filename = str(number)

    i.name = export_dir + "/" + filename + ".png"
    i.save()
        



        
        


#############################################################


def main_wrapper(argv):
    try:
        scribus.statusMessage("Running script...")
        scribus.progressReset()
        main(argv)
    finally:
        # Exit neatly even if the script terminated with an exception,
        # so we leave the progress bar and status bar blank and make sure
        # drawing is enabled.
        if scribus.haveDoc():
            scribus.setRedraw(True)
        scribus.statusMessage("")
        scribus.progressReset()


# This code detects if the script is being run as a script, or imported as a module.
# It only runs main() if being run as a script. This permits you to import your script
# and control it manually for debugging.
if __name__ == '__main__':
    main_wrapper(sys.argv)


