"""
Node class
"""
from constants import *
import pygame


class Node:
    """
    Class Node that holds attributes and methods regarding nodes.
    """

    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = NODE_COLOR
        self.width = width
        self.total_rows = total_rows
        self.left_weight, self.right_weight, self.down_weight, self.up_weight = 1, 1, 1, 1
        self.neighbors = {}

    def get_pos(self):
        """
        Gets the position of the node.
        :return: The row and column of the current node instance.
        """
        return self.row, self.col

    def is_closed(self):
        """
        Checks whether or not the node instance is closed.
        :return: A boolean representing whether or not the color has been set to the closed color(black).
        """
        return self.color == CLOSED_COLOR

    def is_open(self):
        """
        Checks whether or not the node instance is open.
        :return: A boolean representing whether or not the color has been set to the open color(grey).
        """
        return self.color == OPEN_COLOR

    def is_barrier(self):
        """
        Checks whether or not the node instance is a barrier.
        :return: A boolean representing whether or not the color has been set to the barrier color(red).
        """
        return self.color == BARRIER_COLOR

    def is_start(self):
        """
        Checks whether or not the node instance is the start node.
        :return: A boolean representing whether or not the color has been set to the start color(green).
        """
        return self.color == START_COLOR

    def is_end(self):
        """
        Checks whether or not the node instance is the end node.
        :return: A boolean representing whether or not the color has been set to the end color(orange).
        """
        return self.color == END_COLOR

    def is_edited(self):
        """
        Checks whether or not the node instance is an edited node.
        :return: A boolean representing whether or not the color has been set to the edit color(blue).
        """
        return self.color == EDIT_COLOR

    def reset(self):
        """
        Sets the node's color to the original node color(white).
        """

        self.color = NODE_COLOR

    def make_start(self):
        """
        Sets the node's color to the start node color(green).
        """
        self.color = START_COLOR

    def make_closed(self):
        """
        Sets the node's color to the closed color(black).
        """
        self.color = CLOSED_COLOR

    def make_open(self):
        """
        Sets the node's color to the open color(grey).
        """
        self.color = OPEN_COLOR

    def make_barrier(self):
        """
        Sets the node's color to the barrier color(red).
        """
        self.color = BARRIER_COLOR

    def make_end(self):
        """
        Sets the node's color to the end color(orange).
        """
        self.color = END_COLOR

    def make_path(self):
        """
        Sets the node's color to the path color(turquoise).
        """
        self.color = PATH_COLOR

    def make_edit(self, weight_list):
        """
        Makes edits to nodes weights.
        :param weight_list:
        """
        self.color = EDIT_COLOR
        self.down_weight = weight_list[0]
        self.up_weight = weight_list[1]
        self.right_weight = weight_list[2]
        self.left_weight = weight_list[3]

    def draw(self, win):
        """
        Draws the node instance on the window.
        :param win: The window being drawn on.
        """
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        """
        Updates the neighbor list attribute.
        :param grid: The grid/list of nodes.
        """

        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # Down
            self.neighbors[grid[self.row + 1][self.col]] = self.down_weight

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # Up
            self.neighbors[grid[self.row - 1][self.col]] = self.up_weight

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # Right
            self.neighbors[grid[self.row][self.col + 1]] = self.right_weight

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # Left
            self.neighbors[grid[self.row][self.col - 1]] = self.left_weight
