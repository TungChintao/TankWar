import pygame


class SceneElement(pygame.sprite.Sprite):

    def __init__(self, image, position, blit=False):
        super().__init__()
        self.image = pygame.image.load(image)
        if blit:
            self.image = pygame.Surface((24, 24))
            for i in range(2):
                for j in range(2):
                    self.image.blit(pygame.image.load(image), (12*i, 12*j))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position