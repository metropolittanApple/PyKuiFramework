from pyKui_Alt_F4_studios.imports import *

class pyKuiWindowSizeError(Exception):
    pass

class pyKuiMinWindowSizeError(Exception):
    pass

class pyKuiWindowsLimitError(Exception):
    pass

class pyKuiNoDrawerInitError(Exception):
    pass

class pyKuiFpsLimitError(Exception):
    pass

class pyKuiAudioNotInit(Exception):
    pass

def warn(message):
    ### Shows a warning in light red

    print(Fore.LIGHTRED_EX + "WARN:", message)
    print(Fore.RESET + "")
