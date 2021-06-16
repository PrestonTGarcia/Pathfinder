"""
External functions used to make, draw, and find positions on grid.
"""
from Node import Node
from constants import *
import pygame
from queue import PriorityQueue


def find_dist(p1, p2):
    """
    Finds the distance given two positions/points.
    :param p1: The starting point.
    :param p2: The destination point
    :return: The distance of nodes between the two points
    """
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def make_grid(rows, width):
    """
    Makes the grid/list of nodes.
    :param rows: The amount of rows.
    :param width: The width of the window.
    :return: The grid/list of nodes.
    """
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return grid

def make_grid_leave_barrier(rows, width, oldgrid):
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = oldgrid[i][j]
            if not oldgrid[i][j].is_barrier() and not oldgrid[i][j].is_start() and not oldgrid[i][j].is_end():
                node.reset()
            grid[i].append(node)
    return grid

def draw_grid(win, rows, width):
    """
    Draws the gridlines on the window.
    :param win: The window being drawn on.
    :param rows: The amount of rows to be drawn.
    :param width: The width of the window.
    """
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, OPEN_COLOR, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, OPEN_COLOR, (j * gap, 0), (j * gap, width))



def draw(win, grid, rows, width):
    """
    Draws the rectangles/nodes.
    :param win: The window being drawn on.
    :param grid: The list/grid of nodes.
    :param rows: The amount of rows in the grid.
    :param width: The width of the window.
    """
    win.fill(NODE_COLOR)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    """
    Converts the position of a click to a row and a column.
    :param pos: The mouse clicked position.
    :param rows: The amount of rows of nodes in the window.
    :param width: The width of the window.
    :rtype: int, int
    :return: The row and column clicked on.
    """
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col


def reconstruct_path(came_from, current, draw_func):
    """
    Draws the path found from the algorithm.
    :param came_from: The list of nodes in the path.
    :param current: The current node being analyzed; the end node since this is only called when end is found.
    :param draw_func: The function used to draw.
    """
    while current in came_from:
        current = came_from[current]
        if current is not None:
            current.make_path()
        draw_func()

def dijkstra(draw_func, grid, start, end):
    """
    Dijkstra's algorithm implemented with pygame
    :param draw_func: The function used to draw and update the graph.
    :param grid: The grid/graph of nodes.
    :param start: The start node.
    :param end: The end node.
    :return: A boolean representing whether or not a path is possible between the two nodes.
    """
    dist = {node: float('inf') for row in grid for node in row}  # Sets dist of each node to infinity
    previous = {node: None for row in grid for node in row}  # Sets previous of each node to None
    dist[start] = 0
    node_queue = dist.copy()

    while node_queue:  # Checks if the queue is empty

        for event in pygame.event.get():

            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                # If user wants to quit the algorithm midway through the visualization
                pygame.quit()

        current = min(node_queue, key=node_queue.get)

        if dist[current] == float('inf'):  # If the minimum distance is infinity
            break

        del node_queue[current]  # Removes the minimum current from the set

        if current == end:  # If we reached the end
            reconstruct_path(previous, current, draw_func)
            # Recolors start and end to avoid loss of start and end positions
            start.make_start()
            end.make_end()
            return True

        for neighbor in current.neighbors:
            alt = dist[current] + 1  # Adds distance of current to the distance between neighbors
            # Change in the future to find dist between current and neighbor when adding edge weights
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                node_queue[neighbor] = alt
                previous[neighbor] = current
                if not (neighbor.is_start() or neighbor.is_end()):
                    neighbor.make_open()

            elif current != start and current != end:  # Closes unneeded nodes
                current.make_closed()

        draw_func()

    return False
