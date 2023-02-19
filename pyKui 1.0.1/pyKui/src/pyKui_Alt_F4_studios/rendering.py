from pyKui_Alt_F4_studios.variables import *
from pyKui_Alt_F4_studios.imports import *
from pyKui_Alt_F4_studios.errors import *

class get:
    def windowW(windowSurface = pygame.Surface):
        ### Gets the window width

        return windowSurface.get_size()[0]

    def windowH(windowSurface = pygame.Surface):
        ### Gets the window height

        return windowSurface.get_size()[1]

class imageLoad:
    def loadNoAlpha(imagePath = ""):
      ### Loads an image without converting in to alpha

      try:
        return pygame.image.load(imagePath)

      except Exception as E:
        warn(E)
      
    def load(imagePath = ""):
        ### Loads an image

        try:
            return pygame.image.load(imagePath).convert_alpha()

        except Exception as E:
            warn(E)

    def loadNoBackgound(imagePath = ""):
        ### Loads an image without backround
        
        try:
            return pygame.image.load(imagePath).convert()

        except Exception as E:
            warn(E)

def setIcon(iconPath):
    ### Sets the program icon

    pygame.display.set_icon(iconPath)

class create:
    def title(display = pygame.Surface, title = f"PyKui {version_} window"):
        ### Creates a title for the window that you created

        if (title == ""):
            title = f"PyKuy {version_} window"

        display.set_caption(title)

    def WINDOW(title = f"PyKuy {version_} window", x = 500, y = 500, flags = RESIZABLE):
        ### Create a window

        global screen, windowsCreated, windowX, windowY

        windowsCreated += 1

        if (allowMoreWindows or windowsCreated == 1):
            if (allowMoreWindows):
                windowsCreated = 1
                
            if (title == ""):
                title = f"PyKuy {version_} window"

            windowX = x
            windowY = y
            
            if (minWindowSizeAllowed):
                if (windowX < 100 and windowX != 0):
                    raise pyKuiWindowSizeError(f"WindowX size is {windowX} px, it must be bigger than 99px")

                if (windowY < 100 and windowY != 0):
                    raise pyKuiWindowSizeError(f"WindowY size is {windowY} px, it must be bigger than 99px")

                if (windowX < 0):
                    raise pyKuiWindowSizeError(f"WindowX size has negative values")

                if (windowY < 0):
                    raise pyKuiWindowSizeError(f"WindowY size has negative values")

            if (autoResizeWhen00):
                if (windowX == 0 and windowY == 0):
                    screen = pygame.display.set_mode((0, 0))

                    windowX = screen.get_size()[0]
                    windowY = screen.get_size()[1]

            pygame.display.set_caption(title)

        else:
            raise pyKuiWindowsLimitError("There is more than 1 window")

        if (windowsCreated > 1):
            warn("More than one window created, canceled")

        return pygame.display.set_mode((windowX, windowY), flags)
      
def blit(windowSurface = pygame.Surface, surface = pygame.Surface, x = 0, y = 0):
    ### Shows (blits) image (surface) in windowSurface in given x and y coordinates

    if (x > 0 - surface.get_size()[0] and x <= 0 + windowX and y > 0 - surface.get_size()[1] and y <= 0 + windowY):
        windowSurface.blit(surface, (x, y))

def smoothScaledBlit(windowSurface = pygame.Surface, surface = pygame.Surface, x = 0, y = 0, w = 0, h = 0):
    ### Shows (blits) image (surface) in windowSurface in given x and y coordinates and smooth resizes the image in the given w and h

    surface = pygame.transform.smoothscale(surface, size=(w, h))

    if (w < 0):
        w = 0

    if (h < 0):
        h = 0

    if (x > 0 - surface.get_size()[0] and x <= 0 + windowX and y > 0 - surface.get_size()[1] and y <= 0 + windowY):
        windowSurface.blit(surface, (x, y))
        
def scaledBlit(windowSurface = pygame.Surface, surface = pygame.Surface, x = 0, y = 0, w = 0, h = 0):
    ### Shows (blits) image (surface) in windowSurface in given x and y coordinates and resizes the image in the given w and h

    surface = pygame.transform.scale(surface, size=(w, h))
    
    if (w < 0):
        w = 0

    if (h < 0):
        h = 0

    if (x > 0 - surface.get_size()[0] and x <= 0 + windowX and y > 0 - surface.get_size()[1] and y <= 0 + windowY):
        windowSurface.blit(surface, (x, y))

