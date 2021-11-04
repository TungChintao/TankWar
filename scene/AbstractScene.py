import sys
import pygame
from manager.GameManager import GameManager


class AbstractScene:
    def __init__(self):
        self._load_resources()
        self._load_logo()

    @property
    def config(self):
        return GameManager().config

    def _load_resources(self):
        pass

    def _load_logo(self):
        pass

    def _load_tips(self):
        pass

    def _load_bottons(self):
        pass

    def _game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self._draw_interface()
        pass

    def _draw_interface(self):
        pass

    def show(self):
        GameManager().load_screen()
        self._load_tips()
        self._load_bottons()
        self._game_loop()

