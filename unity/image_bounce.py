import pygame

# prereq: pip install pygame
screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)

img = pygame.image.load('<image-path>>')

keep_alive = True
x = 0
y = 0
while True:
    while x < 360/2:
        screen.blit(img, [x, y])
        pygame.display.update()
        x = x + 1
        y = y + 1
    while y < 600/2:
        screen.blit(img, [x, y])
        pygame.display.update()
        x = x - 1
        y = y + 1
    while x > 0:
        screen.blit(img, [x, y])
        pygame.display.update()
        x = x - 1
        y = y - 1
    while x < 360/2:
        screen.blit(img, [x, y])
        pygame.display.update()
        x = x + 1
        y = y - 1
    while y > 0:
        screen.blit(img, [x, y])
        pygame.display.update()
        x = x - 1
        y = y - 1
    print(x, y)