def smoothScale(surface = pygame.Surface, w = 0, h = 0):
    ### Smooths scales a surface

    if (w < 0):
        w = 0

    if (h < 0):
        h = 0

    surface = pygame.transform.smoothscale(surface, size=(w, h)).convert_alpha()

def scale(surface = pygame.Surface, w = 0, h = 0):
    ### Scales a surface

    if (w < 0):
        w = 0

    if (h < 0):
        h = 0

    surface = pygame.transform.scale(surface, size=(w, h)).convert_alpha()

def flipImage(sprite = pygame.Surface, x = True, y = False):
    ### Flip a image 

    try:
        return pygame.transform.flip(sprite, x, y).convert_alpha()

    except:
        warn("var 'sprite' value is None")

class frameRate:
    def limit(FPS):
        ### Sets frame rate

        global defaultFPS, frameRateSet

        if (FPS > 900 and fpsLimit == True):
            raise pyKuiFpsLimitError("E: Its imposible to reach a limit of 900 FPS! To disable this error, edit it in rule.set()")

        frameRateSet = True

        defaultFPS = FPS

    def tick():
        ### Sets frame rate to defaultFPS

        clockTick.tick(defaultFPS)

class draw:
    def rect(windowSurface = pygame.Surface, r = 0, g = 0, b = 0, x = 0, y = 0, w = 0, h = 0, borderRad = 0):
        ### The surface spot is in wich you will have to enter the 'window' variable of your game
        ## x -> position x
        ## y -> position y
        ## w -> width of the rect
        ## h -> height of the rect

        pygame.draw.rect(windowSurface, (r,g,b), pygame.Rect(x, y, w, h), border_radius=borderRad)

    def circle(windowSurface = pygame.Surface, r = 0, g = 0, b = 0, x = 0, y = 0, w = 0, h = 0):
        ### The surface spot is in wich you will have to enter the 'window' variable of your game
        ## x -> position x
        ## y -> position y
        ## w -> width of the circle
        ## h -> height of the rect

        pygame.draw.circle(windowSurface, (r,g,b), (x, y), w, h)

    def line(windowSurface = pygame.Surface, r = 0, g = 0, b = 0, width = 1, startX = 0, startY = 0, endX = windowX, endY = windowY):
        ### Create a line to x and y to endX and endY
        
        pygame.draw.line(windowSurface, color=(r, g, b), start_pos=(startX, startY), end_pos=(endX, endY), width=width)

class sdrawer:
    #### Simple Drawer

    def init():
        ### Init the sdrawer to use it

        global initedSDrawer
        
        if (initedSDrawer == False):
            initedSDrawer = True

        else:
            warn("initedSDrawer is already to bool(True)")

    def uninit():
        ### UnInit sdrawer to not use it
        
        global initedSDrawer

        if (initedSDrawer == True):
            initedSDrawer = False

        else:
            warn("initedSDrawer is already to bool(True)")

    def showPointer(windowSurface = pygame.Surface, show = True):
        ### Show pointer of the penX and penY

        if (initedSDrawer and show == True):
            draw.rect(windowSurface, 255, 0, 0, penX, penY, 10, 10, 10)

        elif (initedSDrawer == False):
            raise pyKuiNoDrawerInitError(noDrawerInitErrorMessage)

    def goto(x, y):  
        ### PenX and penY goes to x and y values

        global penX, penY

        if (initedSDrawer):
            penX = x
            penY = y

        else:
            raise pyKuiNoDrawerInitError(noDrawerInitErrorMessage)

    def glide(windowSurface = pygame.Surface, r = 0, g = 0, b = 0, width = 1, endX = windowX, endY = windowY):
        ### The line slides to the endX and endY values

        global penX, penY

        if (initedSDrawer):
            draw.line(windowSurface, r, g, b, width, penX, penY, endX, endY)

            penX = endX
            penY = endY

        else:
            raise pyKuiNoDrawerInitError(noDrawerInitErrorMessage)

    def square(windowSurface = pygame.Surface, r = 0, g = 0, b = 0, size = 10, borderRad = 0):
        ### Makes a square

        if (initedSDrawer):
            draw.rect(windowSurface, r, g, b, penX, penY, size, size, borderRad)

        else:
            raise pyKuiNoDrawerInitError(noDrawerInitErrorMessage)

    def rectangle(windowSurface = pygame.Surface, r = 0, g = 0, b = 0, w = 10, h = 10, borderRad = 0):
        ### Creates a rectangle

        if (initedSDrawer):
            draw.rect(windowSurface, r, g, b, penX, penY, w, h, borderRad)

        else:
            raise pyKuiNoDrawerInitError(noDrawerInitErrorMessage)

