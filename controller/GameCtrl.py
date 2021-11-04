import os
import pygame


class GameCtrl(object):

    _init_flag = False

    def __init__(self, config=None):
        if not self._init_flag:
            if not config:
                raise Exception('Config Error!')

            self._init_flag = True

            # 初始配置---------------------------
            self.level = 0
            self.screen = None
            self.config = config

            # 游戏判断标志-------------------------
            self.lose_game = False
            self.exit_game = False

            # 开始游戏------------------------------
            # self.start()

    # 实现单例模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(GameCtrl, "_instance"):
            GameCtrl._instance = object.__new__(cls)
        return GameCtrl._instance

    def up_level(self):
        self.level += 1

    def reset_level(self):
        self.level = 0

    def load_screen(self, size=None):
        if size is None:
            self.screen = pygame.display.set_mode((self.config.SCREEN_WIDTH, self.config.SCREEN_HEIGHT))
        else:
            self.screen = pygame.display.set_mode(size)

    def load_music(self):
        pass

    def load_level(self):
        pass

    def game_loop(self):
        from scene.SceneManager import SceneManager
        SceneManager().show('GameStart')
        while True:
            print('ok')
            # self.viewManager.show('UPLevelView')
            # self.viewManager.show('GameLevelView')
            # if self.lose_game:
            #     self.viewManager.show('GameOverView')
            #     self.reset_level()
            # else:
            #     self.up_level()
            # if self.exit_game:
            #     break

    def init_game(self):
        pygame.init()
        pygame.display.set_caption(self.config.TITLE)
        self.load_screen()
        self.load_music()
        self.load_level()

    def start(self):
        self.init_game()
        self.game_loop()

