import pygame
import config
from view.ViewManager import ViewManager


class GameCtrl:
    def __init__(self):
        # 视图层---------------------------
        self.viewManager = ViewManager()

        # 游戏判断标志-------------------------
        self.level = 0
        self.lose_game = False
        self.exit_game = False

        # 开始游戏------------------------------
        self.start()

    def up_level(self):
        self.level += 1

    def reset_level(self):
        self.level = 0

    def load_scene(self):
        pass

    def load_music(self):
        pass

    def load_level(self):
        pass

    def game_loop(self):
        pass

    def init_game(self):
        pygame.init()
        pygame.display.set_caption(config.TITLE)
        pygame.display.set_mode(config.SCREEN_WIDTH,config.SCREEN_HEIGHT )
        self.load_music()
        self.load_level()

    def start(self):
        self.init_game()
        self.game_loop()

