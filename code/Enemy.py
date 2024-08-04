#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity
class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.speed_x = ENTITY_SPEED[self.name]
        self.speed_y = 3  # Default vertical speed for Enemy3
        self.direction = 1  # 1 for down, -1 for up

    def move(self):
        if self.name == 'Enemy3':
            # Move horizontally to the left
            self.rect.centerx -= self.speed_x

            # Move vertically up and down
            self.rect.centery += self.speed_y * self.direction

            # Check for collision with screen borders
            if self.rect.bottom >= WIN_HEIGHT: 
                self.direction = -1  # Change direction to up
            elif self.rect.top <= 0:
                self.direction = 1  # Change direction to down

                # Increase speed when changing direction to down
                self.speed_y = 6
        else:
            # Default movement for other enemies
            self.rect.centerx -= self.speed_x

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
