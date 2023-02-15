# PyKui beta 1
# Created by: Pau Cava and Paul Cannon
# The next generation framework to make python graphics simpler and faster
# Made with pygame
# (C) 2023

print("Loading...")

class pyKuiWindowSizeError(Exception):
    pass

class pyKuiMinWindowSizeError(Exception):
    pass

class pyKuiInstallError(Exception):
    pass

class pyKuiWindowsLimitError(Exception):
    pass

class pyKuiNoDrawerInitError(Exception):
    pass

import sys
import os
import platform

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

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

PyKuiIcon = pygame.image.load("rsrc/images/icon/icon v1.png")

print("Loading variables")

key = pygame.key.get_pressed

version_ = "beta 1"

noDrawerInitErrorMessage = "Do pyKui.sdrawer.init() to initalize the simple drawing functions"
noCDrawerInitErrorMessage = "Do pyKui.drawer.init() to initalize the simple drawing functions"

printwText = "None"
rulesArg1 = []
rulesArg2 = []
windowX = 0
windowY = 0
defaultFPS = 0.1
windowsCreated = 0
i = 0
penX = 0
penY = 0

frameRateSet = False

initedSDrawer = False
initedDrawer = False
autoFLimit = True

isPenUp = True

getEvent = pygame.event.get

event = pygame.event
display = pygame.display
image = pygame.image
time = pygame.time
mouse = pygame.mouse
Cursor = pygame.Cursor
joystick = pygame.joystick
bufferproxy = pygame.bufferproxy
color = pygame.color
Color = pygame.Color
version = pygame.version
Vector3 = pygame.Vector3
Vector2 = pygame.Vector2
surfarray = pygame.surfarray
surface = pygame.surface
sndarray = pygame.sndarray
sprite = pygame.sprite
scrap = pygame.scrap
Rect_ = pygame.Rect
rect = pygame.rect
pixelcopy = pygame.pixelcopy
pixelarray = pygame.pixelarray
pixelArray = pygame.PixelArray
register_quit = pygame.register_quit
set_error = pygame.set_error
mixer = pygame.mixer
math = pygame.math
mask = pygame.mask
fastevent = pygame.fastevent
event = pygame.event
error = pygame.error
Rect_ = pygame.Rect
ACTIVEEVENT_ = pygame.ACTIVEEVENT
ANYFORMAT_ = pygame.ANYFORMAT
APPACTIVE_ = pygame.APPACTIVE
APPFOCUSMOUSE_ = pygame.APPFOCUSMOUSE
APPINPUTFOCUS_ = pygame.APPINPUTFOCUS
ASYNCBLIT_ = pygame.ASYNCBLIT
AUDIODEVICEADDED_ = pygame.AUDIODEVICEADDED
AUDIODEVICEREMOVED_ = pygame.AUDIODEVICEREMOVED
AUDIO_ALLOW_ANY_CHANGE_ = pygame.AUDIO_ALLOW_ANY_CHANGE
AUDIO_ALLOW_CHANNELS_CHANGE_ = pygame.AUDIO_ALLOW_CHANNELS_CHANGE
AUDIO_ALLOW_FORMAT_CHANGE_ = pygame.AUDIO_ALLOW_FORMAT_CHANGE
AUDIO_ALLOW_FREQUENCY_CHANGE_ = pygame.AUDIO_ALLOW_FREQUENCY_CHANGE
AUDIO_S16_ = pygame.AUDIO_S16
AUDIO_S16LSB_ = pygame.AUDIO_S16LSB
AUDIO_S16MSB_ = pygame.AUDIO_S16MSB
AUDIO_S16SYS_ = pygame.AUDIO_S16SYS
AUDIO_S8_ = pygame.AUDIO_S8
AUDIO_U16_ = pygame.AUDIO_U16
AUDIO_U16LSB_ = pygame.AUDIO_U16LSB
AUDIO_U16MSB_ = pygame.AUDIO_U16MSB
AUDIO_U16SYS_ = pygame.AUDIO_U16SYS
AUDIO_U8_ = pygame.AUDIO_U8
BIG_ENDIAN_ = pygame.BIG_ENDIAN
BLENDMODE_ADD_ = pygame.BLENDMODE_ADD
BLENDMODE_BLEND_ = pygame.BLENDMODE_BLEND
BLENDMODE_MOD_ = pygame.BLENDMODE_MOD
BLENDMODE_NONE_ = pygame.BLENDMODE_NONE
BLEND_ADD_ = pygame.BLEND_ADD
BLEND_MAX_ = pygame.BLEND_MAX
BLEND_MIN_ = pygame.BLEND_MIN
BLEND_MULT_ = pygame.BLEND_MULT
BLEND_PREMULTIPLIED_ = pygame.BLEND_PREMULTIPLIED
BLEND_ALPHA_SDL2_ = pygame.BLEND_ALPHA_SDL2
BLEND_RGBA_ADD_ = pygame.BLEND_RGBA_ADD
BLEND_RGBA_MAX_ = pygame.BLEND_RGBA_MAX
BLEND_RGBA_MIN_ = pygame.BLEND_RGBA_MIN
BLEND_RGBA_MULT_ = pygame.BLEND_RGBA_MULT
BLEND_RGBA_SUB_ = pygame.BLEND_RGBA_SUB
BLEND_RGB_ADD_ = pygame.BLEND_RGB_ADD
BLEND_RGB_MAX_ = pygame.BLEND_RGB_MAX
BLEND_RGB_MIN_ = pygame.BLEND_RGB_MIN
BLEND_RGB_MULT_ = pygame.BLEND_RGB_MULT
BLEND_RGB_SUB_ = pygame.BLEND_RGB_SUB
BLEND_SUB_ = pygame.BLEND_SUB
BUTTON_LEFT_ = pygame.BUTTON_LEFT
BUTTON_MIDDLE_ = pygame.BUTTON_MIDDLE
BUTTON_RIGHT_ = pygame.BUTTON_RIGHT
BUTTON_WHEELDOWN_ = pygame.BUTTON_WHEELDOWN
BUTTON_WHEELUP_ = pygame.BUTTON_WHEELUP
BUTTON_X1_ = pygame.BUTTON_X1
BUTTON_X2_ = pygame.BUTTON_X2
CONTROLLERAXISMOTION_ = pygame.CONTROLLERAXISMOTION
CONTROLLERBUTTONDOWN_ = pygame.CONTROLLERBUTTONDOWN
CONTROLLERBUTTONUP_ = pygame.CONTROLLERBUTTONUP
CONTROLLERDEVICEADDED_ = pygame.CONTROLLERDEVICEADDED
CONTROLLERDEVICEREMAPPED_ = pygame.CONTROLLERDEVICEREMAPPED
CONTROLLERDEVICEREMOVED_ = pygame.CONTROLLERDEVICEREMOVED
CONTROLLER_AXIS_INVALID_ = pygame.CONTROLLER_AXIS_INVALID
CONTROLLER_AXIS_LEFTX_ = pygame.CONTROLLER_AXIS_LEFTX
CONTROLLER_AXIS_LEFTY_ = pygame.CONTROLLER_AXIS_LEFTY
CONTROLLER_AXIS_MAX_ = pygame.CONTROLLER_AXIS_MAX
CONTROLLER_AXIS_RIGHTX_ = pygame.CONTROLLER_AXIS_RIGHTX
CONTROLLER_AXIS_RIGHTY_ = pygame.CONTROLLER_AXIS_RIGHTY
CONTROLLER_AXIS_TRIGGERLEFT_ = pygame.CONTROLLER_AXIS_TRIGGERLEFT
CONTROLLER_AXIS_TRIGGERRIGHT_ = pygame.CONTROLLER_AXIS_TRIGGERRIGHT
CONTROLLER_BUTTON_A_ = pygame.CONTROLLER_BUTTON_A
CONTROLLER_BUTTON_B_ = pygame.CONTROLLER_BUTTON_B
CONTROLLER_BUTTON_BACK_ = pygame.CONTROLLER_BUTTON_BACK
CONTROLLER_BUTTON_DPAD_DOWN_ = pygame.CONTROLLER_BUTTON_DPAD_DOWN
CONTROLLER_BUTTON_DPAD_LEFT_ = pygame.CONTROLLER_BUTTON_DPAD_LEFT
CONTROLLER_BUTTON_DPAD_RIGHT_ = pygame.CONTROLLER_BUTTON_DPAD_RIGHT
CONTROLLER_BUTTON_DPAD_UP_ = pygame.CONTROLLER_BUTTON_DPAD_UP
CONTROLLER_BUTTON_GUIDE_ = pygame.CONTROLLER_BUTTON_GUIDE
CONTROLLER_BUTTON_INVALID_ = pygame.CONTROLLER_BUTTON_INVALID
CONTROLLER_BUTTON_LEFTSHOULDER_ = pygame.CONTROLLER_BUTTON_LEFTSHOULDER
CONTROLLER_BUTTON_LEFTSTICK_ = pygame.CONTROLLER_BUTTON_LEFTSTICK
CONTROLLER_BUTTON_MAX_ = pygame.CONTROLLER_BUTTON_MAX
CONTROLLER_BUTTON_RIGHTSHOULDER_ = pygame.CONTROLLER_BUTTON_RIGHTSHOULDER
CONTROLLER_BUTTON_RIGHTSTICK_ = pygame.CONTROLLER_BUTTON_RIGHTSTICK
CONTROLLER_BUTTON_START_ = pygame.CONTROLLER_BUTTON_START
CONTROLLER_BUTTON_X_ = pygame.CONTROLLER_BUTTON_X
CONTROLLER_BUTTON_Y_ = pygame.CONTROLLER_BUTTON_Y
DOUBLEBUF_ = pygame.DOUBLEBUF
DROPBEGIN_ = pygame.DROPBEGIN
DROPCOMPLETE_ = pygame.DROPCOMPLETE
DROPFILE_ = pygame.DROPFILE
DROPTEXT_ = pygame.DROPTEXT
FINGERDOWN_ = pygame.FINGERDOWN
FINGERMOTION_ = pygame.FINGERMOTION
FINGERUP_ = pygame.FINGERUP
FULLSCREEN_ = pygame.FULLSCREEN
GL_ACCELERATED_VISUAL_ = pygame.GL_ACCELERATED_VISUAL
GL_ACCUM_ALPHA_SIZE_ = pygame.GL_ACCUM_ALPHA_SIZE
GL_ACCUM_BLUE_SIZE_ = pygame.GL_ACCUM_BLUE_SIZE
GL_ACCUM_GREEN_SIZE_ = pygame.GL_ACCUM_GREEN_SIZE
GL_ACCUM_RED_SIZE_ = pygame.GL_ACCUM_RED_SIZE
GL_ALPHA_SIZE_ = pygame.GL_ALPHA_SIZE
GL_BLUE_SIZE_ = pygame.GL_BLUE_SIZE
GL_BUFFER_SIZE_ = pygame.GL_BUFFER_SIZE
GL_CONTEXT_DEBUG_FLAG_ = pygame.GL_CONTEXT_DEBUG_FLAG
GL_CONTEXT_FLAGS_ = pygame.GL_CONTEXT_FLAGS
GL_CONTEXT_FORWARD_COMPATIBLE_FLAG_ = pygame.GL_CONTEXT_FORWARD_COMPATIBLE_FLAG
GL_CONTEXT_MAJOR_VERSION_ = pygame.GL_CONTEXT_MAJOR_VERSION
GL_CONTEXT_MINOR_VERSION_ = pygame.GL_CONTEXT_MINOR_VERSION
GL_CONTEXT_PROFILE_COMPATIBILITY_ = pygame.GL_CONTEXT_PROFILE_COMPATIBILITY
GL_CONTEXT_PROFILE_CORE_ = pygame.GL_CONTEXT_PROFILE_CORE
GL_CONTEXT_PROFILE_ES_ = pygame.GL_CONTEXT_PROFILE_ES
GL_CONTEXT_PROFILE_MASK_ = pygame.GL_CONTEXT_PROFILE_MASK
GL_CONTEXT_RELEASE_BEHAVIOR_ = pygame.GL_CONTEXT_RELEASE_BEHAVIOR
GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH_ = pygame.GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH
GL_CONTEXT_RELEASE_BEHAVIOR_NONE_ = pygame.GL_CONTEXT_RELEASE_BEHAVIOR_NONE
GL_CONTEXT_RESET_ISOLATION_FLAG_ = pygame.GL_CONTEXT_RESET_ISOLATION_FLAG
GL_CONTEXT_ROBUST_ACCESS_FLAG_ = pygame.GL_CONTEXT_ROBUST_ACCESS_FLAG
GL_DEPTH_SIZE_ = pygame.GL_DEPTH_SIZE
GL_DOUBLEBUFFER_ = pygame.GL_DOUBLEBUFFER
GL_FRAMEBUFFER_SRGB_CAPABLE_ = pygame.GL_FRAMEBUFFER_SRGB_CAPABLE
GL_GREEN_SIZE_ = pygame.GL_GREEN_SIZE
GL_MULTISAMPLEBUFFERS_ = pygame.GL_MULTISAMPLEBUFFERS
GL_MULTISAMPLESAMPLES_ = pygame.GL_MULTISAMPLESAMPLES
GL_RED_SIZE_ = pygame.GL_RED_SIZE
GL_SHARE_WITH_CURRENT_CONTEXT_ = pygame.GL_SHARE_WITH_CURRENT_CONTEXT
GL_STENCIL_SIZE_ = pygame.GL_STENCIL_SIZE
GL_STEREO_ = pygame.GL_STEREO
GL_SWAP_CONTROL_ = pygame.GL_SWAP_CONTROL
HAT_CENTERED_ = pygame.HAT_CENTERED
HAT_DOWN_ = pygame.HAT_DOWN
HAT_LEFT_ = pygame.HAT_LEFT
HAT_LEFTDOWN_ = pygame.HAT_LEFTDOWN
HAT_LEFTUP_ = pygame.HAT_LEFTUP
HAT_RIGHT_ = pygame.HAT_RIGHT
HAT_RIGHTDOWN_ = pygame.HAT_RIGHTDOWN
HAT_RIGHTUP_ = pygame.HAT_RIGHTUP
HAT_UP_ = pygame.HAT_UP
HIDDEN_ = pygame.HIDDEN
HWACCEL_ = pygame.HWACCEL
HWPALETTE_ = pygame.HWPALETTE
HWSURFACE_ = pygame.HWSURFACE
JOYAXISMOTION_ = pygame.JOYAXISMOTION
JOYBALLMOTION_ = pygame.JOYBALLMOTION
JOYBUTTONDOWN_ = pygame.JOYBUTTONDOWN
JOYBUTTONUP_ = pygame.JOYBUTTONUP
JOYHATMOTION_ = pygame.JOYHATMOTION
JOYDEVICEADDED_ = pygame.JOYDEVICEADDED
JOYDEVICEREMOVED_ = pygame.JOYDEVICEREMOVED
KEYDOWN_ = pygame.KEYDOWN
KEYUP_ = pygame.KEYUP
KMOD_ALT_ = pygame.KMOD_ALT
KMOD_CAPS_ = pygame.KMOD_CAPS
KMOD_CTRL_ = pygame.KMOD_CTRL
KMOD_GUI_ = pygame.KMOD_GUI
KMOD_LALT_ = pygame.KMOD_LALT
KMOD_LCTRL_ = pygame.KMOD_LCTRL
KMOD_LGUI_ = pygame.KMOD_LGUI
KMOD_LMETA_ = pygame.KMOD_LMETA
KMOD_LSHIFT_ = pygame.KMOD_LSHIFT
KMOD_META_ = pygame.KMOD_META
KMOD_MODE_ = pygame.KMOD_MODE
KMOD_NONE_ = pygame.KMOD_NONE
KMOD_NUM_ = pygame.KMOD_NUM
KMOD_RALT_ = pygame.KMOD_RALT
KMOD_RCTRL_ = pygame.KMOD_RCTRL
KMOD_RGUI_ = pygame.KMOD_RGUI
KMOD_RMETA_ = pygame.KMOD_RMETA
KMOD_RSHIFT_ = pygame.KMOD_RSHIFT
KMOD_SHIFT_ = pygame.KMOD_SHIFT
KSCAN_0_ = pygame.KSCAN_0
KSCAN_1_ = pygame.KSCAN_1
KSCAN_2_ = pygame.KSCAN_2
KSCAN_3_ = pygame.KSCAN_3
KSCAN_4_ = pygame.KSCAN_4
KSCAN_5_ = pygame.KSCAN_5
KSCAN_6_ = pygame.KSCAN_6
KSCAN_7_ = pygame.KSCAN_7
KSCAN_8_ = pygame.KSCAN_8
KSCAN_9_ = pygame.KSCAN_9
KSCAN_A_ = pygame.KSCAN_A
KSCAN_APOSTROPHE_ = pygame.KSCAN_APOSTROPHE
KSCAN_B_ = pygame.KSCAN_B
KSCAN_BACKSLASH_ = pygame.KSCAN_BACKSLASH
KSCAN_BACKSPACE_ = pygame.KSCAN_BACKSPACE
KSCAN_BREAK_ = pygame.KSCAN_BREAK
KSCAN_C_ = pygame.KSCAN_C
KSCAN_CAPSLOCK_ = pygame.KSCAN_CAPSLOCK
KSCAN_CLEAR_ = pygame.KSCAN_CLEAR
KSCAN_COMMA_ = pygame.KSCAN_COMMA
KSCAN_CURRENCYSUBUNIT_ = pygame.KSCAN_CURRENCYSUBUNIT
KSCAN_CURRENCYUNIT_ = pygame.KSCAN_CURRENCYUNIT
KSCAN_D_ = pygame.KSCAN_D
KSCAN_DELETE_ = pygame.KSCAN_DELETE
KSCAN_DOWN_ = pygame.KSCAN_DOWN
KSCAN_E_ = pygame.KSCAN_E
KSCAN_END_ = pygame.KSCAN_END
KSCAN_EQUALS_ = pygame.KSCAN_EQUALS
KSCAN_ESCAPE_ = pygame.KSCAN_ESCAPE
KSCAN_EURO_ = pygame.KSCAN_EURO
KSCAN_F_ = pygame.KSCAN_F
KSCAN_F1_ = pygame.KSCAN_F1
KSCAN_F10_ = pygame.KSCAN_F10
KSCAN_F11_ = pygame.KSCAN_F11
KSCAN_F12_ = pygame.KSCAN_F12
KSCAN_F13_ = pygame.KSCAN_F13
KSCAN_F14_ = pygame.KSCAN_F14
KSCAN_F15_ = pygame.KSCAN_F15
KSCAN_F2_ = pygame.KSCAN_F2
KSCAN_F3_ = pygame.KSCAN_F3
KSCAN_F4_ = pygame.KSCAN_F4
KSCAN_F5_ = pygame.KSCAN_F5
KSCAN_F6_ = pygame.KSCAN_F6
KSCAN_F7_ = pygame.KSCAN_F7
KSCAN_F8_ = pygame.KSCAN_F8
KSCAN_F9_ = pygame.KSCAN_F9
KSCAN_G_ = pygame.KSCAN_G
KSCAN_GRAVE_ = pygame.KSCAN_GRAVE
KSCAN_H_ = pygame.KSCAN_H
KSCAN_HELP_ = pygame.KSCAN_HELP
KSCAN_HOME_ = pygame.KSCAN_HOME
KSCAN_I_ = pygame.KSCAN_I
KSCAN_INSERT_ = pygame.KSCAN_INSERT
KSCAN_INTERNATIONAL1_ = pygame.KSCAN_INTERNATIONAL1
KSCAN_INTERNATIONAL2_ = pygame.KSCAN_INTERNATIONAL2
KSCAN_INTERNATIONAL3_ = pygame.KSCAN_INTERNATIONAL3
KSCAN_INTERNATIONAL4_ = pygame.KSCAN_INTERNATIONAL4
KSCAN_INTERNATIONAL5_ = pygame.KSCAN_INTERNATIONAL5
KSCAN_INTERNATIONAL6_ = pygame.KSCAN_INTERNATIONAL6
KSCAN_INTERNATIONAL7_ = pygame.KSCAN_INTERNATIONAL7
KSCAN_INTERNATIONAL8_ = pygame.KSCAN_INTERNATIONAL8
KSCAN_INTERNATIONAL9_ = pygame.KSCAN_INTERNATIONAL9
KSCAN_J_ = pygame.KSCAN_J
KSCAN_K_ = pygame.KSCAN_K
KSCAN_KP0_ = pygame.KSCAN_KP0
KSCAN_KP1_ = pygame.KSCAN_KP1
KSCAN_KP2_ = pygame.KSCAN_KP2
KSCAN_KP3_ = pygame.KSCAN_KP3
KSCAN_KP4_ = pygame.KSCAN_KP4
KSCAN_KP5_ = pygame.KSCAN_KP5
KSCAN_KP6_ = pygame.KSCAN_KP6
KSCAN_KP7_ = pygame.KSCAN_KP7
KSCAN_KP8_ = pygame.KSCAN_KP8
KSCAN_KP9_ = pygame.KSCAN_KP9
KSCAN_KP_0_ = pygame.KSCAN_KP_0
KSCAN_KP_1_ = pygame.KSCAN_KP_1
KSCAN_KP_2_ = pygame.KSCAN_KP_2
KSCAN_KP_3_ = pygame.KSCAN_KP_3
KSCAN_KP_4_ = pygame.KSCAN_KP_4
KSCAN_KP_5_ = pygame.KSCAN_KP_5
KSCAN_KP_6_ = pygame.KSCAN_KP_6
KSCAN_KP_7_ = pygame.KSCAN_KP_7
KSCAN_KP_8_ = pygame.KSCAN_KP_8
KSCAN_KP_9_ = pygame.KSCAN_KP_9
KSCAN_KP_DIVIDE_ = pygame.KSCAN_KP_DIVIDE
KSCAN_KP_ENTER_ = pygame.KSCAN_KP_ENTER
KSCAN_KP_EQUALS_ = pygame.KSCAN_KP_EQUALS
KSCAN_KP_MINUS_ = pygame.KSCAN_KP_MINUS
KSCAN_KP_MULTIPLY_ = pygame.KSCAN_KP_MULTIPLY
KSCAN_KP_PERIOD_ = pygame.KSCAN_KP_PERIOD
KSCAN_KP_PLUS_ = pygame.KSCAN_KP_PLUS
KSCAN_L_ = pygame.KSCAN_L
KSCAN_LALT_ = pygame.KSCAN_LALT
KSCAN_LANG1_ = pygame.KSCAN_LANG1
KSCAN_LANG2_ = pygame.KSCAN_LANG2
KSCAN_LANG3_ = pygame.KSCAN_LANG3
KSCAN_LANG4_ = pygame.KSCAN_LANG4
KSCAN_LANG5_ = pygame.KSCAN_LANG5
KSCAN_LANG6_ = pygame.KSCAN_LANG6
KSCAN_LANG7_ = pygame.KSCAN_LANG7
KSCAN_LANG8_ = pygame.KSCAN_LANG8
KSCAN_LANG9_ = pygame.KSCAN_LANG9
KSCAN_LCTRL_ = pygame.KSCAN_LCTRL
KSCAN_LEFT_ = pygame.KSCAN_LEFT
KSCAN_LEFTBRACKET_ = pygame.KSCAN_LEFTBRACKET
KSCAN_LGUI_ = pygame.KSCAN_LGUI
KSCAN_LMETA_ = pygame.KSCAN_LMETA
KSCAN_LSHIFT_ = pygame.KSCAN_LSHIFT
KSCAN_LSUPER_ = pygame.KSCAN_LSUPER
KSCAN_M_ = pygame.KSCAN_M
KSCAN_MENU_ = pygame.KSCAN_MENU
KSCAN_MINUS_ = pygame.KSCAN_MINUS
KSCAN_MODE_ = pygame.KSCAN_MODE
KSCAN_N_ = pygame.KSCAN_N
KSCAN_NONUSBACKSLASH_ = pygame.KSCAN_NONUSBACKSLASH
KSCAN_NONUSHASH_ = pygame.KSCAN_NONUSHASH
KSCAN_NUMLOCK_ = pygame.KSCAN_NUMLOCK
KSCAN_NUMLOCKCLEAR_ = pygame.KSCAN_NUMLOCKCLEAR
KSCAN_O_ = pygame.KSCAN_O
KSCAN_P_ = pygame.KSCAN_P
KSCAN_PAGEDOWN_ = pygame.KSCAN_PAGEDOWN
KSCAN_PAGEUP_ = pygame.KSCAN_PAGEUP
KSCAN_PAUSE_ = pygame.KSCAN_PAUSE
KSCAN_PERIOD_ = pygame.KSCAN_PERIOD
KSCAN_POWER_ = pygame.KSCAN_POWER
KSCAN_PRINT_ = pygame.KSCAN_PRINT
KSCAN_PRINTSCREEN_ = pygame.KSCAN_PRINTSCREEN
KSCAN_Q_ = pygame.KSCAN_Q
KSCAN_R_ = pygame.KSCAN_R
KSCAN_RALT_ = pygame.KSCAN_RALT
KSCAN_RCTRL_ = pygame.KSCAN_RCTRL
KSCAN_RETURN_ = pygame.KSCAN_RETURN
KSCAN_RGUI_ = pygame.KSCAN_RGUI
KSCAN_RIGHT_ = pygame.KSCAN_RIGHT
KSCAN_RIGHTBRACKET_ = pygame.KSCAN_RIGHTBRACKET
KSCAN_RMETA_ = pygame.KSCAN_RMETA
KSCAN_RSHIFT_ = pygame.KSCAN_RSHIFT
KSCAN_RSUPER_ = pygame.KSCAN_RSUPER
KSCAN_S_ = pygame.KSCAN_S
KSCAN_SCROLLLOCK_ = pygame.KSCAN_SCROLLLOCK
KSCAN_SCROLLOCK_ = pygame.KSCAN_SCROLLOCK
KSCAN_SEMICOLON_ = pygame.KSCAN_SEMICOLON
KSCAN_SLASH_ = pygame.KSCAN_SLASH
KSCAN_SPACE_ = pygame.KSCAN_SPACE
KSCAN_SYSREQ_ = pygame.KSCAN_SYSREQ
KSCAN_T_ = pygame.KSCAN_T
KSCAN_TAB_ = pygame.KSCAN_TAB
KSCAN_U_ = pygame.KSCAN_U
KSCAN_UNKNOWN_ = pygame.KSCAN_UNKNOWN
KSCAN_UP_ = pygame.KSCAN_UP
KSCAN_V_ = pygame.KSCAN_V
KSCAN_W_ = pygame.KSCAN_W
KSCAN_X_ = pygame.KSCAN_X
KSCAN_Y_ = pygame.KSCAN_Y
KSCAN_Z_ = pygame.KSCAN_Z
K_0_ = pygame.K_0
K_1_ = pygame.K_1
K_2_ = pygame.K_2
K_3_ = pygame.K_3
K_4_ = pygame.K_4
K_5_ = pygame.K_5
K_6_ = pygame.K_6
K_7_ = pygame.K_7
K_8_ = pygame.K_8
K_9_ = pygame.K_9
K_AC_BACK_ = pygame.K_AC_BACK
K_AMPERSAND_ = pygame.K_AMPERSAND
K_ASTERISK_ = pygame.K_ASTERISK
K_AT_ = pygame.K_AT
K_BACKQUOTE_ = pygame.K_BACKQUOTE
K_BACKSLASH_ = pygame.K_BACKSLASH
K_BACKSPACE_ = pygame.K_BACKSPACE
K_BREAK_ = pygame.K_BREAK
K_CAPSLOCK_ = pygame.K_CAPSLOCK
K_CARET_ = pygame.K_CARET
K_CLEAR_ = pygame.K_CLEAR
K_COLON_ = pygame.K_COLON
K_COMMA_ = pygame.K_COMMA
K_CURRENCYSUBUNIT_ = pygame.K_CURRENCYSUBUNIT
K_CURRENCYUNIT_ = pygame.K_CURRENCYUNIT
K_DELETE_ = pygame.K_DELETE
K_DOLLAR_ = pygame.K_DOLLAR
K_DOWN_ = pygame.K_DOWN
K_END_ = pygame.K_END
K_EQUALS_ = pygame.K_EQUALS
K_ESCAPE_ = pygame.K_ESCAPE
K_EURO_ = pygame.K_EURO
K_EXCLAIM_ = pygame.K_EXCLAIM
K_F1_ = pygame.K_F1
K_F10_ = pygame.K_F10
K_F11_ = pygame.K_F11
K_F12_ = pygame.K_F12
K_F13_ = pygame.K_F13
K_F14_ = pygame.K_F14
K_F15_ = pygame.K_F15
K_F2_ = pygame.K_F2
K_F3_ = pygame.K_F3
K_F4_ = pygame.K_F4
K_F5_ = pygame.K_F5
K_F6_ = pygame.K_F6
K_F7_ = pygame.K_F7
K_F8_ = pygame.K_F8
K_F9_ = pygame.K_F9
K_GREATER_ = pygame.K_GREATER
K_HASH_ = pygame.K_HASH
K_HELP_ = pygame.K_HELP
K_HOME_ = pygame.K_HOME
K_INSERT_ = pygame.K_INSERT
K_KP0_ = pygame.K_KP0
K_KP1_ = pygame.K_KP1
K_KP2_ = pygame.K_KP2
K_KP3_ = pygame.K_KP3
K_KP4_ = pygame.K_KP4
K_KP5_ = pygame.K_KP5
K_KP6_ = pygame.K_KP6
K_KP7_ = pygame.K_KP7
K_KP8_ = pygame.K_KP8
K_KP9_ = pygame.K_KP9
K_KP_0_ = pygame.K_KP_0
K_KP_1_ = pygame.K_KP_1
K_KP_2_ = pygame.K_KP_2
K_KP_3_ = pygame.K_KP_3
K_KP_4_ = pygame.K_KP_4
K_KP_5_ = pygame.K_KP_5
K_KP_6_ = pygame.K_KP_6
K_KP_7_ = pygame.K_KP_7
K_KP_8_ = pygame.K_KP_8
K_KP_9_ = pygame.K_KP_9
K_KP_DIVIDE_ = pygame.K_KP_DIVIDE
K_KP_ENTER_ = pygame.K_KP_ENTER
K_KP_EQUALS_ = pygame.K_KP_EQUALS
K_KP_MINUS_ = pygame.K_KP_MINUS
K_KP_MULTIPLY_ = pygame.K_KP_MULTIPLY
K_KP_PERIOD_ = pygame.K_KP_PERIOD
K_KP_PLUS_ = pygame.K_KP_PLUS
K_LALT_ = pygame.K_LALT
K_LCTRL_ = pygame.K_LCTRL
K_LEFT_ = pygame.K_LEFT
K_LEFTBRACKET_ = pygame.K_LEFTBRACKET
K_LEFTPAREN_ = pygame.K_LEFTPAREN
K_LESS_ = pygame.K_LESS
K_LGUI_ = pygame.K_LGUI
K_LMETA_ = pygame.K_LMETA
K_LSHIFT_ = pygame.K_LSHIFT
K_LSUPER_ = pygame.K_LSUPER
K_MENU_ = pygame.K_MENU
K_MINUS_ = pygame.K_MINUS
K_MODE_ = pygame.K_MODE
K_NUMLOCK_ = pygame.K_NUMLOCK
K_NUMLOCKCLEAR_ = pygame.K_NUMLOCKCLEAR
K_PAGEDOWN_ = pygame.K_PAGEDOWN
K_PAGEUP_ = pygame.K_PAGEUP
K_PAUSE_ = pygame.K_PAUSE
K_PERCENT_ = pygame.K_PERCENT
K_PERIOD_ = pygame.K_PERIOD
K_PLUS_ = pygame.K_PLUS
K_POWER_ = pygame.K_POWER
K_PRINT_ = pygame.K_PRINT
K_PRINTSCREEN_ = pygame.K_PRINTSCREEN
K_QUESTION_ = pygame.K_QUESTION
K_QUOTE_ = pygame.K_QUOTE
K_QUOTEDBL_ = pygame.K_QUOTEDBL
K_RALT_ = pygame.K_RALT
K_RCTRL_ = pygame.K_RCTRL
K_RETURN_ = pygame.K_RETURN
K_RGUI_ = pygame.K_RGUI
K_RIGHT_ = pygame.K_RIGHT
K_RIGHTBRACKET_ = pygame.K_RIGHTBRACKET
K_RIGHTPAREN_ = pygame.K_RIGHTPAREN
K_RMETA_ = pygame.K_RMETA
K_RSHIFT_ = pygame.K_RSHIFT
K_RSUPER_ = pygame.K_RSUPER
K_SCROLLLOCK_ = pygame.K_SCROLLLOCK
K_SCROLLOCK_ = pygame.K_SCROLLOCK
K_SEMICOLON_ = pygame.K_SEMICOLON
K_SLASH_ = pygame.K_SLASH
K_SPACE_ = pygame.K_SPACE
K_SYSREQ_ = pygame.K_SYSREQ
K_TAB_ = pygame.K_TAB
K_UNDERSCORE_ = pygame.K_UNDERSCORE
K_UNKNOWN_ = pygame.K_UNKNOWN
K_UP_ = pygame.K_UP
LIL_ENDIAN_ = pygame.LIL_ENDIAN
MIDIIN_ = pygame.MIDIIN
MIDIOUT_ = pygame.MIDIOUT
MOUSEBUTTONDOWN_ = pygame.MOUSEBUTTONDOWN
MOUSEBUTTONUP_ = pygame.MOUSEBUTTONUP
MOUSEMOTION_ = pygame.MOUSEMOTION
MOUSEWHEEL_ = pygame.MOUSEWHEEL
MULTIGESTURE_ = pygame.MULTIGESTURE
NOEVENT_ = pygame.NOEVENT
NOFRAME_ = pygame.NOFRAME
NUMEVENTS_ = pygame.NUMEVENTS
OPENGL_ = pygame.OPENGL
OPENGLBLIT_ = pygame.OPENGLBLIT
PREALLOC_ = pygame.PREALLOC
QUIT_ = pygame.QUIT
RESIZABLE_ = pygame.RESIZABLE
RLEACCEL_ = pygame.RLEACCEL
RLEACCELOK_ = pygame.RLEACCELOK
SCALED_ = pygame.SCALED
SCRAP_BMP_ = pygame.SCRAP_BMP
SCRAP_CLIPBOARD_ = pygame.SCRAP_CLIPBOARD
SCRAP_PBM_ = pygame.SCRAP_PBM
SCRAP_PPM_ = pygame.SCRAP_PPM
SCRAP_SELECTION_ = pygame.SCRAP_SELECTION
SCRAP_TEXT_ = pygame.SCRAP_TEXT
SHOWN_ = pygame.SHOWN
SRCALPHA_ = pygame.SRCALPHA
SRCCOLORKEY_ = pygame.SRCCOLORKEY
SWSURFACE_ = pygame.SWSURFACE
SYSTEM_CURSOR_ARROW_ = pygame.SYSTEM_CURSOR_ARROW
SYSTEM_CURSOR_CROSSHAIR_ = pygame.SYSTEM_CURSOR_CROSSHAIR
SYSTEM_CURSOR_HAND_ = pygame.SYSTEM_CURSOR_HAND
SYSTEM_CURSOR_IBEAM_ = pygame.SYSTEM_CURSOR_IBEAM
SYSTEM_CURSOR_NO_ = pygame.SYSTEM_CURSOR_NO
SYSTEM_CURSOR_SIZEALL_ = pygame.SYSTEM_CURSOR_SIZEALL
SYSTEM_CURSOR_SIZENESW_ = pygame.SYSTEM_CURSOR_SIZENESW
SYSTEM_CURSOR_SIZENS_ = pygame.SYSTEM_CURSOR_SIZENS
SYSTEM_CURSOR_SIZENWSE_ = pygame.SYSTEM_CURSOR_SIZENWSE
SYSTEM_CURSOR_SIZEWE_ = pygame.SYSTEM_CURSOR_SIZEWE
SYSTEM_CURSOR_WAIT_ = pygame.SYSTEM_CURSOR_WAIT
SYSTEM_CURSOR_WAITARROW_ = pygame.SYSTEM_CURSOR_WAITARROW
SYSWMEVENT_ = pygame.SYSWMEVENT
TEXTEDITING_ = pygame.TEXTEDITING
TEXTINPUT_ = pygame.TEXTINPUT
TIMER_RESOLUTION_ = pygame.TIMER_RESOLUTION
USEREVENT_ = pygame.USEREVENT
USEREVENT_DROPFILE_ = pygame.USEREVENT_DROPFILE
VIDEOEXPOSE_ = pygame.VIDEOEXPOSE
VIDEORESIZE_ = pygame.VIDEORESIZE
WINDOWSHOWN_ = pygame.WINDOWSHOWN
WINDOWHIDDEN_ = pygame.WINDOWHIDDEN
WINDOWEXPOSED_ = pygame.WINDOWEXPOSED
WINDOWMOVED_ = pygame.WINDOWMOVED
WINDOWRESIZED_ = pygame.WINDOWRESIZED
WINDOWSIZECHANGED_ = pygame.WINDOWSIZECHANGED
WINDOWMINIMIZED_ = pygame.WINDOWMINIMIZED
WINDOWMAXIMIZED_ = pygame.WINDOWMAXIMIZED
WINDOWRESTORED_ = pygame.WINDOWRESTORED
WINDOWENTER_ = pygame.WINDOWENTER
WINDOWLEAVE_ = pygame.WINDOWLEAVE
WINDOWFOCUSGAINED_ = pygame.WINDOWFOCUSGAINED
WINDOWFOCUSLOST_ = pygame.WINDOWFOCUSLOST
WINDOWCLOSE_ = pygame.WINDOWCLOSE
WINDOWTAKEFOCUS_ = pygame.WINDOWTAKEFOCUS
WINDOWHITTEST_ = pygame.WINDOWHITTEST

