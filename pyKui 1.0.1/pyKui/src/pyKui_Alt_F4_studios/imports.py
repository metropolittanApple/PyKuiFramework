import sys
import os
import platform

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

class pyKuiInstallError(Exception):
    pass

try:
    import pygame
    from pygame.mixer import *
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
