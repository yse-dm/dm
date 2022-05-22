import pygame                   #　pygameのインポート
from pygame.locals import *     #　pygameで定義済みの定数
from random import randint      #乱数の生成用
from random import choice
import math

class Beacon(pygame.sprite.Sprite):
    #　コンストラクタ
    def __init__(self, imagelist, x = 0, y = 0, width = 32, height = 32, speed = -8):
        super().__init__()
        self.imagelist = imagelist
        self.image = pygame.image.load(self.imagelist)
        self.rect = pygame.Rect(x, y, width, height)
        self.setcount()     
        self.speed = speed
        self.radian = 0

    #フレームカウンタ
    def setcount(self,count=0):
        self.count = count

    #　更新用関数
    def update(self):
        self.radian += 2 * math.pi / 100
        self.rect.x = 250 + 128 * math.cos(self.radian)
        self.rect.y = 128 - 128 * math.sin(self.radian)
