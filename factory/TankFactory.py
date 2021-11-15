from sprites.EnemyTank import EnemyTank
from sprites.PlayerTank import PlayerTank
from sprites.AutoPlayerTank import AutoPlayerTank
from manager.GameManager import GameManager
from uiutil import AutoName


class TankFactory(object):
    ENEMY_TANK = 0
    PLAYER1_TANK = 1
    PLAYER2_TANK = 2

    def __init__(self, config):
        self.config = config

    def create_tank(self, position, tank_type, name=None):
        if tank_type == TankFactory.ENEMY_TANK:
            return EnemyTank(position=position, config=self.config)
        elif tank_type == TankFactory.PLAYER1_TANK:
            tank = PlayerTank(name='player1', position=position, config=self.config)
            tank.set_nickname(GameManager().player_name)
            return tank
        elif tank_type == TankFactory.PLAYER2_TANK:
            tank = AutoPlayerTank(name='player2', position=position, config=self.config)
            tank.set_nickname(AutoName.random())
            return tank