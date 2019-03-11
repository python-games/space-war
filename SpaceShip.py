import pygame
import MainGame


class SpaceShip(pygame.sprite.Sprite):

    def __init__(self, color=(255, 255, 255), width=50, height=50):
        pygame.sprite.Sprite.__init__(self)

        self.width = width
        self.height = height

        self.change_x = 0

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.rect.x = MainGame.SCREEN_WIDTH / 2 - self.width/2
        self.rect.y = MainGame.SCREEN_HEIGHT - 1.25 * height

    def update(self):
        if self.rect.x <= 0 and self.change_x < 0:
            self.stop()
        if self.rect.x >= MainGame.SCREEN_WIDTH-self.width and self.change_x > 0:
            self.stop()
        else:
            self.rect.x += self.change_x

    def go_left(self):
        self.change_x -= 5

    def go_right(self):
        self.change_x += 5

    def stop(self):
        self.change_x = 0
