import os
import random
import pygame


class GameManager(object):

    _init_flag = False

    def __init__(self, config=None):
        if not self._init_flag:
            if not config:
                raise Exception('Config Error!')

            self._init_flag = True

            # 初始配置---------------------------
            self.config = config
            self.level = 0
            self.music = {}
            self.final = None
            self.levels = None
            self.screen = None
            self.double_mode = False

            # 游戏判断标志-------------------------
            self.win_game = False
            self.exit_game = False

            # 开始游戏------------------------------
            # self.start()

    # 实现单例模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(GameManager, "_instance"):
            GameManager._instance = object.__new__(cls)
        return GameManager._instance

    @property
    def game_file(self):

        weights = [1]*len(self.levels)
        if self.final is not None:
            weights[self.final]  = 0

        self.final = random.choices(range(len(self.levels)), weights=weights)[0]
        return self.levels[self.final]

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
        for music, file in self.config.AUDIO.items():
            pass

    def load_levels(self):
        self.levels = [
            os.path.join(self.config.LEVEL, filename)
            for filename in sorted(os.listdir(self.config.LEVEL))
        ]

    def game_loop(self):
        from manager.SceneManager import SceneManager
        SceneManager().show('GameStart')
        while True:
            # self.viewManager.show('UPLevelView')
            SceneManager().show('GameRun')
            if self.win_game:
                SceneManager().show('GameOver')
                self.reset_level()
            else:
                self.up_level()
            if self.exit_game:
                break

    def init_game(self):
        pygame.init()
        pygame.display.set_caption(self.config.TITLE)
        self.load_screen()
        self.load_music()
        self.load_levels()

    def start(self):
        self.init_game()
        self.game_loop()