minWindowSizeAllowed = True
autoResizeWhen00 = True
allowMoreWindows = False

inWindow = True

clockTick = time.Clock()

print(f"{Fore.YELLOW}WELCOME TO")
print(f"{Fore.WHITE}PyKui {version_}")
print(f"{Fore.YELLOW}Web: https://metropolittanapple.github.io/pykuiframework/")
print(f"©2023{Fore.RESET}")

def warn(message):
    ### Shows a warning in light red

    print(Fore.LIGHTRED_EX + "WARN:", message)
    print(Fore.RESET + "")

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
    def title(title = f"PyKui {version_} window"):
        ### Creates a title for the window that you created

        if (title == ""):
            title = f"PyKuy {version_} window"

        display.set_caption(title)

    def WINDOW(title = f"PyKuy {version_} window", x = 500, y = 500, flags = RESIZABLE):
        ### Create a window

        global screen, windowsCreated, windowX, windowY

        windowsCreated += 1

        if (windowsCreated == 1 or allowMoreWindows):
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

        setIcon(PyKuiIcon)

        return pygame.display.set_mode((windowX, windowY), flags)

class open:
    def openSysFont(fontName, size):
        ### Open a system font

        return pygame.font.SysFont(fontName, size)

    def openFont(fontName, size):
        ### Open a custom font

        return pygame.font.Font(fontName, size)

