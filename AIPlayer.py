import random
from uiutil import DIRECTION, COLLISION


class AIPlayer(object):
    _init_flag = False

    def __init__(self, tank=None, home=None):
        if not self._init_flag:
            self._init_flag = True
            self.__control_tank = tank
            self.__home = home
            self.scene_elements = None
            self.player_group = None
            self.enemy_group = None

    # 实现单例模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(AIPlayer, "_instance"):
            AIPlayer._instance = object.__new__(cls)
        return AIPlayer._instance

    def strategy(self):
        # if (self.__control_tank.rect.centerx <= self.__home.rect.top or
        #     self.__control_tank.rect.centerx >= self.__home.rect.bottom) and (
        #         self.__control_tank.direction == DIRECTION.RIGHT or
        #         self.__control_tank.direction == DIRECTION.LEFT):
        #     return False
        return True

    @property
    def control_tank(self):
        return self.__control_tank

    @control_tank.setter
    def control_tank(self, tank):
        self.__control_tank = tank

    def update_group(self, scene_elements, player_group, enemy_group):
        self.scene_elements = scene_elements
        self.player_group = player_group
        self.enemy_group = enemy_group

    def change_direction(self, current_direction=False):
        direction_list = DIRECTION.list()
        if current_direction:
            direction_list.remove(self.__control_tank.direction)
        self.__control_tank.update_direction(random.choice(direction_list))

    def control_tank_move(self):
        direction = DIRECTION.UP
        collision = self.__control_tank.move(direction, self.scene_elements,
                                             self.player_group, self.enemy_group, self.__home)
        print(collision)
        if collision is None or collision == 0:
            return
        # change_direction = False
        # if collision & COLLISION.WITH_SCENE_ELEMENTS & COLLISION.WITH_BORDER & COLLISION.WITH_HOME:
        #     change_direction = True
        # self.change_direction(change_direction)

    def control_tank_shoot(self):
        if self.strategy():
            self.__control_tank.shoot()
