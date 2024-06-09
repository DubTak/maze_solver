from graphics import *
from cell import *


def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell2 = Cell(win)
    cell2.has_bottom_wall = False
    cell1.draw(100, 100, 200, 200)
    cell2.draw(300, 300, 400, 400)
    win.wait_for_close()


main()