def saveSysText(font = pygame.font.SysFont, text = "None", goodQuality = True, r = 0, g = 0, b = 0):
    ### You can save text in a variable an then you can manualy blit it

    return font.render(text, goodQuality, (r, g, b))

def saveText(font = pygame.font.Font, text = "None", goodQuality = True, r = 0, g = 0, b = 0):
    ### You can save text in a variable an then you can manualy blit it

    return font.render(text, goodQuality, (r, g, b))

def printw(windowSurface = pygame.Surface, font = pygame.font.SysFont, text = "None", goodQuality = True, r = 0, g = 0, b = 0, x = 0, y = 0):
    ### Prints text in the screen

    global printwText

    text = str(text)

    printwText = font.render(text, goodQuality, (r, g, b))
    
    blit(windowSurface, printwText, x, y)

pygame.key.get_pressed()

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

        global minWindowSizeAllowed, autoResizeWhen00, allowMoreWindows, autoFLimit

        try:
            rulesArg1.append(str(arg1))
            rulesArg2.append(str(arg2))

            if (arg1 == "min window size" or arg1 == "mws1" or arg1 == "minimum window size"):
                minWindowSizeAllowed = bool(arg2)

            elif (arg1 == "auto resize when 00" or arg1 == "arw001"):
                autoResizeWhen00 = bool(arg2)

            elif (arg1 == "allow more windows" or arg1 == "amw1"):
                allowMoreWindows = bool(arg2)

            elif (arg1 == "auto tick"):
                autoFLimit = bool(arg2)
            
            else:
                print(Fore.RED + "Unknown command for arg1")

                rule.removeList()

        except Exception as E:
            print(Fore.RED + "ERROR:", E)

        print(Fore.RESET + "")

