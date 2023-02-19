# All variables used by the library

from pyKui_Alt_F4_studios.imports import *

print("Loading variables")

PyKuiIcon = pygame.image.load("pyKui_Alt_F4_studios/.rsrc/images/icon/icon v1.png")

key = pygame.key.get_pressed
getEvent = pygame.event.get

version_ = "1.0.1"

noDrawerInitErrorMessage = "Do pyKui.sdrawer.init() to initalize the simple drawing functions"
noCDrawerInitErrorMessage = "Do pyKui.drawer.init() to initalize the simple drawing functions"
audioNotInitErrorMessage = "Audio is not inited, do 'pyKui.audio.init()'"

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
initedAudio = False
autoFLimit = True
fpsLimit = True

isPenUp = True

register_quit = pygame.register_quit
set_error = pygame.set_error

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
mixer = pygame.mixer
math = pygame.math
mask = pygame.mask
fastevent = pygame.fastevent
event = pygame.event
error = pygame.error
Rect_ = pygame.Rect

minWindowSizeAllowed = True
autoResizeWhen00 = True
allowMoreWindows = False

inWindow = True

clockTick = time.Clock()
