import pygame as pg
import sys
import math

from Enviroment import *
from Point import *
from Raycasting import *
from Render import *

RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.show_start_screen_flag = True

        pg.mixer.init()
        pg.mixer.music.load('texturas/Musica.mp3') 
        pg.mixer.music.play(-1)

        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)

    def get_show_start_screen(self):
        return self.show_start_screen_flag

    def toggle_show_start_screen(self):
        self.show_start_screen_flag = not self.show_start_screen_flag

    def display_start_screen(self):
        self.screen.fill(BLACK)
        font = pg.font.SysFont("Rockwell", 50)
        text = font.render("Press space to start( )", True, WHITE)
        text_rect = text.get_rect(center=(HALF_WIDTH, HALF_HEIGHT + 200))
        font_1 = pg.font.SysFont("Rockwell", 400)
        text_1 = font_1.render("DOOM", True, WHITE)
        text_rect_1 = text_1.get_rect(center=(HALF_WIDTH, HALF_HEIGHT - 200))

        self.screen.blit(text, text_rect)
        self.screen.blit(text_1, text_rect_1)
        pg.display.flip()


    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.object_renderer.draw()
        self.map.draw()
        self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                elif event.key == pg.K_SPACE and self.get_show_start_screen():
                    self.toggle_show_start_screen()

    def run(self):
        self.display_start_screen()

        while True:
            self.check_events()
            if not self.get_show_start_screen(): 
                break

        while True: 
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
