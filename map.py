import pygame as pg
import os
# 1 = walls 0 = empty space


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = []
        self.world_map = {}
        self.load_map()

    def load_map(self):

        map_file = os.path.join(os.path.dirname(__file__), 'map.txt')
        
        with open(map_file) as f:
            rows = f.readlines()
            
        self.mini_map = []
        for row in rows:
            nums = row.strip().split(',')
            map_row = []
            for num in nums:
                if num == "_":
                    map_row.append(False) 
                else:
                    map_row.append(int(num))
            self.mini_map.append(map_row)

        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    # draw every blank element as an unfilled square
    def draw(self):
        # Dibujar el mapa más pequeño
        map_width = 300  
        map_height = 300
        cell_size = 10
        for pos, value in self.world_map.items():
            if value: # Solo dibujar casillas con muros
                x, y = pos
                pg.draw.rect(self.game.screen, 'darkgray',  
                    (x * cell_size + 50, y * cell_size + 50, cell_size, cell_size))
