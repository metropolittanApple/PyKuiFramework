# PyKui - Created by Pau Cava and Paul Cannon
# A simple framework to easily
# create UI elements and displays
# (C) 2023

print("Loading...")

class pyKuiWindowSizeError(Exception):
    pass

class pyKuiMinWindowSizeError(Exception):
    pass

class pyKuiInstallError(Exception):
    pass

class pyKuiRequirementError(Exception):
    pass

class pyKuiWindowsLimit(Exception):
    pass

import sys
import os
import platform

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

try:
    import pygame
    from pygame.locals import *

except Exception as E:
    print(E)

    try:
        os.system("pip3 install pygame --upgrade")

    except:
        try:
            os.system("pip install pygame --upgrade")

        except:
            raise pyKuiInstallError("Couln't install pygame")

try:
    from colorama import Fore

except Exception as E:
    try:
        os.system("pip3 install colorama --upgrade")

    except:
        try:
            os.system("pip install colorama --upgrade")

        except:
            raise pyKuiInstallError("Couln't install colorama")

print("Checking python version")

if (int(platform.python_version_tuple()[0]) < 3):
    raise pyKuiRequirementError("Must be at python version 3.0.0 or higher")

print("Accept")

key = pygame.key.get_pressed

version_ = ["demo", 1]

printwText = "None"
rulesArg1 = []
rulesArg2 = []
windowX = 0
windowY = 0
defaultFPS = 0.1
windowsCreated = 0
i = 0

getEvent = pygame.event.get
event = pygame.event
update = pygame.display.update
display = pygame.display
image = pygame.image
time = pygame.time
mouse = pygame.mouse
Cursor = pygame.Cursor
joystick = pygame.joystick
bufferproxy = pygame.bufferproxy
color = pygame.color
Color = pygame.Color
encode_file_path = pygame.encode_file_path
encode_string = pygame.encode_string
version = pygame.version
Vector3 = pygame.Vector3
Vector2 = pygame.Vector2
surfarray = pygame.surfarray
surface = pygame.surface
sndarray = pygame.sndarray
sprite = pygame.sprite
register_quit = pygame.register_quit
scrap = pygame.scrap
set_error = pygame.set_error
Rect = pygame.Rect
rect = pygame.rect
pixelcopy = pygame.pixelcopy
pixelarray = pygame.pixelarray
pixelArray = pygame.PixelArray

encode_str = encode_string

minWindowSizeAllowed = True
autoResizeWhen00 = True
allowMoreWindows = False

inWindow = True

clockTick = time.Clock()

print(f"{Fore.YELLOW}WELCOME TO")
print(f"{Fore.WHITE}PyKui {version_}")
print(f"{Fore.YELLOW}Web: https://metropolittanapple.github.io/PyKuiFramework/")
print(f"©2023{Fore.RESET}")

def warn(message):
    print(Fore.LIGHTRED_EX + "WARN:", message)
    print(Fore.RESET + "")

class imageLoad:
    def load(imagePath = ""):
        ### Loads an image

        try:
            return pygame.image.load(imagePath).convert_alpha()

        except Exception as E:
            warn(E)

    def loadNoBackround(imagePath = ""):
        ### Loads an image without backround
        
        try:
            return pygame.image.load(imagePath).convert()

        except Exception as E:
            warn(E)

class create:
    def title(title = f"PyKui {version_} window"):
        if (title == ""):
            title = f"PyKuy {version_} window"

        display.set_caption(title)

    def WINDOW(title = f"PyKuy {version_} window", x = 500, y = 500, flags = RESIZABLE):
        ### Create a window

        global screen, windowsCreated, windowX, windowY

        windowsCreated += 1

        if (windowsCreated == 1 or allowMoreWindows == True):
            if (title == ""):
                title = f"PyKuy {version_} window"

            windowX = x
            windowY = y
            
            if (minWindowSizeAllowed == True):
                if (windowX < 100 and windowX != 0):
                    raise pyKuiWindowSizeError(f"WindowX size ({windowX} px) is smaller than 100")

                if (windowY < 100 and windowY != 0):
                    raise pyKuiWindowSizeError(f"WindowY size ({windowY} px) is smaller than 100")

                if (windowX < 0):
                    raise pyKuiWindowSizeError(f"WindowX size ({windowX}px) has negative values")

                if (windowY < 0):
                    raise pyKuiWindowSizeError(f"WindowY size ({windowY}px) has negative values")

            if (autoResizeWhen00 == True):
                if (windowX == 0 and windowY == 0):
                    screen = pygame.display.set_mode((0, 0))

                    windowX = screen.get_size()[0]
                    windowY = screen.get_size()[1]

            pygame.display.set_caption(title)

        else:
            raise pyKuiWindowsLimit("There is more than 1 window")

        if (windowsCreated > 1):
            warn("More than one window created, canceled")

        return pygame.display.set_mode((windowX, windowY), flags)

def openFont(fontName, size):
    ### Open a system font

    return pygame.font.SysFont(fontName, size)

class render:
    def text(font = pygame.font.SysFont, text = "None", goodQuality = True, r = 0, g = 0, b = 0):
        ### You can save text in a variable an then you can manualy blit it

        return font.render(text, goodQuality, (r, g, b))

