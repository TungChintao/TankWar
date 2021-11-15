from src import config
from src.manager.GameManager import GameManager

if __name__ == '__main__':
    # print(config.AUDIO.items())
    gamectrl = GameManager(config)
    gamectrl.start()
