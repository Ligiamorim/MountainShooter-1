#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score

class Level:
    def __init__(self, window, level_name, menu_return, player_score):
        self.window = window
        self.level_name = level_name
        self.menu_return = menu_return
        self.player_score = player_score
        self.duration = 20  # default duration for levels 1 and 2
        self.background = None
        self.music = None

        if level_name == 'Level1':
            self.duration = 20  # example duration for Level1
            self.background = 'assets/Level1_background.png'
            self.music = 'asset/Level1.mp3'
        elif level_name == 'Level2':
            self.duration = 20  # example duration for Level2
            self.background = 'assets/Level2_background.png'
            self.music = 'assets/Level2.mp3'
        elif level_name == 'Level3':
            self.duration = 40  # double the duration for Level3
            self.background = 'assets/level3_background.png'
            self.music = 'assets/level3_music.mp3'

        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(-1)

    def run(self, player_score):
        # Main loop for running the level
        start_ticks = pygame.time.get_ticks()
        while True:
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000
            if seconds > self.duration:
                return True  # Level finished

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.window.fill((0, 0, 0))
            # Add background drawing and enemy generation logic here
            pygame.display.update()
import pygame

class Enemy3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/enemy3.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = -5
        self.speed_y = 3
        self.direction = 1

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y * self.direction

        if self.rect.bottom >= WIN_HEIGHT:
            self.direction = -1
        elif self.rect.top <= 0:
            self.direction = 2

    def shoot(self):
        # Add shooting logic here
        pass

import pygame
import sys
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # [Player1, Player2]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        level = Level(self.window, 'Level3', menu_return, player_score)
                        level_return = level.run(player_score)
                        if level_return:
                            score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[3]:
                score.show()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()

