import PyKui as pyKui

pyKui.sdrawer.init()

window = pyKui.create.WINDOW("Sdrawing test", 800, 800)

def main():
    pyKui.sdrawer.goto(800 / 2 - 25, 10)
    pyKui.sdrawer.square(window, 255, 255, 255, 50, 10)
    pyKui.sdrawer.goto(800 / 2, 10)
    pyKui.sdrawer.glide(window, 255, 255, 255, 10, 800 / 2, 200)
    pyKui.sdrawer.glide(window, 255, 255, 255, 10, 800 / 2 - 25 * 2, 215 + 15)
    pyKui.sdrawer.glide(window, 255, 255, 255, 10, 800 / 2 - 25 * 2, 215 + 15)
    pyKui.sdrawer.goto(800 / 2, 10)
    pyKui.sdrawer.glide(window, 255, 255, 255, 10, 800 / 2, 200)
    pyKui.sdrawer.glide(window, 255, 255, 255, 10, 800 / 2 + 25 * 2, 215 + 15)
    pyKui.sdrawer.goto(800 / 2, 125)
    pyKui.sdrawer.glide(window, 255, 255, 255, 10, 800 / 2 + 25 * 2, 100 - 25 * 2)
    pyKui.sdrawer.goto(800 / 2, 125)
    pyKui.sdrawer.glide(window, 255, 255, 255, 10, 800 / 2 - 25 * 2, 100 - 25 * 2)
    pyKui.sdrawer.showPointer(window, False)

pyKui.frameRate.limit(5)

while 1:
    pyKui.simpleUpdate()
    main()

    pyKui.frameRate.tick()
