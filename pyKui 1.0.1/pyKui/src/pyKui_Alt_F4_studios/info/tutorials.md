# PyKui tutorials
## 1.0
### ©2023 All rights reserved

---

**Arguments in functions and explanations**

    create:
        WINDOW() # Create a window
            1: Window title, 2: width of window, 3: height of window
    
        title() # Create a title for a window
            1: Title
    
    open:
        openSysFont() # Open a system font
            1: Font name, 2: Size

        openFont()
            1: Font path, 2: Size
    
    saveText() # Saves text in to a variable with custom font
        1: font name, 2: text, 3: Pixelated, 4: r color value, 5: g color value, 6:  b color value

    saveSysText() # Saves text in to a variable with a system font
        1: font name, 2: text, 3: Pixelated, 4: r color value, 5: g color value, 6:  b color value

    printw() # Prints text to the screen without doing it manualy
        1: Window to display it, 2: font name, 3: text, 4: Pixelated, 5: r color value, 6: g color value, 7:  b color value

    rule:
        removeList() # Removes the last item in the rule history commands

        get() # Get all the history of rule

        set() # Sets a rule
            1: Arg 1, 2: Arg 2

    blit() # Shows an image in the given window and x and y 
    coordinates

        1: window, 2: image, 3: x, 4: y
    
    smoothScale() || scale() # Shows an image (smoother when resized) in the given window, x and y

        1: Image, 2: w, 3: h

    flipImage() # Flips an image

        1: Image, 2: flip bool(x), 3: flip bool(y)

    frameRate:
        limit() # Sets the maximim frame rate

            1: FPS

        tick() # Ticks at the maximum FPS that you set

    coordinates and w and h

        1: window, 2: image, 3: x, 4: y, 5: w, 6: h

    scaledBlit() # Shows an image (you can resize it) in the given window, x and y
    coordinates and w and h

        1: window, 2: image, 3: x, 4: y, 5: w, 6: h

    smoothScale() # smooth scales the image with the given w and h

    imageLoad:
        loadNoAlpha() # Load image without .convert_alpha()
            1: window path

        load() # Load image
            1: window path

        loadNoBackgound() # Load image without background
            1: window path

    setIcon() # Set icon for window
        1: icon path
    
    draw:
        rect() # Does a rect

            1: Window, 2: r color, 3: g color, 4: b color, 5: x, 6: y, 7: w, 8: h, 9: border radius

        circle() # Does a circle

            1: Window, 2: r color, 3: g color, 4: b color, 5: x, 6: y, 7: w, 8: h

        line() # Makes a line
            1: Window, 2: r color, 3: g color, 4: b color, 5: width, 6: Start X, 7: Start Y, 8: End X, 9: End Y

        sdrawer:
            init() # Start the sdrawer
            uninit() # End the sdrawer

            showPointer() # Show pointer

                1: Window, 2: show

            goto() # Go to the given x and y coordinates
                1: x, 2: y
            
            glide() # Glide to the given x and y coordinates

                1: Window, 2: r color, 3: g color, 4: b color, 5: width, 6: End X, 7: End Y

            square() # Makes a square

                1: Window, 2: r color, 3: g color, 4: b color, 5: Size, 6: border radius

            rectangle() # Makes a rectangle

                1: Window, 2: r color, 3: g color, 4: b color, 5: w, 6: h, 7: border radius

        drawer:
            init() # Start the sdrawer
            uninit() # End the sdrawer

            showPointer() # Show pointer

                1: Window, 2: show

            goto() # Go to the given x and y coordinates, but it draws to the start X and Y to the end X and Y
                1: x, 2: y
            
            glide() # Glide to the given x and y coordinates

                1: Window, 2: r color, 3: g color, 4: b color, 5: width, 6: End X, 7: End Y

            square() # Makes a square

                1: Window, 2: r color, 3: g color, 4: b color, 5: Size, 6: border radius

            rectangle() # Makes a rectangle

                1: Window, 2: r color, 3: g color, 4: b color, 5: w, 6: h, 7: border radius

        cursor:
            goto() # Cursor goes to given x and y coordinates

                1: x, 2: y
            
            getx() # Gets the cursor x
            
            gety() # Gets the cursor y
            
            getxy() # Gets the cursor x and y
            
            showCursor() # Shows cursor

                1: bool(show)

            setCursor() # Changes the cursor image

                1: Window, 2: cursorImage, 3: size
            
            get:
                windowW() # Gets the window W

                    1: Window

                windowH() # Gets the window H

                    1: Window

            end() # Ends the program

                1: End type

            update() # Updates the display

            simpleUpdate() # Does a simple update without doing it manualy

                1: bool(fill), 2: Window, r color, 3: g color, 4: b color
