import pygame

from scene.AbstractScene import AbstractScene
from controller.GameCtrl import GameCtrl


class GameRunScene(AbstractScene):
    def __init_resources(self):
        config = self.config
        self.sounds = GameCtrl().sounds
        self.images = config.IMAGE
        self.home = pygame.image.load(self.images.get('background'))
        self.font = pygame.font.Font(config.FONT, config.HEIGHT//35)
        self.grid_size = config.GRID_SIZE
        self.scene_factory = TankFactory(self.config)
        self.scene_elements = None
