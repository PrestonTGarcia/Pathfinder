"""
Holds constants such as colors.
"""
ROWS = 50
WIDTH = 600
DRAW_FUNCS = [1, 0]  # 0th index is initially 1, due to dijkstra's being the preferred visualized algorithm.
COLORS = {'BARRIER': (255, 0, 0),
          'START': (0, 255, 0),
          'NODE': (255, 255, 255),
          'CLOSED': (0, 0, 0),
          'END': (255, 165, 0),
          'OPEN': (128, 128, 128),
          'PATH': (64, 224, 208),
          'EDIT': (0, 0, 255),
          'LINE': (64, 64, 64)}
