import PyKui as pyKui

window = pyKui.create.WINDOW("Image test")

anImage = pyKui.imageLoad.load(".rsrc/images/tests/man.png")

mainFont = pyKui.open.openSysFont("Arial", 35)

px = 0
py = 0

def main():
    global px, py, anImage

    if (pyKui.key()[pyKui.K_LEFT]):
        px -= 7
        
    if (pyKui.key()[pyKui.K_RIGHT]):
        px += 7

    if (pyKui.key()[pyKui.K_DOWN]):
        py += 7

    if (pyKui.key()[pyKui.K_UP]):
        py -= 7

    pyKui.printw(window, mainFont, "Hello world", True, 255, 255, 255, 100, 200)
    pyKui.smoothScaledBlit(window, anImage, px, py, 50, 50)

pyKui.frameRate.limit(30)

while 1:
    pyKui.simpleUpdate(True, window, 0, 0, 0)
    main()