def blit(windowSurface = pygame.Surface, surface = pygame.Surface, x = 0, y = 0):
    ### Shows (blits) image (surface) in windowSurface in given x and y coordinates

    if (x >= 0 - surface.get_size()[0] and x <= 0 + windowX and y >= 0 - surface.get_size()[1] and y <= 0 + windowY):
        windowSurface.blit(surface, (x, y))
    
def smoothScaledBlit(windowSurface = pygame.Surface, surface = pygame.Surface, x = 0, y = 0, w = 0, h = 0):
    ### Shows (blits) image (surface) in windowSurface in given x and y coordinates and smooth resizes the image in the given w and h

    surface = pygame.transform.smoothscale(surface, size=(w, h))

    if (x >= 0 - surface.get_size()[0] and x <= 0 + windowX and y >= 0 - surface.get_size()[1] and y <= 0 + windowY):
        windowSurface.blit(surface, (x, y))
        
def scaledBlit(windowSurface = pygame.Surface, surface = pygame.Surface, x = 0, y = 0, w = 0, h = 0):
    ### Shows (blits) image (surface) in windowSurface in given x and y coordinates and resizes the image in the given w and h

    surface = pygame.transform.scale(surface, size=(w, h))
    
    if (x >= 0 - surface.get_size()[0] and x <= 0 + windowX and y >= 0 - surface.get_size()[1] and y <= 0 + windowY):
        windowSurface.blit(surface, (x, y))

