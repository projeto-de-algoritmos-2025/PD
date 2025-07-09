import pygame

WIDTH, HEIGHT = 1000, 700
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (64, 64, 64)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)

PHRASES = {
    "Português": [
        "Bom dia!",
        "Por favor.",
        "Muito obrigado.",
        "Permissão concedida.",
        "Com licença."
    ],
    "English": [
        "Good morning!",
        "Thank you.",
        "Please proceed.",
        "Excuse me.",
        "Of course."
    ],
    "Français": [
        "Bonjour!",
        "Merci beaucoup.",
        "S'il vous plaît.",
        "Excusez-moi.",
        "Bien sûr."
    ]
}

MAX_ATTEMPTS = 50
TIME_LIMIT = 300
DIFFICULTY_LEVELS = {
    "Fácil": 0.3,
    "Médio": 0.5,
    "Difícil": 0.7
}

PERFECT_COLOR = GREEN
GOOD_COLOR = BLUE
OK_COLOR = YELLOW
BAD_COLOR = RED

BLOCK_NORMAL = LIGHT_BLUE
BLOCK_SELECTED = ORANGE
BLOCK_SPACE = LIGHT_GRAY

