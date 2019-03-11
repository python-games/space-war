import pygame
import MainGame


class Enemy(pygame.sprite.Sprite):

    def __init__(self, color=(255, 40, 0), width=35, height=35):
        pygame.sprite.Sprite.__init__(self)

        self.width = width
        self.height = height

        self.change_x = 0
        self.change_y = 0

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y
