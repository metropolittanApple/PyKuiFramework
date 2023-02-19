from pyKui_Alt_F4_studios.imports import *
from pyKui_Alt_F4_studios.variables import *
from pyKui_Alt_F4_studios.errors import *
from pyKui_Alt_F4_studios.rendering import *

class open:
    def openSysFont(fontName, size):
        ### Open a system font

        try:
            return pygame.font.SysFont(fontName, size)

        except:
            warn("Can't open font")

    def openFont(fontName, size):
        ### Open a custom font

        try:
            return pygame.font.Font(fontName, size)

        except:
            warn("Can't open font")

def saveSysText(font = pygame.font.SysFont, text = "None", goodQuality = True, r = 0, g = 0, b = 0):
    ### You can save text in a variable an then you can manualy blit it

    if (goodQuality != True and goodQuality != False):
        goodQuality = False
        warn("var 'goodQuality is not bool'")

    if (r < 0):
        r = 0

    if (g < 0):
        g = 0
    
    if (b < 0):
        b = 0

    return font.render(text, goodQuality, (r, g, b))

def saveText(font = pygame.font.Font, text = "None", goodQuality = True, r = 0, g = 0, b = 0):
    ### You can save text in a variable an then you can manualy blit it

    if (goodQuality != True and goodQuality != False):
        goodQuality = False
        warn("var 'goodQuality is not bool'")

    if (r < 0):
        r = 0

    if (g < 0):
        g = 0
    
    if (b < 0):
        b = 0

    return font.render(text, goodQuality, (r, g, b))

def printw(windowSurface = pygame.Surface, font = pygame.font.SysFont, text = "None", goodQuality = True, r = 0, g = 0, b = 0, x = 0, y = 0):
    ### Prints text in the screen
    
    global printwText

    if (goodQuality != True and goodQuality != False):
        goodQuality = False
        warn("var 'goodQuality is not bool'")

    printwText = font.render(str(text), goodQuality, (r, g, b))
    
    blit(windowSurface, printwText, x, y)