"""
The main method of the program: opens pygame window and has main loop.
"""
import pygame.locals

from functions import *


def main():
    """
    :return:
    """
    WIN = pygame.display.set_mode((WIDTH, WIDTH), pygame.locals.DOUBLEBUF, 24)
    pygame.display.set_caption("Algorithm Comparison")
    grid = make_grid(ROWS, WIDTH)

    start = None
    end = None
    need_reset = False
    run = True

    while run:

        draw(WIN, grid, ROWS, WIDTH)

        for event in pygame.event.get():

            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                run = False

            if pygame.mouse.get_pressed(3)[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)
                node = grid[row][col]

                if not start and node != end:
                    start = node
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()

                elif node != start and node != end:
                    node.make_barrier()

            elif pygame.mouse.get_pressed(3)[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)
                node = grid[row][col]

                if node == start:
                    start = None

                if node == end:
                    end = None

                node.reset()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE and start and end and not need_reset:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    dijkstra(lambda: draw(WIN, grid, ROWS, WIDTH), grid, start, end)
                    need_reset = True

                if event.key == pygame.K_r:
                    start = None
                    end = None
                    grid = make_grid(ROWS, WIDTH)
                    need_reset = False

    pygame.quit()


if __name__ == '__main__':
    main()