def smoothScale(surface = pygame.Surface, w = 0, h = 0):
    ### Smooths scales a surface

    surface = pygame.transform.smoothscale(surface, size=(w, h))

def scale(surface = pygame.Surface, w = 0, h = 0):
    ### Scales a surface

    surface = pygame.transform.scale(surface, size=(w, h))

def flipImage(sprite = pygame.Surface, x = True, y = False):
    ### Flip a image 

    return pygame.transform.flip(sprite, x, y).convert_alpha()

class frameRate:
    def limit(FPS):
        ### Sets frame rate

        global defaultFPS, frameRateSet

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

        else:
            pygame.mouse.set_visible(False)

    def setCursor(windowSurface = pygame.Surface, cursorImage = pygame.Surface, size = 25):
        ### Change the cursor image

        cursor.showCursor(False)
        cursor.getxy()

        if (cursorImage == "rect"):
            draw.rect(windowSurface, 255, 0, 0, mx, my, size, size)

        else:
            blit(windowSurface, cursorImage, mx, my, size, size)

class get:
    def windowW(windowSurface = pygame.Surface):
        ### Gets the window width

        return windowSurface.get_size()[0]

    def windowH(windowSurface = pygame.Surface):
        ### Gets the window height

        return windowSurface.get_size()[1]

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
        windowSurface.fill((r, g, b))

    for event in getEvent():
        if (event.type == QUIT):
            end(0)
          
print("Done!")
