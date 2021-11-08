from sprites.tank import Tank
from uiutil import DIRECTION


class PlayerTank(Tank):
    def __init__(self, name, position, config):
        super().__init__(config=config)
        print(self.config.TANK_IMAGE.get(name))
        self.load_tank_image(self.config.TANK_IMAGE.get(name))
        self.init_direction = DIRECTION.UP
        self.init_position = position
        self.life = 3
        self._update_direction(self.init_direction)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = self.init_position

    def _load_resources(self):
        super()._load_resources()



    def draw(self, screen):
        screen.blit(self.image, self.rect)




    #
    # def __reborn(self):
    #     self._tank_image =