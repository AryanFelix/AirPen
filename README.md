# AirPen
 A virtual drawing app that lets you use your household object as a stylus. The code works purely on the OpenCV and NumPy libraries.

 ## Libraries Used
 1. OpenCV

 2. NumPy

 ## Running AirPen
 1. The program already has the stylus color codes for 5 different colors. Namely Bright Orange, Bright Blue, Bright Yellow, Bright Blue and Bright Pink. If you want to add custom stylus color codes, see 'Adding Custom Stylus'.

 2. When done, install the required python libraries using pip.

 3. Run AirPen.py

 ## Adding a Custom Stylus
 * Before I tell you this, lets make sure that you understand what you're going to do properly in order to avoid any sort of mistakes.

 * A custom stylus is any household object that has a very distinct colour. Like a pen with a colorful cap. For my experimentation, I used highlighters with rather bright and colorful caps.

 * Once you have located your stylus, run the second python file called MaskValues.py

 * When you run it, your camera will start up and you will see three things on your screen. One, the image shown by your camera. Two, a white screen below it. Three, a window with trackbars which measure Hue, Saturation and Values.

 * Now hold your stylus in front of your camera (6-8 inches from it). Now alter all the values of the trackbar till only your stylus is white and everything else is black in the second window.

 * Now remember, this is important. Only the bright and colorful region of your stylus should be white and not the entire thing. For example, if you're using a pen with a bright blue cap lets say. Then the second window which was earlier completely white should now only show the cap (in white) and the body should not be visible.

 * Adjusting the trackbar might seem a little tricky but eventually, you'll get the hang of it.

 * Once you have obtained the perfect image, it should look something like this.
 
    ![Mask](https://github.com/AryanFelix/AirPen/blob/master/test/capture.JPG)
 
 * Note down the values from the trackbar in the form of a list like so.

    [Hue Main, Hue Max, Sat Min, Sat Max, Val Min, Val Max]

 * Add this list into the variable 'colors' in the AirPen.py file. It will be under the comment marked 'Stylus Color Codes'

 * Your custom stylus is now ready.

 * You still have to add the BGR value that will be printed when the program detects this particular stylus.

 * Choose your desired color and make a list of the values like so

    [B, G, R]

 * Add this list into the variable 'colorValues' in the AirPen.py file. It will be under the comment marked 'Colors for Drawing'.

 * Now your stylus is all set.

 * ### Enjoy Painting!

 # License
 * ## MIT License

