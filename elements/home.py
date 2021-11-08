import pygame
from elements.SceneElements import SceneElement


class Home(SceneElement):
    def __init__(self, position, image, protection_position):
        super().__init__(position, image[0])
        self.__destroyed = False
        self.destroyed_image = image[1]
        self.protection_position = protection_position

    @property
    def destroyed(self):
        return self.__destroyed

    @destroyed.setter
    def destroyed(self, destroyed):
        self.__destroyed = destroyed
        if destroyed:
            self.image = pygame.image.load(self.destroyed_image)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

