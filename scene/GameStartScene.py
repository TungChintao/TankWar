import sys
import pygame
from manager.GameManager import GameManager
from scene.AbstractScene import AbstractScene


class GameStartScene(AbstractScene):

    def _load_resources(self):

        config = self.config
        self.background = pygame.image.load(config.IMAGE.get('background'))
        self.logo = pygame.transform.scale(
            pygame.image.load(config.IMAGE.get('logo')),
            (450, 70))
        self.cursor = pygame.image.load(
            config.TANK_IMAGE.get('player1')[0]
        ).convert_alpha().subsurface((0, 144), (48, 48))
        self.font = pygame.font.Font(config.FONT, config.SCREEN_WIDTH // 20)

    def _load_logo(self):
        config = self.config
        self.logo_rect = self.logo.get_rect()
        self.logo_rect.centerx, self.logo_rect.centery = config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 4

    def _load_tips(self):
        config = self.config
        self.player_normal = self.font.render('1 PLAYER', True, config.NORMAL)
        self.player_hover = self.font.render('1 PLAYER', True, config.HOVER)
        self.player_rect = self.player_normal.get_rect()
        self.player_rect.left, self.player_rect.top = config.SCREEN_WIDTH / 2.8, config.SCREEN_HEIGHT / 2.5

        self.players_normal = self.font.render('2 PLAYERS', True, config.NORMAL)
        self.players_hover = self.font.render('2 PLAYERS', True, config.HOVER)
        self.players_rect = self.players_normal.get_rect()
        self.players_rect.left, self.players_rect.top = config.SCREEN_WIDTH / 2.8, config.SCREEN_HEIGHT / 2

        self.name_normal = self.font.render('Set Your Name', True, config.NORMAL)
        self.name_hover = self.font.render('Set Your Name', True, config.HOVER)
        self.name_rect = self.name_normal.get_rect()
        self.name_rect.left, self.name_rect.top = config.SCREEN_WIDTH/2.8, config.SCREEN_HEIGHT/1.5

        self.cursor_rect = self.cursor.get_rect()

        self.tip = self.font.render('Press <Enter> to start !', True, config.NORMAL)
        self.tip_rect = self.tip.get_rect()
        self.tip_rect.centerx, self.tip_rect.top = config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 1.5

    def _game_loop(self):
        tip_flash_count = 0
        tip_flash_time = 30
        self.tip_flag = True
        self.double_mode = False
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        GameManager().double_mode = self.double_mode
                        return
                    elif event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.double_mode = not self.double_mode
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.double_mode:
                self.cursor_rect.right, self.cursor_rect.top = self.players_rect.left - 10, self.players_rect.top-10
            else:
                self.cursor_rect.right, self.cursor_rect.top = self.player_rect.left - 10, self.player_rect.top-10
            tip_flash_count += 1
            if tip_flash_count > tip_flash_time:
                tip_flash_count = 0
                self.tip_flag = not self.tip_flag

            self._draw_interface()
            pygame.display.update()
            clock.tick(60)

    def _draw_interface(self):
        screen = GameManager().screen
        screen.blit(self.background, (0, 0))
        screen.blit(self.logo, self.logo_rect)
        if self.tip_flag:
            screen.blit(self.tip, self.tip_rect)

        screen.blit(self.cursor, self.cursor_rect)

        if self.double_mode:
            screen.blit(self.player_normal, self.player_rect)
            screen.blit(self.players_hover, self.players_rect)
        else:
            screen.blit(self.player_hover, self.player_rect)
            screen.blit(self.players_normal, self.players_rect)
