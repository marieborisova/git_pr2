import os
import sys
import random
import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def main():
    size = 400, 300
    screen = pygame.display.set_mode(size)
    screen.fill((255,255,255))
    # создадим группу, содержащую все спрайты
    all_sprites = pygame.sprite.Group()

    # создадим спрайт
    sprite = pygame.sprite.Sprite()
    # определим его вид
    bomb_image = load_image("bomb.png")

    for i in range(50):
        # можно сразу создавать спрайты с указанием группы
        bomb = pygame.sprite.Sprite(all_sprites)
        bomb.image = bomb_image
        bomb.rect = bomb.image.get_rect()

        # задаём случайное местоположение бомбочке
        bomb.rect.x = random.randrange(width)
        bomb.rect.y = random.randrange(height)
    all_sprites.draw(screen)
    pygame.display.flip()
   # pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()



if __name__ == '__main__':
    main()
