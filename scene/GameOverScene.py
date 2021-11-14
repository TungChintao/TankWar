import sys
import pygame
from manager.GameManager import GameManager
from scene.AbstractScene import AbstractScene


class GameOverScene(AbstractScene):

    def _load_resources(self):
        config = self.config
        self.background = pygame.image.load(config.IMAGE.get('background'))
        self.font = pygame.font.Font(config.FONT, config.SCREEN_WIDTH//12)
        self.font2 = pygame.font.Font(config.FONT, config.SCREEN_WIDTH//18)
        self.tank_cursor = pygame.image.load(
            config.TANK_IMAGE.get('player1')
        ).convert_alpha().subsurface((0, 144), (48, 48))

    def _load_tips(self):
        config = self.config

        self.font_render = self.font.render("Player Record", True, (255, 255, 0))

        self.font_rect = self.font_render.get_rect()
        self.kill_render = self.font2.render('Kill Enemies: ' + str(GameManager().kill_enemies), True, (0, 255, 0))
        self.kill_rect = self.kill_render.get_rect()
        self.kill_rect.centerx, self.kill_rect.top = config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 4

        self.time_render = self.font2.render('Time Consume: %.2fs' % GameManager().time_consuming, True, (0, 255, 0))
        self.time_rect = self.time_render.get_rect()
        self.time_rect.centerx, self.time_rect.top = config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 3
        self.font_rect.centerx, self.font_rect.centery = config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 9
        self.restart_render_normal = self.font.render('RESTART', True, config.NORMAL)
        self.restart_render_hover = self.font.render('RESTART', True, config.HOVER)
        self.quit_render_normal = self.font.render('QUIT', True, config.NORMAL)
        self.quit_render_hover = self.font.render('QUIT', True, config.HOVER)

    def _draw_interface(self):
        screen = GameManager().screen
        screen.blit(self.background, (0, 0))

        if self.record_show_flag:
            screen.blit(self.font_render, self.font_rect)

        screen.blit(self.kill_render, self.kill_rect)
        screen.blit(self.time_render, self.time_rect)

        if not self.exit_game:
            screen.blit(self.tank_cursor, self.tank_rect)
            screen.blit(self.restart_render_hover, self.restart_rect)
            screen.blit(self.quit_render_normal, self.quit_rect)
        else:
            screen.blit(self.tank_cursor, self.tank_rect)
            screen.blit(self.restart_render_normal, self.restart_rect)
            screen.blit(self.quit_render_hover, self.quit_rect)

    def _load_bottons(self):
        config = self.config
        self.tank_rect = self.tank_cursor.get_rect()
        self.restart_rect = self.restart_render_normal.get_rect()
        self.restart_rect.centerx, self.restart_rect.top = config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 1.8
        self.quit_rect = self.quit_render_normal.get_rect()
        self.quit_rect.centerx, self.quit_rect.top = config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 1.4

    def _game_loop(self):
        clock = pygame.time.Clock()

        record_time = 30
        record_count = 0
        self.record_show_flag = True
        self.exit_game = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        GameManager().exit_game = self.exit_game
                        return
                    elif event.key in [pygame.K_UP, pygame.K_w, pygame.K_DOWN, pygame.K_s]:
                        self.exit_game = not self.exit_game

            record_count += 1
            if record_count > record_time:
                self.record_show_flag = not self.record_show_flag
                record_count = 0
            if self.exit_game:
                self.tank_rect.right, self.tank_rect.top = self.quit_rect.left - 10, self.quit_rect.top
            else:
                self.tank_rect.right, self.tank_rect.top = self.restart_rect.left - 10, self.restart_rect.top

            self._draw_interface()

            pygame.display.update()
            clock.tick(60)

