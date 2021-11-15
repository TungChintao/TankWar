from sprites.tank import Tank
from uiutil import DIRECTION


class PlayerTank(Tank):
    def __init__(self, name, position, config):
        super().__init__(config=config)
        # print(self.config.TANK_IMAGE.get(name))
        self.name = name
        self.nick = None
        self.load_tank_image(self.config.TANK_IMAGE.get(name))
        self.init_direction = DIRECTION.UP
        self.init_position = position

        self.life = 3
        self._reborn()

    def set_nickname(self, nick):
        self.nick = nick
        if self.nick is None:
            self.nick = 'Lazy Boy'

    def _load_resources(self):
        super()._load_resources()

    def update(self):
        if self.bullet_cooling:
            self.bullet_cooling_count += 1
            if self.bullet_cooling_count >= self.bullet_time:
                self.bullet_cooling_count = 0
                self.bullet_cooling = False

        if self.boom_flag:
            self.boom_count += 1
            if self.boom_count > self.boom_time:
                self.boom_count = 0
                self.boom_flag = False
                self._reborn()

    def decrease_life(self):
        if self.boom_flag:
            return False
        self.boom_flag = True
        self.life -= 1
        return True

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def _reborn(self):
        # print(self.life)
        self.bullet_cooling = False
        self.bullet_time = 30
        self.bullet_cooling_count = 0
        self._update_direction(self.init_direction)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.init_position