def printw(windowSurface = pygame.Surface, font = pygame.font.SysFont, text = "None", goodQuality = True, r = 0, g = 0, b = 0, x = 0, y = 0):
    ### Prints text in the screen

    global printwText

    text = str(text)

    printwText = font.render(text, goodQuality, (r, g, b))
    
    blit(windowSurface, printwText, x, y)

class rule:
    def removeList():
        ### Removes item in rulesArg1 and rulesArg2

        rulesArg1.reverse()
        rulesArg1.pop(1)
        rulesArg1.reverse()

        rulesArg2.reverse()
        rulesArg2.pop(1)
        rulesArg2.reverse()

    def get():
        ### Prints the list of commands that you used

        print(rulesArg1)
        print(rulesArg2)

    def set(arg1 = "", arg2 = ""):
        ### Sets rule for program

        global minWindowSizeAllowed, autoResizeWhen00, allowMoreWindows

        try:
            rulesArg1.append(str(arg1))
            rulesArg2.append(str(arg2))

            if (arg1 == "min window size" or arg1 == "mws1" or arg1 == "minimum window size"):
                minWindowSizeAllowed = bool(arg2)

            elif (arg1 == "auto resize when 00" or arg1 == "arw001"):
                autoResizeWhen00 = bool(arg2)

            elif (arg1 == "allow more windows" or arg1 == "amw1"):
                allowMoreWindows = bool(arg2)

            else:
                print(Fore.RED + "Unknown command for arg1")

                rule.removeList()

        except Exception as E:
            print(Fore.RED + "ERROR:", E)

        print(Fore.RESET + "")

def blit(windowSurface = pygame.Surface, surface = pygame.Surface, x = 0, y = 0):
    ### Shows (blits) image (surface) in windowSurface in given x and y coordinates

    windowSurface.blit(surface, (x, y))

def smoothScaledBlit(windowSurface = pygame.Surface, surface = pygame.Surface, x = 0, y = 0, w = 0, h = 0):
    ### Shows (blits) image (surface) in windowSurface in given x and y coordinates and smooth resizes the image in the given w and h

    surface = pygame.transform.smoothscale(surface, size=(w, h))

    blit(windowSurface, surface, (x, y))

def scaledBlit(windowSurface = pygame.Surface, surface = pygame.Surface, x = 0, y = 0, w = 0, h = 0):
    ### Shows (blits) image (surface) in windowSurface in given x and y coordinates and resizes the image in the given w and h

    surface = pygame.transform.scale(surface, size=(w, h))

    blit(windowSurface, surface, (x, y))

def smoothScale(surface = pygame.Surface, w = 0, h = 0):
    ### Smooths scales a surface

    surface = pygame.transform.smoothscale(surface, size=(w, h))

def scale(surface = pygame.Surface, w = 0, h = 0):
    ### Scales a surface

    surface = pygame.transform.scale(surface, size=(w, h))

def setIcon(iconPath):
    ### Sets the program icon

    pygame.display.set_icon(iconPath)

class frameRate:
    def setFrameRate(FPS):
        ### Sets frame rate

        global defaultFPS

        defaultFPS = FPS

    def tick():
        clockTick.tick(defaultFPS)

class draw:
    def rect(windowSurface, r, g, b, x, y, w = 0, h = 0, borderRad = 0):
        ### The surface spot is in wich you will have to enter the 'window' variable of your game
        ## x -> position x
        ## y -> position y
        ## w -> width of the rect
        ## h -> height of the rect

        pygame.draw.rect(windowSurface, (r,g,b), pygame.Rect(x, y, w, h), borderRad)

    def circl(surface, r, g, b, x, y, R=0, w = 0):
        ### The surface spot is in wich you will have to enter the 'window' variable of your game
        ## x -> position x
        ## y -> position y
        ## w -> width of the circle
        ## h -> height of the rect

        pygame.draw.circle(surface, (r,g,b), (x, y), R, w)

    def line(windowSurface = pygame.Surface, r = 0, g = 0, b = 0, width = 1, startX = 0, startY = 0, endX = windowX, endY = windowY):
        pygame.draw.line(windowSurface, color=(r, g, b), start_pos=(startX, startY), end_pos=(endX, endY), width=width)

class cursor:
    def goto(x = 0, y = 0):
        pygame.mouse.set_pos([x, y])

    def getx():
        global mx

        mx = pygame.mouse.get_pos()[0]

    def gety():
        global my
        
        my = pygame.mouse.get_pos()[1]

    def getxy():
        global mx, my

        mx = pygame.mouse.get_pos()[0]
        my = pygame.mouse.get_pos()[1]

    def showCursor(show = True):
        if (show == True):
            pygame.mouse.set_visible(True)

        else:
            pygame.mouse.set_visible(False)

    def setCursor(windowSurface = pygame.Surface, cursorImage = pygame.Surface, size = 25):
        cursor.showCursor(False)
        cursor.getxy()

        if (cursorImage == "rect"):
            draw.rect(windowSurface, 255, 0, 0, mx, my, size, size)

        else:
            blit(windowSurface, cursorImage, mx, my, size, size)

def end(type = 0):
    ### Ends the program

    print(Fore.RESET + "")

    pygame.quit()
    sys.exit(type)

print("Done!")
