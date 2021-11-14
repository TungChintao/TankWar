from sprites.tank import Tank
from uiutil import DIRECTION


class PlayerTank(Tank):
    def __init__(self, name, position, config):
        super().__init__(config=config)
        # print(self.config.TANK_IMAGE.get(name))
        self.name = name
        self.load_tank_image(self.config.TANK_IMAGE.get(name))
        self.init_direction = DIRECTION.UP
        self.init_position = position
        self.life = 3
        self.__reborn()

    def _load_resources(self):
        super()._load_resources()

    def update(self):
        if self.boom_flag:
            self.boom_count += 1
            if self.boom_count > self.boom_time:
                self.boom_count = 0
                self.boom_flag = False
                self.__reborn()

    def decrease_life(self):
        if self.boom_flag:
            return False
        self.boom_flag = True
        self.life -= 1
        return True

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def __reborn(self):
        print(self.life)
        self._update_direction(self.init_direction)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.init_position




    #
    # def __reborn(self):
    #     self._tank_image =