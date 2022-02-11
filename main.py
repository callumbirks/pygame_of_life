import getopt
import sys
from math import floor

import funcy
import pygame as pg

import engine


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h:")
        grid_size = int(opts[0][1]) if opts[0][0] == '-h' else 100
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
    clock = pg.time.Clock()

    sim_running = False
    alive_cells = frozenset()
    last_pos = -1
    sim_speed = 6

    while 1:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    sim_running = not sim_running
                elif event.key == pg.K_c:
                    alive_cells = frozenset()
                elif event.key == pg.K_UP:
                    sim_speed = sim_speed + 3
                elif event.key == pg.K_DOWN and sim_speed > 3:
                    sim_speed = sim_speed - 3

        if sim_running:
            clock.tick(sim_speed)
            alive_cells = engine.step(grid_size, alive_cells)
        else:
            left, middle, right = pg.mouse.get_pressed()
            if left:
                pos = funcy.walk(lambda p: floor(p / pixel_mult), pg.mouse.get_pos())
                pos = pos[1] * grid_size + pos[0]
                if (pos != last_pos):
                    last_pos = pos
                    alive_cells = alive_cells ^ frozenset({pos})

        cell_coords = funcy.map(lambda c: (c % grid_size, floor(c / grid_size)), alive_cells)
        background.fill((16, 16, 16))
        for cell in cell_coords:
            pg.draw.rect(background, (250, 250, 250),
                         (cell[0] * pixel_mult, cell[1] * pixel_mult, pixel_mult, pixel_mult))
        screen.blit(background, (0, 0))
        pg.display.flip()


if __name__ == '__main__':
    main(sys.argv[1:])
