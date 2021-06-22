"""
The main method of the program: opens pygame window and has main loop.
"""
import pygame.locals
import EditWindow
from functions import *
from tkinter import Tk
from tkinter import messagebox as mb


def main():
    """
    main method - runs the window displayed.
    """
    WIN = pygame.display.set_mode((WIDTH, WIDTH), pygame.locals.DOUBLEBUF, 24)
    pygame.display.set_caption("Algorithm Comparison")
    grid = make_grid(ROWS, WIDTH)

    start = None
    end = None
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

                if event.key == pygame.K_SPACE and start and end:
                    make_grid_keep_edits(ROWS, grid)
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    d_commands, d_found = dijkstra(None, grid, start, end)
                    b_commands, b_found = bellmanford(lambda: draw(WIN, grid, ROWS, WIDTH), grid, start, end)
                    pygame.display.set_caption("Algorithm Comparison")
                    if d_found:
                        d_string = f'Dijkstra\'s algorithm took {d_commands} commands to find the path.'
                    else:
                        d_string = f'Dijkstra\'s algorithm did not find a shortest path after {d_commands} commands.'

                    if b_found:
                        b_string = f'Bellman-Ford\'s algorithm took {b_commands} commands to find the path.'
                    else:
                        b_string = f'Bellman-Ford\'s algorithm did not find a shortest path after {b_commands} ' \
                                   'commands.'
                    root = Tk()
                    root.withdraw()
                    mb.showinfo('Algorithm Comparison', d_string + '\n' + b_string)
                    root.destroy()

                if event.key == pygame.K_r:
                    start = None
                    end = None
                    grid = make_grid(ROWS, WIDTH)

                if event.key == pygame.K_e:
                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(pos, ROWS, WIDTH)
                    node = grid[row][col]
                    weight_list = EditWindow.main()
                    node.make_edit(weight_list)

                if event.key == pygame.K_b:
                    grid = make_grid_keep_edits(ROWS, grid)

    pygame.quit()


if __name__ == '__main__':
    main()
