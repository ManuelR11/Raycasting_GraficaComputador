import pygame as pg

RES = WIDTH, HEIGHT = 1600, 900

HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
TEXTURE_SIZE = 256
FLOOR_COLOR = (0, 0, 0)
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('texturas/Cielo_1.png', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0

    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.0 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return{
            1: self.get_texture('texturas/Pared_1.png'),
            2: self.get_texture('texturas/Pared_2.png'),
            3: self.get_texture('texturas/Pared_3.png'),
            4: self.get_texture('texturas/Pared_4.png'),
            5: self.get_texture('texturas/Pared_1.png'),
        }
