import os.path
from os import walk, path
import pygame
import sys
from settings import DEFAULT_FONT


def import_animation(path):
    lst = []
    for info in walk(path):
        for img in info[2]:
            lst.append(pygame.image.load(path + '/' + img).convert_alpha())
    return lst


def load_level(name):
    if not os.path.isfile(name):
        print(f"Файл {name} не найден")
        return ['', '@', 'XXXX']
    return [i.rstrip('\n') for i in open(name, 'r', encoding='utf-8').readlines()]


# эта функция отвечает за печать текста на кнопках и не только
def render_text(message, x, y, screen, font_color=(0, 0, 0), font_type=DEFAULT_FONT, font_size=50):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))


def termination():
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()