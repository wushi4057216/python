import time
import pygame
from pygame.locals import *
import random

class BassPlane(object):
    def __init__(self, screen_temp,x,y,image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)
        self.bullet_list = []

    def disply(self):
        self.screen.blit(self.image,(self.x, self.y))
        for bullet in self.bullet_list:
            bullet.disply()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)

class BassBullet(object):
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)
    def disply(self):
        self.screen.blit(self.image,(self.x, self.y))

class HeroPlane(BassPlane):
    '''英雄的类'''
    def __init__(self, screen_temp):
        BassPlane.__init__(self,screen_temp,210,720,"./hero.png")

    def move_left(self):
        self.x -= 5
    def move_right(self):
        self.x += 5
    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))


class EnemyPlane(BassPlane):
    '''敌人的类'''
    def __init__(self, screen_temp):
        BassPlane.__init__(self, screen_temp, 200, 0, "./enemy.png")
        self.direm = "right"

    def move(self):
        if self.direm == "right":
            self.x += 10
        elif self.direm == "left":
            self.x -= 10
        if self.x > 430:
            self.direm = "left"
        elif self.x < 0:
            self.direm = "right"

    def fire(self):
        random_temp = random.randint(0,100)
        if random_temp == 10 or random_temp == 20:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))


class Bullet(BassBullet):
    '''子弹的类'''
    def __init__(self, screen_temp, x, y):
        BassBullet.__init__(self, screen_temp, x+40, y-20, "./bullet.png")

    def move(self):
        self.y -= 11
    def judge(self):
        if self.y <= 200:
            return True
        else:
            return False
class EnemyBullet(BassBullet):
    '''子弹的类'''
    def __init__(self, screen_temp, x, y):
        BassBullet.__init__(self, screen_temp, x+25, y+40, "./bullet.png")

    def move(self):
        self.y += 11
    def judge(self):
        if self.y >= 800:
            return True
        else:
            return False

def key_control(hero_temp):
    '''按键的类
    #获取按键事件，比如按键等'''
    for event in pygame.event.get():
        #判断是否点击了退出按钮
        if event.type ==QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()

def main():
    #创建窗口
    screen = pygame.display.set_mode((480,860),0,32)
    #创建一个背景图
    background = pygame.image.load("./beiy.png")
    #创建一个飞机对象
    hero = HeroPlane(screen)
    #程序循环执行
    enemy = EnemyPlane(screen)
    while True:
        screen.blit(background,(0,0))
        hero.disply()
        enemy.disply()
        enemy.move()
        enemy.fire()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.02)

if __name__ == '__main__':
    main()