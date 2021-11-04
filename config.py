import os

SCREEN_WIDTH = 630
SCREEN_HEIGHT = 630

NORMAL = (255, 255, 255)
HOVER = (128, 0, 128)

TITLE = 'TankWar --061900224童锦涛'

FONT = os.path.join(os.getcwd(), 'resources/font/consola.ttf')

IMAGE = {
    'appear': os.path.join(os.getcwd(), 'resources/others/appear.png'),
    'background': os.path.join(os.getcwd(), 'resources/others/background.png'),
    'boom_dynamic': os.path.join(os.getcwd(), 'resources/others/boom_dynamic.png'),
    'boom_static': os.path.join(os.getcwd(), 'resources/others/boom_static.png'),
    'gameover': os.path.join(os.getcwd(), 'resources/others/gameover.png'),
    'logo': os.path.join(os.getcwd(), 'resources/others/logo.png'),
    'mask': os.path.join(os.getcwd(), 'resources/others/mask.png'),
    'protect': os.path.join(os.getcwd(), 'resources/others/protect.png'),
    'tip': os.path.join(os.getcwd(), 'resources/others/tip.png'),
    'loadbar': os.path.join(os.getcwd(), 'resources/others/gamebar.png')
}
TANK_IMAGE = {
    # player tank
    'player1': [os.path.join(os.getcwd(), 'resources/tank/tank_T1_0.png'),
                os.path.join(os.getcwd(), 'resources/tank/tank_T1_1.png'),
                os.path.join(os.getcwd(), 'resources/tank/tank_T1_2.png')],
    'player2': [os.path.join(os.getcwd(), 'resources/tank/tank_T2_0.png'),
                os.path.join(os.getcwd(), 'resources/tank/tank_T2_1.png'),
                os.path.join(os.getcwd(), 'resources/tank/tank_T2_2.png')],

    # enemy tank
    '0': [os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_1_0.png'),
          os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_1_1.png'),
          os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_1_2.png'),
          os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_1_3.png')],
    '1': [os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_2_0.png'),
          os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_2_1.png'),
          os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_2_2.png'),
          os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_2_3.png')],
    '2': [os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_3_0.png'),
          os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_3_1.png'),
          os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_3_2.png'),
          os.path.join(os.getcwd(), 'resources/images/enemyTank/enemy_3_3.png')],
}

BULLET_IMAGE_PATHS = {
    (0, 1): os.path.join(os.getcwd(), 'resources/images/bullet/bullet_down.png'),
    (1, 0): os.path.join(os.getcwd(), 'resources/images/bullet/bullet_right.png'),
    (0, -1): os.path.join(os.getcwd(), 'resources/images/bullet/bullet_up.png'),
    (-1, 0): os.path.join(os.getcwd(), 'resources/images/bullet/bullet_left.png')
}

SCENE_IMAGE = {
    'brick': os.path.join(os.getcwd(), 'resources/images/scene/brick.png'),
    'ice': os.path.join(os.getcwd(), 'resources/images/scene/ice.png'),
    'iron': os.path.join(os.getcwd(), 'resources/images/scene/iron.png'),
    'river1': os.path.join(os.getcwd(), 'resources/images/scene/river1.png'),
    'river2': os.path.join(os.getcwd(), 'resources/images/scene/river2.png'),
    'tree': os.path.join(os.getcwd(), 'resources/images/scene/tree.png')
}

HOME_IMAGE_PATHS = [os.path.join(os.getcwd(), 'resources/images/home/home1.png'),
                    os.path.join(os.getcwd(), 'resources/images/home/home_destroyed.png')]

# 音乐
AUDIO_PATHS = {
    'add': os.path.join(os.getcwd(), 'resources/audios/add.wav'),
    'bang': os.path.join(os.getcwd(), 'resources/audios/bang.wav'),
    'blast': os.path.join(os.getcwd(), 'resources/audios/blast.wav'),
    'fire': os.path.join(os.getcwd(), 'resources/audios/fire.wav'),
    'Gunfire': os.path.join(os.getcwd(), 'resources/audios/Gunfire.wav'),
    'hit': os.path.join(os.getcwd(), 'resources/audios/hit.wav'),
    'start': os.path.join(os.getcwd(), 'resources/audios/start.wav')
}

# 关卡
LEVEL = os.path.join(os.getcwd(), 'modules/levels')