class drawer:
    def init():
        ### Init the drawer to use it

        global initedDrawer, initedSDrawer
        
        if (initedDrawer == False):
            initedDrawer = True
            initedSDrawer = True

        else:
            warn("initedDrawer is already to bool(True)")

    def uninit():
        ### UnInit drawer to not use it
        
        global initedDrawer, initedSDrawer

        if (initedDrawer == True):
            initedDrawer = False
            initedSDrawer = False

        else:
            warn("initedDrawer is already to bool(True)")

    def showPointer(windowSurface = pygame.Surface, show = True):
        ### Show pointer of the penX and penY

        if (initedDrawer and show == True):
            if (isPenUp == False):
                draw.rect(windowSurface, 255, 0, 0, penX, penY, 10, 10, 10)

        elif (initedDrawer == False):
            raise pyKuiNoDrawerInitError(noCDrawerInitErrorMessage)

    def glide(windowSurface = pygame.Surface, r = 0, g = 0, b = 0, width = 1, endX = windowX, endY = windowY):
        ### The line slides to the endX and endY values

        global penX, penY

        if (initedDrawer):
            if (isPenUp == False):
                draw.line(windowSurface, r, g, b, width, penX, penY, endX, endY)

            penX = endX
            penY = endY

        else:
            raise pyKuiNoDrawerInitError(noCDrawerInitErrorMessage)

    def penUp():
        ### Doesen't draw

        global isPenUp

        isPenUp = True
    
    def penDown():
        ### Draws

        global isPenUp
        
        isPenUp = False

    def goto(windowSurface = pygame.Surface, x = 0, y = 0, r = 255, g = 255, b = 255):  
        ### PenX and penY goes to x and y values

        global penX, penY

        if (initedDrawer):
            if (isPenUp == False):
                sdrawer.glide(windowSurface, r, g, b, 1, x, y)

            penX = x
            penY = y
        
        else:
            raise pyKuiNoDrawerInitError(noCDrawerInitErrorMessage)

    def square(windowSurface = pygame.Surface, r = 0, g = 0, b = 0, size = 10, borderRad = 0):
        ### Makes a square

        if (initedDrawer):
            if (isPenUp == False):
                draw.rect(windowSurface, r, g, b, penX, penY, size, size, borderRad)

        else:
            raise pyKuiNoDrawerInitError(noCDrawerInitErrorMessage)

    def rectangle(windowSurface = pygame.Surface, r = 0, g = 0, b = 0, w = 10, h = 10, borderRad = 0):
        ### Creates a rectangle

        if (initedDrawer):
            if (isPenUp == False):
                draw.rect(windowSurface, r, g, b, penX, penY, w, h, borderRad)

        else:
            raise pyKuiNoDrawerInitError(noCDrawerInitErrorMessage)
            
class cursor:
    def goto(x = 0, y = 0):
        ### Cursor goes to the given X and Y value

        pygame.mouse.set_pos([x, y])

    def getx():
        ### Gets the current mouse X

        global mx

        mx = pygame.mouse.get_pos()[0]

    def gety():
        ### Gets the current mouse Y
        
        global my
        
        my = pygame.mouse.get_pos()[1]

    def getxy():
        ### Gets the current mouse X and Y

        global mx, my

        mx = pygame.mouse.get_pos()[0]
        my = pygame.mouse.get_pos()[1]

    def showCursor(show = True):
        ### shows Cursor if variable show is True, else, it doesen't show

        if (show):
            pygame.mouse.set_visible(True)

        elif show == False:
            pygame.mouse.set_visible(False)

        else:
            pygame.mouse.set_visible(True)

            warn("var 'show' is not a bool")

    def setCursor(windowSurface = pygame.Surface, cursorImage = pygame.Surface, size = 25):
        ### Change the cursor image

        cursor.showCursor(False)
        cursor.getxy()

        if (cursorImage == "rect"):
            draw.rect(windowSurface, 255, 0, 0, mx, my, size, size)

        else:
            blit(windowSurface, cursorImage, mx, my, size, size)

