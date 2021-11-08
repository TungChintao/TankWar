import sys
import pygame
from factory import *
from uiutil import DIRECTION
from scene.AbstractScene import AbstractScene
from manager.GameManager import GameManager
from sprites.SpriteGroup import SpriteGroup
from sprites.SceneElementGroup import SceneElementGroup


class GameRunScene(AbstractScene):

    def _load_resources(self):
        config = self.config
        self.tank_factory = TankFactory(self.config)
        self.scene_factory = SceneElementFactory(self.config)
        self.scene_elements = None
        self.sprites = SpriteGroup()

        self.music = GameManager().music
        self.home_image = config.HOME_IMAGE
        self.grid_size = config.GRID_SIZE
        self.border_len = config.BORDER_LEN
        self.background = pygame.image.load(config.IMAGE.get('background'))
        self.font = pygame.font.Font(config.FONT, config.SCREEN_HEIGHT // 35)
        self.grid_size = config.GRID_SIZE

        self.scene_elements = SceneElementGroup()
        self.win_flag = False
        self.next_level = True

    def __load_tanks(self):
        self.__tank_player1 = self.tank_factory.create_tank(self.__player_point[0], TankFactory.PLAYER1_TANK)
        self.sprites.add(self.__tank_player1)
        self.__tank_player2 = None
        if GameManager().double_mode:
            self.__tank_player2 = self.tank_factory.create_tank(self.__player_point[1], TankFactory.PLAYER2_TANK)
            self.sprites.add(self.__tank_player2)

    def load_game_screen(self):
        GameManager().load_screen(
            (self.config.SCREEN_WIDTH, self.config.SCREEN_HEIGHT)
        )

    def __load_game(self):
        home_position = ()
        home_protection_position = []

        elements_map = {
            'B': SceneElementFactory.BRICK,
            'I': SceneElementFactory.IRON,
            'T': SceneElementFactory.TREE,
            'R': SceneElementFactory.RIVER_1
        }

        f = open(GameManager().game_file)
        num = -1
        for line in f.readlines():
            line = line.strip('\n')
            if line.startswith('#') or (not line):
                continue
            elif line.startswith('%ENEMYTOTALNUM'):
                self.__enemy_total_num = 20 + GameManager().level
            elif line.startswith('%MAXENEMYNUM'):
                self.max_enemy_num = 6 + GameManager().level
            elif line.startswith('%HOMEPOS'):
                home_position = line.split(':')[-1]
                home_position = [
                    int(home_position.split(',')[0]), int(home_position.split(',')[1])
                ]
                home_position = (
                    self.border_len + home_position[0] * self.grid_size,
                    self.border_len + home_position[1] * self.grid_size
                )
            # 我方坦克初始位置
            elif line.startswith('%PLAYERTANKPOS'):
                self.__player_point = line.split(':')[-1]
                self.__player_point = [
                    [
                        int(pos.split(',')[0]), int(pos.split(',')[1])
                    ] for pos in self.__player_point.split(' ')
                ]
                self.__player_point = [
                    (self.border_len + pos[0] * self.grid_size, self.border_len + pos[1] * self.grid_size
                     ) for pos in self.__player_point
                ]
            # 敌方坦克初始位置
            elif line.startswith('%ENEMYTANKPOS'):
                self.__enemy_point = line.split(':')[-1]
                self.__enemy_point = [
                    [
                        int(pos.split(',')[0]), int(pos.split(',')[1])
                    ] for pos in self.__enemy_point.split(' ')
                ]
                self.__enemy_point = [
                    (
                        self.border_len + pos[0] * self.grid_size, self.border_len + pos[1] * self.grid_size
                    ) for pos in self.__enemy_point
                ]

    def play_music(self, music):
        print(self.music[music])

    def dispatch_player_operation(self):
        key_press = pygame.key.get_pressed()
        key_map = {
            'direction': {
                self.__tank_player1: {
                    pygame.K_UP: DIRECTION.UP,
                    pygame.K_DOWN: DIRECTION.DOWN,
                    pygame.K_LEFT: DIRECTION.LEFT,
                    pygame.K_RIGHT: DIRECTION.RIGHT
                }
            },
            'shoot': {
                self.__tank_player1: pygame.K_SPACE,
            }
        }
        player_tank_list = []
        if self.__tank_player1.life >= 0:
            player_tank_list.append(self.__tank_player1)
        if GameManager().double_mode and self.__tank_player2.life >= 0:
            player_tank_list.append(self.__tank_player2)

        for tank in player_tank_list:
            for key, direction in key_map['direction'][tank].items():
                if key_press[key]:
                    self.sprites.remove(tank)
                    tank.move(direction)
                    self.sprites.add(tank)
                    break
            if key_press[key_map['shoot'][tank]]:
                bullet = tank.shoot()
                if bullet:
                    # self.play_music('shoot')
                    self.sprites.add(bullet)

    def game_loop(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.dispatch_player_operation()
            self.sprites.update()
            self._draw_interface()

            clock.tick(60)

    def _draw_interface(self):
        screen = GameManager().screen
        screen.blit(self.background, (0, 0))
        self.sprites.draw(screen, 1)
        pygame.display.flip()

    def show(self):
        self.load_game_screen()
        self.__load_game()
        self.__load_tanks()
        self.game_loop()
        GameManager().win_flag = self.win_flag
