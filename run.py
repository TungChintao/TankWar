import config
from controller.GameCtrl import GameCtrl

if __name__ == '__main__':
    gamectrl = GameCtrl(config)
    gamectrl.start()
