import os
import random
import pygame

size = width, height = 400, 300
screen = pygame.display.set_mode(size)

def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")

    def __init__(self, group):
        # РќР•РћР‘РҐРћР”РРњРћ РІС‹Р·РІР°С‚СЊ РєРѕРЅСЃС‚СЂСѓРєС‚РѕСЂ СЂРѕРґРёС‚РµР»СЊСЃРєРѕРіРѕ РєР»Р°СЃСЃР° Sprite
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)


clock = pygame.time.Clock()

# РіСЂСѓРїРїР°, СЃРѕРґРµСЂР¶Р°С‰Р°СЏ РІСЃРµ СЃРїСЂР°Р№С‚С‹
all_sprites = pygame.sprite.Group()

for i in range(50):
    # РЅР°Рј СѓР¶Рµ РЅРµ РЅСѓР¶РЅРѕ РґР°Р¶Рµ РёРјСЏ РѕР±СЉРµРєС‚Р°!
    Bomb(all_sprites)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()

pygame.quit()