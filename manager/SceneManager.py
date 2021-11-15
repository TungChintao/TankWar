from scene import *


class SceneManager(object):

    def __init__(self):
        self.__scenes = {
            'SetDifficulty': SetDifficultyScene(),
            'GameStart': GameStartScene(),
            'GameLoad': GameLoadScene(),
            'GameRun': GameRunScene(),
            'GameOver': GameOverScene(),
            'SetName': SetNameScene(),
        }

    def __new__(cls, *args, **kwargs):
        if not hasattr(SceneManager, "_instance"):
            SceneManager._instance = object.__new__(cls)
        return SceneManager._instance

    def show(self, scene):
        self.__scenes[scene].show()

