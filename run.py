import config
from manager.GameManager import GameManager

if __name__ == '__main__':
    gamectrl = GameManager(config)
    gamectrl.start()
