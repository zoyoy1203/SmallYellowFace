import pygame
from random import *


class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size,small_enemies_index):
        pygame.sprite.Sprite.__init__(self)
        self.image=[]
        self.image.extend([\
            pygame.image.load("images/f1.png").convert_alpha(), \
            pygame.image.load("images/f2.png").convert_alpha(), \
            pygame.image.load("images/f3.png").convert_alpha(), \
            pygame.image.load("images/f4.png").convert_alpha(),\
            pygame.image.load("images/f5.png").convert_alpha(), \
            pygame.image.load("images/f6.png").convert_alpha(), \
            pygame.image.load("images/f7.png").convert_alpha(), \
            pygame.image.load("images/f8.png").convert_alpha(),\
            pygame.image.load("images/f9.png").convert_alpha(), \
            pygame.image.load("images/f10.png").convert_alpha(), \
            pygame.image.load("images/f11.png").convert_alpha(), \
            pygame.image.load("images/f12.png").convert_alpha(), \
            pygame.image.load("images/df4.png").convert_alpha(), \
            pygame.image.load("images/df12.png").convert_alpha(), \
            pygame.image.load("images/f15.png").convert_alpha(), \
            pygame.image.load("images/f16.png").convert_alpha(), \
            pygame.image.load("images/df11.png").convert_alpha(), \
            pygame.image.load("images/df18.png").convert_alpha(), \
            pygame.image.load("images/20.png").convert_alpha(), \
            pygame.image.load("images/21.png").convert_alpha(), \
            pygame.image.load("images/22.png").convert_alpha(), \
            pygame.image.load("images/23.png").convert_alpha(), \
            pygame.image.load("images/24.png").convert_alpha(), \
            pygame.image.load("images/25.png").convert_alpha() \
            ])
       # self.image = pygame.image.load("images/f1.png").convert_alpha()
        self.destroy_images = pygame.image.load("images/ddf6.png").convert_alpha()

        self.rect = self.image[0].get_rect()    #因为列表里的图标大小一致，所以可以这样写，如果不一致，填写self.image[small_enemies_index]
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 2
        self.active = True
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-5 * self.height, 0)
        self.mask = pygame.mask.from_surface(self.image[small_enemies_index])

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-5 * self.height, 0)


class MidEnemy(pygame.sprite.Sprite):
    energy = 20

    def __init__(self, bg_size,mid_enemies_index):
        pygame.sprite.Sprite.__init__(self)
        self.image = []
        self.image.extend([ \
            pygame.image.load("images/26.png").convert_alpha(), \
            pygame.image.load("images/29.png").convert_alpha(), \
            pygame.image.load("images/42.png").convert_alpha(), \
            pygame.image.load("images/35.png").convert_alpha(), \
            pygame.image.load("images/36.png").convert_alpha(), \
            pygame.image.load("images/26.png").convert_alpha(), \
            pygame.image.load("images/46.png").convert_alpha(), \
            pygame.image.load("images/27.png").convert_alpha(), \
            pygame.image.load("images/30.png").convert_alpha(), \
            pygame.image.load("images/31.png").convert_alpha(), \
            pygame.image.load("images/34.png").convert_alpha(),\
            pygame.image.load("images/37.png").convert_alpha(), \
            pygame.image.load("images/41.png").convert_alpha(), \
            pygame.image.load("images/47.png").convert_alpha() \
 \
            ])

        self.image_hit = pygame.image.load("images/ddf1.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([ \
            pygame.image.load("images/ddf2.png").convert_alpha(), \
            pygame.image.load("images/ddf3.png").convert_alpha(), \
            pygame.image.load("images/ddf4.png").convert_alpha(), \
            pygame.image.load("images/ddf5.png").convert_alpha() \
            ])
        self.rect = self.image[mid_enemies_index].get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-10 * self.height, -self.height)
        self.mask = pygame.mask.from_surface(self.image[mid_enemies_index])
        self.energy = MidEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):

        self.active = True
        self.energy = MidEnemy.energy
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-10 * self.height, -self.height)


class BigEnemy(pygame.sprite.Sprite):
    energy = 40

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("images/97.png").convert_alpha()
        self.image2 = pygame.image.load("images/98.png").convert_alpha()
        self.image_hit = pygame.image.load("images/ddf1.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([ \
            pygame.image.load("images/ddf1.png").convert_alpha(), \
            pygame.image.load("images/ddf2.png").convert_alpha(), \
            pygame.image.load("images/ddf3.png").convert_alpha(), \
            pygame.image.load("images/ddf4.png").convert_alpha(), \
            pygame.image.load("images/ddf5.png").convert_alpha(), \
            pygame.image.load("images/ddf5.png").convert_alpha() \
            ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-15 * self.height, -5 * self.height)
        self.mask = pygame.mask.from_surface(self.image1)
        self.energy = BigEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.energy = BigEnemy.energy
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-15 * self.height, -5 * self.height)
