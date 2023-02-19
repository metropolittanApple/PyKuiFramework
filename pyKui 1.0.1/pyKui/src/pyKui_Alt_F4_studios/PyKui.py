# PyKui 1.0
# Created by: Pau Cava and Paul Cannon
# The next generation framework to make python graphics simpler and faster
# Made with pygame
# (C)2023

from pyKui_Alt_F4_studios.imports import *
from pyKui_Alt_F4_studios.errors import *
from pyKui_Alt_F4_studios.rendering import *
from pyKui_Alt_F4_studios.rules import *
from pyKui_Alt_F4_studios.text import *
from pyKui_Alt_F4_studios.audio import *
from pyKui_Alt_F4_studios.variables import *

print("pygame.init")

pygame.init()
pygame.mixer.init()

print("Checking python version")

if (int(platform.python_version_tuple()[0]) < 3):
    window = pygame.display.set_mode((500, 500))

    while (1):
        pygame.display.update()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            break

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit(1)
        
        font = pygame.font.SysFont("Arial", 35)
        text = font.render("You need python3 to get", True, (255, 255, 255))
        text2 = font.render("better experience", True, (255, 255, 255))
        text3 = font.render("Press ESC to continue", True, (255, 255, 255))

        window.blit(text, (10, 10))
        window.blit(text2, (10, 10 + 40))
        window.blit(text3, (10, 10 + 40 * 2))
    
    del font
    del text
    del text2
    del text3
    del window

print("Accept")

print("Loading pre images")

print(f"{Fore.YELLOW}WELCOME TO")
print(f"{Fore.WHITE}PyKui {version_}")
print(f"{Fore.YELLOW}Web: https://metropolittanapple.github.io/pykuiframework/")
print(f"©2023{Fore.RESET}")


def end(type = 0):
    ### Ends the program

    print(Fore.RESET + "")

    pygame.quit()
    sys.exit(type)

def update():
    pygame.display.update()

    if (autoFLimit):
        frameRate.tick()

def simpleUpdate(fill = False, windowSurface = pygame.Surface, r = 0, g = 0, b = 0):
    ### Does a simple update

    update()

    if (fill):
        if (r < 0):
            r = 0

        if (g < 0):
            g = 0
        
        if (b < 0):
            b = 0

        windowSurface.fill((r, g, b))

    for event in getEvent():
        if event.type == pygame.QUIT:
            end(0)

setIcon(PyKuiIcon)
frameRate.limit(60)
