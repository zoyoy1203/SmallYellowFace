import pygame


class Bullet1(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/b2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 12
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top <0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True


class Bullet2(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/b1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 14
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True


class Bullet3(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/b3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 14
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True


class Bullet4(pygame.sprite.Sprite):
    def __init__(self,position,bg_size,index):
        pygame.sprite.Sprite.__init__(self)
        self.width, self.height = bg_size[0], bg_size[1]
        self.image = pygame.image.load("images/b4.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
    def move(self,index):
        if index==0:
            self.rect.top-=14
        elif index==1:
            self.rect.left+=14
            self.rect.top-=14
        elif index==2:
            self.rect.left += 14
        elif index==3:
            self.rect.left += 14
            self.rect.top += 14
        elif index==4:
            self.rect.top += 14
        elif index==5:
            self.rect.left -= 14
            self.rect.top += 14
        elif index==6:
            self.rect.left -= 14
        elif index==7:
            self.rect.left-=14
            self.rect.top-=14

        if index==0 or index==1 or index==7:
            if self.rect.top<0:
                self.active=False
        elif index==3 or index==4 or index==5:
            if self.rect.top>self.width:
                self.active=False
        elif index==6:
            if self.rect.left<0:
                self.active=False
        elif index==2:
            if self.rect.left>self.width:
                self.active=False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True



