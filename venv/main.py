# main.py
import pygame
import sys
import traceback
import king
import face
import bb
import supply
import win32api,win32con  #我用他用来调节系统音量

from pygame.locals import *
from random import *

pygame.init()  # 初始化pygame
pygame.mixer.init()  # 初始化混音器模块



BLACK = (0, 0, 0)    #设置颜色变量
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.3)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.3)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.3)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.3)
get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.3)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav") #白大王升级的声音
upgrade_sound.set_volume(0.3)
enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.3)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.3)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.5)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.3)


def volume_up():#音量增加2
    win32api.keybd_event(0xaf,0,0,0)
    win32api.keybd_event(0xaf,0,win32con.KEYEVENTF_KEYUP,0)

def volume_down():#音量减少2
    win32api.keybd_event(0xae,0,0,0)
    win32api.keybd_event(0xae,0,win32con.KEYEVENTF_KEYUP,0)

def volume_mute():#静音(但是不改变音量)
    win32api.keybd_event(0xad,0,0,0)
    win32api.keybd_event(0xad,0,win32con.KEYEVENTF_KEYUP,0)


small_enemies_index=0
mid_enemies_index=0
big_enemies_index=0

# 添加敌人数量函数
def add_small_enemies(group1, group2,num,bg_size):
    global small_enemies_index
    for i in range(num):
        e1 = face.SmallEnemy(bg_size,small_enemies_index)
        small_enemies_index=(small_enemies_index+1)%24
        group1.add(e1)
        group2.add(e1)


def add_mid_enemies(group1, group2, num,bg_size):
    global mid_enemies_index
    for i in range(num):
        e2 = face.MidEnemy(bg_size,mid_enemies_index)
        mid_enemies_index = (mid_enemies_index + 1) % 7
        group1.add(e2)
        group2.add(e2)


def add_big_enemies(group1, group2, num,bg_size):
    for i in range(num):
        e3 = face.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)


def inc_speed(target, inc): #增加速度的函数
    for each in target:
        each.speed += inc


