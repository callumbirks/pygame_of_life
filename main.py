import engine
import funcy
import pygame as pg
from math import floor
import sys, getopt


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h:")
        grid_size = args[0] if opts[0] == 'h' else 100
    except IndexError or getopt.GetoptError:
        print("usage: main.py -h <grid height>")
        sys.exit(1)

    pixel_mult = 8

    # pg setup
    pg.init()
    screen = pg.display.set_mode((pixel_mult * grid_size, pixel_mult * grid_size))
    pg.display.set_caption("pygame_of_life")
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((16, 16, 16))
    screen.blit(background, (0, 0))
    pg.display.flip()

    sim_running = False
    alive_cells = frozenset()
    last_pos = -1

    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        left, middle, right = pg.mouse.get_pressed()
        if left:
            pos = funcy.walk(lambda p: floor(p / pixel_mult), pg.mouse.get_pos())
            pos = pos[1] * grid_size + pos[0]
            if (pos != last_pos):
                last_pos = pos
                alive_cells = alive_cells ^ frozenset({pos})
        screen.blit(background, (0, 0))
        pg.display.flip()


if __name__ == '__main__':
    main(sys.argv[1:])
