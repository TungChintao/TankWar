import pygame
from sprites.bullet import Bullet

from uiutil import DIRECTION, COLLISION


class Tank(pygame.sprite.Sprite):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.tank_image = None

        self.speed = 8
        self.switch_flag = False

        self.bullet_cooling = False
        self.bullet_cooling_time = 20
        self.boom_flag = False

        self.border_len = config.BORDER_LEN
        self.screen_size = [config.SCREEN_WIDTH, config.SCREEN_HEIGHT]
        self._load_resources()

    @property
    def image(self):
        if self.boom_flag:
            return self.boom_image
        return self.tank_direction_image.subsurface((48*int(self.switch_flag), 0), (48,48))

    def load_tank_image(self, image):
        self.tank_image = pygame.image.load(image).convert_alpha()

    def _load_resources(self):
        self.bullet_image = self.config.BULLET_IMAGE
        self.boom_image = pygame.image.load(self.config.IMAGE.get('boom_static'))

    def _update_direction(self, direction):
        self.direction = direction
        if self.direction == DIRECTION.UP:
            self.tank_direction_image = self.tank_image.subsurface((0, 0), (96, 48))
        elif self.direction == DIRECTION.DOWN:
            self.tank_direction_image = self.tank_image.subsurface((0, 48), (96, 48))
        elif self.direction == DIRECTION.LEFT:
            self.tank_direction_image = self.tank_image.subsurface((0, 96), (96, 48))
        elif self.direction == DIRECTION.RIGHT:
            self.tank_direction_image = self.tank_image.subsurface((0, 144), (96, 48))

    def move(self, direction):
        if self.boom_flag:
            return
        if self.direction != direction:
            self._update_direction(direction)

        new_position = (self.direction.value[0] * self.speed, self.direction.value[1]*self.speed)
        old_rect = self.rect
        self.rect = self.rect.move(new_position)

    def shoot(self):
        print(self.boom_flag, self.bullet_cooling)
        if self.boom_flag:
            return False
        if not self.bullet_cooling:
            self.bullet_cooling = True
            position = (self.rect.centerx + self.direction.value[0], self.rect.centery + self.direction.value[1])
            bullet = Bullet(direction=self.direction, position=position,tank=self,config=self.config)
            return bullet
        return False