def main():
    small_enemies_index1 = 0  # 绘制小型敌人的列表索引
    mid_enemies_index1=0
    mid_enemies_index2=6
    big_enemies_index1=0

    size = pygame.display.list_modes()  #获取当前显示器支持的分辨率
    bg_size = width, height = 1024, 640


    screen = pygame.display.set_mode(bg_size)  # 创建窗口
    pygame.display.set_caption("小黄脸之战")  # 设置窗口标题

    bg_images_index=0
    bg_image=pygame.image.load("images/bg.jpg").convert()
    bg_image1=pygame.image.load("images/bg1.png").convert()
    bg_image2 = pygame.image.load("images/bg2.jpg").convert()
    bg_image3 = pygame.image.load("images/bg3.jpg").convert()
    bg_image4 = pygame.image.load("images/bg4.jpg").convert()
    bg_image5 = pygame.image.load("images/bg5.jpg").convert()
    bg_image6 = pygame.image.load("images/bg6.jpg").convert()
    obg =bg_image   # 载入原始背景图片
    background = pygame.transform.scale(obg, bg_size)

    #background = obg  # 改变后的背景图片


    fullscreen = False  # 是否全屏

    # 载入游戏音乐
    musics = []
    musics.extend([ \
        "sound/讲真的.mp3", \
        "sound/你打不过我吧.mp3", \
        "sound/Axero - Trip.mp3", \
        "sound/Es rappelt im Karton.mp3", \
        "sound/Wicked Wonderland.mp3", \
        "sound/that girl.mp3", \
        "sound/ConsoulTrainin-TakeMeToInfinity.mp3",\
        "sound/Shadow.mp3" \

        ])
    music_num = 0
    music_volume = 0.5

    pygame.mixer.music.load(musics[music_num])
    pygame.mixer.music.set_volume(music_volume)

    pygame.mixer.music.play(1)

     #背景音乐

    #设置背景音乐图标
    music_mute=False
    paused1=False
    music_image1=pygame.image.load("images/95.png").convert_alpha()
    music_image2 = pygame.image.load("images/94.png").convert_alpha()
    music_image3=pygame.image.load("images/99.png").convert_alpha()
    music_image = music_image1
    music_image_rect = music_image.get_rect()
    music_image_rect.left, music_image_rect.top = 10, 40

    music_plus_image=pygame.image.load("images/50.png").convert_alpha()
    music_less_image=pygame.image.load("images/51.png").convert_alpha()
    music_mute_image = pygame.image.load("images/52.png").convert_alpha()
    sounds_mute_image = pygame.image.load("images/53.png").convert_alpha()
    music_plus_image_rect=music_plus_image.get_rect()
    music_plus_image_rect.left,music_plus_image_rect.top=width-music_plus_image_rect.width-10,80
    music_less_image_rect=music_less_image.get_rect()
    music_less_image_rect.left, music_less_image_rect.top = width - music_less_image_rect.width - 10, 150
    music_mute_image_rect = music_mute_image.get_rect()
    music_mute_image_rect.left, music_mute_image_rect.top = width - music_mute_image_rect.width - 10, 220
    sounds_mute_image_rect=sounds_mute_image.get_rect()
    sounds_mute_image_rect.left,sounds_mute_image_rect.top=width-sounds_mute_image_rect.width-20,290


    # 生成我方老大
    me = king.King(bg_size)
    change_me=True

    enemies = pygame.sprite.Group()  #生成一个敌人总队列

    # 生成低级小黄脸
    small_enemies = pygame.sprite.Group()  #生成一个小敌人队列
    add_small_enemies(small_enemies, enemies, 24,bg_size)  #分别在小敌人队列，总队列中添加18个小敌人

    # 生成中级小黄脸
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 4,bg_size)

    # 生成高级小黄脸
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 2,bg_size)

    # 生成子弹1
    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 8
    for i in range(BULLET1_NUM):
       bullet1.append(bb.Bullet1(me.rect.midtop))  #便便子弹出现位置在白大王的脑袋上方正中央

    # 生成子弹2
    bullet2 = []
    bullet2_index = 0
    BULLET2_NUM = 16
    for i in range(BULLET2_NUM // 2):
        bullet2.append(bb.Bullet2((me.rect.centerx -10, me.rect.centery)))  #超级便便的位置待定
        bullet2.append(bb.Bullet2((me.rect.centerx , me.rect.centery)))

    #生成子弹3
    bullet3=[]
    bullet3_index=0
    BULLET3_NUM=32
    for i in range(BULLET3_NUM // 4):
        bullet3.append(bb.Bullet3((me.rect.centerx - 10, me.rect.centery)))
        bullet3.append(bb.Bullet3((me.rect.centerx+10, me.rect.centery)))
        bullet3.append(bb.Bullet3((me.rect.left -10, me.rect.centery)))
        bullet3.append(bb.Bullet3((me.rect.left+ me.rect.width+10, me.rect.centery)))

    # 生成子弹4
    bullet4 = []
    bullet4_index1 = 0
    bullet4_index2 = 0
    BULLET4_NUM = 64
    for i in range(BULLET4_NUM):
        bullet4.append(bb.Bullet4((me.rect.centerx, me.rect.centery),bg_size,bullet4_index1))
        bullet4_index1=(bullet4_index1+1)%BULLET4_NUM


    clock = pygame.time.Clock()#实例化Clock对象  Clock里的tick()方法能用来设置帧频

    # 中弹图片索引
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0

    # 统计得分
    score = 0
    score_font = pygame.font.Font("font/font.ttf", 36)

    # 标志是否暂停游戏
    paused = False
    pause_nor_image = pygame.image.load("images/pause_nor.png").convert_alpha()
    pause_pressed_image = pygame.image.load("images/pause_pressed.png").convert_alpha()
    resume_nor_image = pygame.image.load("images/resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load("images/resume_pressed.png").convert_alpha()
    paused_rect = pause_nor_image.get_rect()
    paused_rect.left, paused_rect.top = width - paused_rect.width - 10, 10
    paused_image = pause_nor_image                             #

    # 设置难度级别
    level = 1

    # 全屏炸弹
    bomb_image = pygame.image.load("images/zd.png").convert_alpha()
    bomb_rect = bomb_image.get_rect()
    bomb_font = pygame.font.Font("font/font.ttf", 48)
    bomb_num = 3

    # 每30秒发放一个补给包
    bg_index=0
    bullet2_supply = supply.Bullet2_Supply(bg_size)
    bullet3_supply=supply.Bullet3_Supply(bg_size)
    bullet4_supply = supply.Bullet4_Supply(bg_size)
    bomb_supply = supply.Bomb_Supply(bg_size)
    life_supply=supply.Life_Supply(bg_size)
    bg_hb_supply=supply.Bg_Hb_Supply(bg_size)
    change_k_supply=supply.Change_K_Supply(bg_size)
    SUPPLY1_TIME = USEREVENT                   #自定义补给包发放时间事件
    SUPPLY2_TIME =USEREVENT+1
    SUPPLY3_TIME=USEREVENT+2
    SUPPLY4_TIME=USEREVENT+3
    SUPPLY5_TIME=USEREVENT+4
    SUPPLY6_TIME=USEREVENT+7
    SUPPLY7_TIME = USEREVENT + 8
    pygame.time.set_timer(SUPPLY1_TIME, 11 * 1000)#
    pygame.time.set_timer(SUPPLY2_TIME, 22 * 1000)
    pygame.time.set_timer(SUPPLY3_TIME, 33 * 1000)
    pygame.time.set_timer(SUPPLY4_TIME, 44 * 1000)
    pygame.time.set_timer(SUPPLY5_TIME, 55 * 1000)
    pygame.time.set_timer(SUPPLY6_TIME, 5 * 1000)
    # 超级子弹定时器
    SUPER_BULLET_TIME = USEREVENT + 5  #定义一个超级子弹使用时间的事件

    # 标志是否使用超级子弹
    is_bullet =1

    # 解除我方无敌状态定时器
    INVINCIBLE_TIME = USEREVENT + 6

    # 生命数量
    life_image = pygame.image.load("images/k.gif").convert_alpha()   #游戏界面右下方显示的生命
    life_rect = life_image.get_rect()
    life_num = 3

    # 用于阻止重复打开记录文件
    recorded = False  #

    # 游戏结束画面
    gameover_font = pygame.font.Font("font/font.TTF", 48)
    again_image = pygame.image.load("images/again.png").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("images/gameover.png").convert_alpha()
    gameover_rect = gameover_image.get_rect()

    # 用于切换图片
    switch_image = True

    # 用于延迟
    delay = 100

    running = True

    while running:              #游戏循环运行中，处理事件消息
        for event in pygame.event.get():   #游戏关闭
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            elif event.type == MOUSEBUTTONDOWN:        #鼠标按键被按下
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    paused = not paused      #paused的初始值为False
                    if paused:
                        pygame.time.set_timer(SUPPLY1_TIME, 0)
                        pygame.time.set_timer(SUPPLY2_TIME, 0)
                        pygame.time.set_timer(SUPPLY3_TIME, 0)
                        pygame.time.set_timer(SUPPLY4_TIME, 0)
                        pygame.time.set_timer(SUPPLY5_TIME, 0)
                        pygame.time.set_timer(SUPPLY6_TIME, 0)
                        pygame.mixer.music.pause()  #背景音乐暂停播放
                        pygame.mixer.pause()        #音效暂停播放
                    else:
                        pygame.time.set_timer(SUPPLY1_TIME, 11 * 1000)    #补给包的发放时间在这里统计
                        pygame.time.set_timer(SUPPLY2_TIME, 22 * 1000)
                        pygame.time.set_timer(SUPPLY3_TIME, 33 * 1000)
                        pygame.time.set_timer(SUPPLY4_TIME, 44 * 1000)
                        pygame.time.set_timer(SUPPLY5_TIME, 55 * 1000)
                        pygame.time.set_timer(SUPPLY6_TIME, 5 * 1000)
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()

                if event.button==1and music_image_rect.collidepoint(event.pos) and not music_mute:
                    music_image = music_image3
                    music_image_rect = music_image.get_rect()

                    music_num=(music_num+1)%8
                    #pygame.mixer.music.stop()
                    #pygame.mixer.init()
                    pygame.mixer.music.load(musics[music_num])
                    pygame.mixer.music.set_volume(music_volume)
                    pygame.mixer.music.play(1)
                    #pygame.mixer.music.queue(filename)

                if music_plus_image_rect.collidepoint(event.pos):
                    volume_up()
                if music_less_image_rect.collidepoint(event.pos):
                    volume_down()
                if music_mute_image_rect.collidepoint(event.pos):
                    music_mute=not music_mute
                    if music_mute:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                if sounds_mute_image_rect.collidepoint(event.pos):
                    volume_mute()


            elif event.type == MOUSEMOTION:       #处理鼠标是否经过右上角图标的变化
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image = resume_pressed_image
                    else:
                        paused_image = pause_pressed_image
                else:
                    if paused:
                        paused_image = resume_nor_image
                    else:
                        paused_image = pause_nor_image

                if music_image_rect.collidepoint(event.pos):
                        music_image=music_image2
                        music_image_rect = music_image.get_rect()
                else:
                    music_image = music_image1
                    music_image_rect = music_image.get_rect()



            elif event.type == KEYDOWN:     #按下空格键触发全屏炸弹，屏幕上的小黄脸全部死翘翘
                if event.key == K_SPACE:
                    if bomb_num:
                        bomb_num -= 1
                        bomb_sound.play()
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.active = False

                #key_pressed = pygame.key.get_pressed()
                elif event.key==K_z and not music_mute:
                    music_num = (music_num + 1) % 8
                    # pygame.mixer.init()
                    pygame.mixer.music.load(musics[music_num])
                    pygame.mixer.music.set_volume(music_volume)
                    pygame.mixer.music.play(1)

                elif event.key ==K_x:
                    volume_up()
                elif event.key==K_c:
                    volume_down()
                elif event.key==K_v:
                    music_mute=not music_mute
                    if music_mute:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()


                elif event.key == K_ESCAPE:
                    fullscreen = not fullscreen
                    if fullscreen:
                        bg_size =width,height=size[2]
                        screen = pygame.display.set_mode(bg_size, FULLSCREEN | HWSURFACE)
                        background = pygame.transform.scale(obg,bg_size)

                        paused_rect.left, paused_rect.top = width - paused_rect.width - 10, 10  #左上角的暂停，恢复按钮

                        music_plus_image_rect.left, music_plus_image_rect.top = width - music_plus_image_rect.width - 10, 80  #控制音量大小的按钮
                        music_less_image_rect.left, music_less_image_rect.top = width - music_less_image_rect.width - 10, 150
                        music_mute_image_rect.left, music_mute_image_rect.top = width - music_mute_image_rect.width - 10, 220
                        sounds_mute_image_rect.left, sounds_mute_image_rect.top = width - sounds_mute_image_rect.width - 20, 290

                        me=king.King(bg_size)

                        face.SmallEnemy.width=bg_size[0]    #这两句待定，没用到。（小黄脸掉落问题的解决）
                        face.SmallEnemy.height=bg_size[1]

                        bullet2_supply = supply.Bullet2_Supply(bg_size)
                        bullet3_supply = supply.Bullet3_Supply(bg_size)
                        bullet4_supply = supply.Bullet4_Supply(bg_size)
                        bomb_supply = supply.Bomb_Supply(bg_size)
                        life_supply = supply.Life_Supply(bg_size)
                        bg_hb_supply=supply.Bg_Hb_Supply(bg_size)
                        change_k_supply=supply.Change_K_Supply(bg_size)
                    else:
                        bg_size =width,height=1024,640
                        screen = pygame.display.set_mode(bg_size)
                        background = pygame.transform.scale(obg, bg_size)

                        paused_rect.left, paused_rect.top = width - paused_rect.width - 10, 10

                        music_plus_image_rect.left, music_plus_image_rect.top = width - music_plus_image_rect.width - 10, 80  # 控制音量大小的按钮
                        music_less_image_rect.left, music_less_image_rect.top = width - music_less_image_rect.width - 10, 150
                        music_mute_image_rect.left, music_mute_image_rect.top = width - music_mute_image_rect.width - 10, 220
                        sounds_mute_image_rect.left, sounds_mute_image_rect.top = width - sounds_mute_image_rect.width - 20, 290

                        me=king.King(bg_size)

                        bullet2_supply = supply.Bullet2_Supply(bg_size)
                        bullet3_supply = supply.Bullet3_Supply(bg_size)
                        bullet4_supply = supply.Bullet4_Supply(bg_size)
                        bomb_supply = supply.Bomb_Supply(bg_size)
                        life_supply = supply.Life_Supply(bg_size)
                        bg_hb_supply = supply.Bg_Hb_Supply(bg_size)
                        change_k_supply = supply.Change_K_Supply(bg_size)

            elif event.type == SUPPLY1_TIME:   #发放补给 #choice([True, False])
                supply_sound.play()
                bullet2_supply.reset()
            elif event.type == SUPPLY2_TIME:
                supply_sound.play()
                bullet3_supply.reset()
            elif event.type == SUPPLY3_TIME:
                supply_sound.play()
                bomb_supply.reset()
            elif event.type == SUPPLY4_TIME:
                supply_sound.play()
                bullet4_supply.reset()
            elif event.type == SUPPLY5_TIME:
                supply_sound.play()
                life_supply.reset()
            elif event.type == SUPPLY6_TIME:
                supply_sound.play()
                bg_hb_supply.reset()

                supply_sound.play()
                change_k_supply.reset()
            elif event.type == SUPER_BULLET_TIME:   #超级子弹时间到了，将子弹变为普通子弹
                is_bullet=1
                pygame.time.set_timer(SUPER_BULLET_TIME, 0)

            elif event.type == INVINCIBLE_TIME:   #白大王无敌状态时间结束
                me.invincible = False
                pygame.time.set_timer(INVINCIBLE_TIME, 0)

        if not pygame.mixer.music.get_busy() and life_num!=0 and not music_mute:  # 判断音乐是否播放完
            music_num = (music_num + 1) % 8
            # pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load(musics[music_num])
            pygame.mixer.music.set_volume(music_volume)
            pygame.mixer.music.play(1)

        # 根据用户的得分增加难度
        if level == 1 and score > 50000:
            level = 2
            upgrade_sound.play()
            # 增加3架小型敌机、2架中型敌机和1架大型敌机
            add_small_enemies(small_enemies, enemies, 3,bg_size)
            add_mid_enemies(mid_enemies, enemies, 2,bg_size)
            add_big_enemies(big_enemies, enemies, 1,bg_size)
            # 提升小型敌机的速度
            inc_speed(small_enemies, 1)
        elif level == 2 and score > 300000:
            level = 3
            upgrade_sound.play()
            # 增加5架小型敌机、3架中型敌机和2架大型敌机
            add_small_enemies(small_enemies, enemies, 5,bg_size)
            add_mid_enemies(mid_enemies, enemies, 3,bg_size)
            add_big_enemies(big_enemies, enemies, 2,bg_size)
            # 提升小型敌机的速度
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        elif level == 3 and score > 600000:
            level = 4
            upgrade_sound.play()
            # 增加5架小型敌机、3架中型敌机和2架大型敌机
            add_small_enemies(small_enemies, enemies, 5,bg_size)
            add_mid_enemies(mid_enemies, enemies, 3,bg_size)
            add_big_enemies(big_enemies, enemies, 2,bg_size)
            # 提升小型敌机的速度
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)
        elif level == 4 and score > 1000000:
            level = 5
            upgrade_sound.play()
            # 增加5架小型敌机、3架中型敌机和2架大型敌机
            add_small_enemies(small_enemies, enemies, 5,bg_size)
            add_mid_enemies(mid_enemies, enemies, 3,bg_size)
            add_big_enemies(big_enemies, enemies, 2,bg_size)
            # 提升小型敌机的速度
            inc_speed(small_enemies, 1)
            inc_speed(mid_enemies, 1)

        screen.blit(background, (0, 0))
        if life_num and not paused:
            # 检测用户的键盘操作
            key_pressed = pygame.key.get_pressed()
            # 控制白大王上下左右移动
            if key_pressed[K_w] or key_pressed[K_UP]:
                me.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRight()

            # 绘制全屏炸弹补给并检测是否获得
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply, me):
                    get_bomb_sound.play()
                    bomb_num += 1
                    bomb_supply.active = False

            # 绘制子弹补给并检测是否获得
            if bullet2_supply.active:
                bullet2_supply.move()
                screen.blit(bullet2_supply.image, bullet2_supply.rect)
                if pygame.sprite.collide_mask(bullet2_supply, me):
                    get_bullet_sound.play()
                    is_bullet = 2
                    pygame.time.set_timer(SUPER_BULLET_TIME, 18 * 1000)  #设置子弹时间
                    bullet2_supply.active = False

            if bullet3_supply.active:
                bullet3_supply.move()
                screen.blit(bullet3_supply.image, bullet3_supply.rect)
                if pygame.sprite.collide_mask(bullet3_supply, me):
                    get_bullet_sound.play()
                    is_bullet = 3
                    pygame.time.set_timer(SUPER_BULLET_TIME, 18 * 1000)
                    bullet3_supply.active = False

            if bullet4_supply.active:
                bullet4_supply.move()
                screen.blit(bullet4_supply.image, bullet4_supply.rect)
                if pygame.sprite.collide_mask(bullet4_supply, me):
                    get_bullet_sound.play()
                    is_bullet = 4
                    pygame.time.set_timer(SUPER_BULLET_TIME, 18 * 1000)
                    bullet4_supply.active = False

            if life_supply.active:
                life_supply.move()
                screen.blit(life_supply.image, life_supply.rect)
                if pygame.sprite.collide_mask(life_supply, me):
                    get_bullet_sound.play()
                    life_num+=1
                    life_supply.active = False

            if change_k_supply.active:
                change_k_supply.move()
                screen.blit(change_k_supply.image,change_k_supply.rect)
                if pygame.sprite.collide_mask(change_k_supply, me):
                    get_bullet_sound.play()
                    change_k_supply.active = False
                    change_me=not change_me


            if bg_hb_supply.active:
                bg_hb_supply.move()
                if bg_index == 0:
                    screen.blit(bg_hb_supply.image, bg_hb_supply.rect)
                elif bg_index == 1:
                    screen.blit(bg_hb_supply.image1, bg_hb_supply.rect)
                elif bg_index == 2:
                    screen.blit(bg_hb_supply.image2, bg_hb_supply.rect)
                elif bg_index == 3:
                    screen.blit(bg_hb_supply.image3, bg_hb_supply.rect)
                elif bg_index == 4:
                    screen.blit(bg_hb_supply.image4, bg_hb_supply.rect)
                elif bg_index == 5:
                    screen.blit(bg_hb_supply.image5, bg_hb_supply.rect)
                elif bg_index == 6:
                    screen.blit(bg_hb_supply.image6, bg_hb_supply.rect)
                if bg_hb_supply.active==False:
                    bg_index=(bg_index+1)%7

                if pygame.sprite.collide_mask(bg_hb_supply, me):
                    get_bullet_sound.play()
                    bg_hb_supply.active = False
                    if bg_index==0:
                        obg=bg_image
                    elif bg_index==1:
                        obg=bg_image1
                    elif bg_index==2:
                        obg=bg_image2
                    elif bg_index == 3:
                        obg = bg_image3
                    elif bg_index == 4:
                        obg = bg_image4
                    elif bg_index == 5:
                        obg = bg_image5
                    elif bg_index == 6:
                        obg = bg_image6
                    bg_index=(bg_index+1)%7
                    background = pygame.transform.scale(obg, bg_size)

            # 发射子弹
            if not (delay % 10):
                bullet_sound.play()
                if is_bullet == 1:
                    bullets = bullet1
                    bullets[bullet1_index].reset(me.rect.midtop)
                    bullet1_index = (bullet1_index + 1) % BULLET1_NUM

                elif is_bullet==2:
                    bullets = bullet2
                    bullets[bullet2_index].reset((me.rect.centerx - 33, me.rect.centery))
                    bullets[bullet2_index + 1].reset((me.rect.centerx + 30, me.rect.centery))
                    bullet2_index = (bullet2_index + 2) % BULLET2_NUM

                elif is_bullet == 3:
                    bullets = bullet3
                    bullets[bullet3_index].reset((me.rect.centerx - 33, me.rect.centery))
                    bullets[bullet3_index + 1].reset((me.rect.centerx + 30, me.rect.centery))
                    bullets[bullet3_index+2].reset((me.rect.centerx - 10, me.rect.centery))
                    bullets[bullet3_index + 3].reset((me.rect.centerx + 10, me.rect.centery))
                    bullet3_index = (bullet3_index + 4) % BULLET3_NUM

                elif is_bullet == 4:
                    bullets = bullet4
                    for i in range(8):
                        bullets[bullet4_index1].reset((me.rect.centerx, me.rect.centery))
                        bullet4_index1 = (bullet4_index1 + 1) % BULLET4_NUM

            # 检测子弹是否击中敌机
            for b in bullets:
                if b.active :
                    if b in bullet4:
                        b.width = bg_size[0]
                        b.height = bg_size[1]
                       # b.index = bullet4_index2
                        b.move(bullet4_index2)
                        bullet4_index2=(bullet4_index2+1)%8
                        #bullet4_index2 = (bullet4_index2 + 1) % BULLET4_NUM
                    else:
                        b.move()

                    screen.blit(b.image, b.rect)  #绘制子弹
                    enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        #bullet4_index2 = (bullet4_index2 + 1) % 8

                        for e in enemy_hit:
                            if e in mid_enemies or e in big_enemies:
                                e.hit = True
                                e.energy -= 1
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False
                else:
                    bullet4_index2=(bullet4_index2+1)%8
            # 绘制大型敌机
            for each in big_enemies:
                if each.active:
                    each.width = bg_size[0]
                    each.height = bg_size[1]
                    each.move()
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        if switch_image:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)

                    # 绘制血槽
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.right, each.rect.top - 5), \
                                     2)
                    # 当生命大于20%显示绿色，否则显示红色
                    energy_remain = each.energy / face.BigEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, \
                                      each.rect.top - 5), 2)

                    # 即将出现在画面中，播放音效
                    if each.rect.bottom == -50:
                        enemy3_fly_sound.play(-1)
                else:
                    # 毁灭
                    if not (delay % 3):
                        if e3_destroy_index == 0:
                            enemy3_down_sound.play()
                        screen.blit(each.destroy_images[e3_destroy_index], each.rect)
                        e3_destroy_index = (e3_destroy_index + 1) % 6
                        if e3_destroy_index == 0:
                            enemy3_fly_sound.stop()
                            score += 10000
                            each.width = bg_size[0]
                            each.height = bg_size[1]
                            each.reset()

            # 绘制中型敌机：
            for each in mid_enemies:
                if each.active:
                    each.width = bg_size[0]
                    each.height = bg_size[1]
                    each.move()

                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        if switch_image:
                            screen.blit(each.image[mid_enemies_index1], each.rect)
                            mid_enemies_index1 = (mid_enemies_index1 + 1) % 7
                        else:
                            screen.blit(each.image[mid_enemies_index2], each.rect)
                            mid_enemies_index2 = (mid_enemies_index2 + 1) % 14
                            if mid_enemies_index2==0:
                                mid_enemies_index2+=7

                    # 绘制血槽
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.right, each.rect.top - 5), \
                                     2)
                    # 当生命大于20%显示绿色，否则显示红色
                    energy_remain = each.energy / face.MidEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color, \
                                     (each.rect.left, each.rect.top - 5), \
                                     (each.rect.left + each.rect.width * energy_remain, \
                                      each.rect.top - 5), 2)
                else:
                    # 毁灭
                    if not (delay % 3):
                        if e2_destroy_index == 0:
                            enemy2_down_sound.play()
                        screen.blit(each.destroy_images[e2_destroy_index], each.rect)
                        e2_destroy_index = (e2_destroy_index + 1) % 4
                        if e2_destroy_index == 0:
                            score += 6000
                            each.width = bg_size[0]
                            each.height = bg_size[1]
                            each.reset()
            mid_enemies_index1=0
            mid_enemies_index2=7

            # 绘制小型敌机：
            for each in small_enemies:
                if each.active:
                    each.width = bg_size[0]
                    each.height= bg_size[1]
                    each.move()
                    screen.blit(each.image[small_enemies_index1],each.rect)
                    small_enemies_index1 = (small_enemies_index1 + 1) % 24
                else:
                    # 毁灭
                    enemy1_down_sound.play()
                    #if not (delay % 3):
                   #     screen.blit(each.destroy_images, each.rect)
                    score += 1000
                    small_enemies_index1 = (small_enemies_index1 + 1) % 24
                    each.width = bg_size[0]
                    each.height = bg_size[1]
                    each.reset()

            small_enemies_index1=0


            # 检测我方飞机是否被撞
            enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
            if enemies_down and not me.invincible:
                me.active = False
                for e in enemies_down:
                    e.active = False

            # 绘制我方飞机
            if me.active:
                if switch_image:
                    if change_me:
                        screen.blit(me.image1,me.rect)
                    else:
                        screen.blit(me.image3,me.rect)
                else:
                    if change_me:
                        screen.blit(me.image2, me.rect)
                    else:
                        screen.blit(me.image4,me.rect)
            else:
                # 毁灭
                if not (delay % 5):
                    if me_destroy_index == 0:
                        me_down_sound.play()
                    if change_me:
                        screen.blit(me.destroy_images[me_destroy_index], me.rect)
                        me_destroy_index = (me_destroy_index + 1) % 4
                    else:
                        screen.blit(me.destroy_images1[me_destroy_index], me.rect)
                        me_destroy_index = (me_destroy_index + 1) % 4
                    if me_destroy_index == 0:
                        life_num -= 1
                        me.reset()
                        pygame.time.set_timer(INVINCIBLE_TIME, 3 * 1000)

            # 绘制全屏炸弹数量
            bomb_text = bomb_font.render("× %d" % bomb_num, True, WHITE)
            text_rect = bomb_text.get_rect()
            screen.blit(bomb_image, (10, height - 10 - bomb_rect.height))
            screen.blit(bomb_text, (20 + bomb_rect.width, height - 5 - text_rect.height))

            # 绘制剩余生命数量
            if life_num:
                for i in range(life_num):
                    screen.blit(life_image, \
                                (width - 10 - (i + 1) * life_rect.width, \
                                 height - 10 - life_rect.height))

            # 绘制得分
            score_text = score_font.render("Score : %s" % str(score), True, WHITE)
            screen.blit(score_text, (10, 5))

        # 绘制游戏结束画面
        elif life_num == 0:
            # 背景音乐停止
            pygame.mixer.music.stop()

            # 停止全部音效
            pygame.mixer.stop()

            # 停止发放补给
            pygame.time.set_timer(SUPPLY1_TIME, 0)
            pygame.time.set_timer(SUPPLY2_TIME, 0)
            pygame.time.set_timer(SUPPLY3_TIME, 0)
            pygame.time.set_timer(SUPPLY4_TIME, 0)
            pygame.time.set_timer(SUPPLY5_TIME, 0)
            pygame.time.set_timer(SUPPLY6_TIME, 0)
            if not recorded:
                recorded = True
                # 读取历史最高得分
                with open("record.txt", "r") as f:
                    record_score = int(f.read())

                # 如果玩家得分高于历史最高得分，则存档
                if score > record_score:
                    with open("record.txt", "w") as f:
                        f.write(str(score))

            # 绘制结束画面
            record_score_text = score_font.render("Best : %d" % record_score, True, (255, 255, 255))
            screen.blit(record_score_text, (50, 50))

            gameover_text1 = gameover_font.render("Your Score", True, (255, 255, 255))  ##有错误，，，，，
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top = \
                (width - gameover_text1_rect.width) // 2, height // 3
            screen.blit(gameover_text1, gameover_text1_rect)

            gameover_text2 = gameover_font.render(str(score), True, (255, 255, 255))
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left, gameover_text2_rect.top = \
                (width - gameover_text2_rect.width) // 2, \
                gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2, gameover_text2_rect)

            again_rect.left, again_rect.top = \
                (width - again_rect.width) // 2, \
                gameover_text2_rect.bottom + 50
            screen.blit(again_image, again_rect)

            gameover_rect.left, gameover_rect.top = \
                (width - again_rect.width) // 2, \
                again_rect.bottom + 10
            screen.blit(gameover_image, gameover_rect)

            # 检测用户的鼠标操作
            # 如果用户按下鼠标左键
            if pygame.mouse.get_pressed()[0]:
                # 获取鼠标坐标
                pos = pygame.mouse.get_pos()
                # 如果用户点击“重新开始”
                if again_rect.left < pos[0] < again_rect.right and \
                        again_rect.top < pos[1] < again_rect.bottom:
                    # 调用main函数，重新开始游戏
                    main()
                # 如果用户点击“结束游戏”
                elif gameover_rect.left < pos[0] < gameover_rect.right and \
                        gameover_rect.top < pos[1] < gameover_rect.bottom:
                    # 退出游戏
                    pygame.quit()
                    sys.exit()
                    # 绘制暂停按钮



        screen.blit(paused_image, paused_rect)
        screen.blit(music_plus_image,music_plus_image_rect)
        screen.blit(music_less_image,music_less_image_rect)
        screen.blit(music_mute_image,music_mute_image_rect)
        screen.blit(sounds_mute_image, sounds_mute_image_rect)
        screen.blit(music_image,music_image_rect)


        # 切换图片
        if not (delay % 20):
            switch_image = not switch_image    #控制敌方图片转变时间

        delay -= 1
        if not delay:
            delay = 100

        pygame.display.flip()
        clock.tick(60)



if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
