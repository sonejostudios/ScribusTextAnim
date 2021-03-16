# ScribusTextAnim
Use Scribus to generate text animation.

This script generates a "typewriter" animation, by adding one character to each animation frame.

![screenshot](https://raw.githubusercontent.com/sonejostudios/ScribusTextAnim/master/samples.gif "Scribus TextAnim")

## Best usage
1. Open Scribus, create a new document, set the units to Points (pt) and the dimensions to your video resolution, e.g. 1920x1080 (FullHD).
2. Add a text frame with your text.
3. Make sure the text is aligned left, set of "Fixed Linespacing", and has only one color.
4. Add a BLANK LINE at the beginning of the text (this is really important, because otherwise scribus will set the text to the highest character and this will cause weird movements).
5. Select the text frame and start the script from the "Scripter" menu. Alternatively, you can name the text frame "textanim", this will be automatically used (no need to select anything).
6. Choose a destination folder for your images.
7. If everything is fine, confirm the action by clicking "Okay" (leave "yes" in the field). This will take a long time and produce a lot of files, because one image will be exported for each character. So be patient and have a look to the progress bar ;)
8. Once done, you'll find the whole image sequence in the previously selected folder. Import all these images to a video editing app (e.g. Kdenlive) and enjoy!

## Preview
Have a look at the "samples.mp4" file.

## Examples
Open example.sla or example2.sla with Scribus and run TextAnim.
