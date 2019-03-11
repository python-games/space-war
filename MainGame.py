import pygame
import SpaceShip
import Enemies

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("First game")

    clock = pygame.time.Clock()

    # SPACE
    spaceShip = SpaceShip.SpaceShip()

    spaceSprite = pygame.sprite.Group(spaceShip)

    # FIRS ENEMY
    enemies = []
    shift_x = 20
    shift_y = 15
    for i in range(10):
        enemies.append(Enemies.Enemy())
        enemies[i].set_pos(0+shift_x, shift_y)
        shift_x += 80

    shift_x = 60
    shift_y += 50
    for i in range(9):
        enemies.append(Enemies.Enemy())
        enemies[10+i].set_pos(0+shift_x, shift_y)
        shift_x += 80

    shift_x = 100
    shift_y += 50
    for i in range(8):
        enemies.append(Enemies.Enemy())
        enemies[i+19].set_pos(0+shift_x, shift_y)
        shift_x += 80

    enemiesSprite = pygame.sprite.Group(enemies)

    # GAME LOOP
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    spaceShip.go_left()
                if event.key == pygame.K_RIGHT:
                    spaceShip.go_right()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and spaceShip.change_x < 0:
                    spaceShip.stop()
                if event.key == pygame.K_RIGHT and spaceShip.change_x > 0:
                    spaceShip.stop()

        screen.fill((0, 0, 0))

        spaceSprite.update()

        spaceSprite.draw(screen)

        enemiesSprite.update()

        enemiesSprite.draw(screen)

        clock.tick(60)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
