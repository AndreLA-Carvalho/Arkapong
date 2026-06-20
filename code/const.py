import pygame

# C
C_ORANGE = (196, 91, 12)
C_LIGHT_ORANGE = (235, 165, 112)
C_WHITE = (255, 255, 255)
C_DARK_BLUE = (15, 25, 45)


# E
ENTITY_SPEED = {
    'menuBg0': 1,
    'menuBg1': 0,
    'menuBg2': 4,
    'menuBg3': 3,
    'menuBg4': 1,
    'menuBg5': 1,
    'Player': 0.1,
    'Ball': 0.17,
    'brick1': 0,
    'brick2': 0,
    'brick3': 0
}

ENTITY_HEALTH = {
    'menuBg0': 999,
    'menuBg1': 999,
    'menuBg2': 999,
    'menuBg3': 999,
    'menuBg4': 999,
    'menuBg5': 999,
    'Player': 3,
    'Ball': -1,
    'brick1': 1,
    'brick2': 1,
    'brick3': 1
}

ENTITY_DAMAGE = {
    'menuBg0': 0,
    'menuBg1': 0,
    'menuBg2': 0,
    'menuBg3': 0,
    'menuBg4': 0,
    'menuBg5': 0,
    'Player': 1,
    'Ball': 1,
    'brick1': 0,
    'brick2': 0,
    'brick3': 0
}

ENTITY_SCORE = {
    'menuBg0': 0,
    'menuBg1': 0,
    'menuBg2': 0,
    'menuBg3': 0,
    'menuBg4': 0,
    'menuBg5': 0,
    'Player': 0,
    'Ball': 0,
    'brick1': 10,
    'brick2': 20,
    'brick3': 30
}


# K
KEYS = {
    'up': pygame.K_w,
    'down': pygame.K_s,
    'left': pygame.K_a,
    'right': pygame.K_d,
    'space': pygame.K_SPACE,
}

#M
MENU_OPTIONS = [
    'JOGAR',
    'PONTUACAO',
    'SAIR'
]

# S
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
