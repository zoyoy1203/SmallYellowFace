import pygame

class King(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("images/k1.gif").convert_alpha()
        self.image2 = pygame.image.load("images/k2.gif").convert_alpha()
        self.image3 = pygame.image.load("images/k3.png").convert_alpha()
        self.image4 = pygame.image.load("images/k4.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/die1.gif").convert_alpha(), \
            pygame.image.load("images/die2.gif").convert_alpha(), \
            pygame.image.load("images/die3.gif").convert_alpha(), \
            pygame.image.load("images/die3.gif").convert_alpha() \
            ])
        self.destroy_images1 = []
        self.destroy_images1.extend([ \
            pygame.image.load("images/die4.png").convert_alpha(), \
            pygame.image.load("images/die5.png").convert_alpha(), \
            pygame.image.load("images/die6.png").convert_alpha(), \
            pygame.image.load("images/die6.png").convert_alpha() \
            ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.speed = 10
        self.active = True
        self.change_k=True
        self.invincible = False
        self.mask = pygame.mask.from_surface(self.image1)#?????????

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top=self.height     #self.rect.top = 0   打通上边界

    def moveDown(self):
        if self.rect.bottom < self.height:
            self.rect.top += self.speed
        else:
            self.rect.top=0-self.rect.height   #  self.rect.bottom = self.height - 60   打通下边界， self.rect.top=0
    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left=self.width   #self.rect.left = 0
    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.left=0-self.rect.width   #self.rect.right = self.width


    def reset(self):                          #死后重生的位置设置
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60

        self.active = True
        self.invincible = True




