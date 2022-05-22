import pygame       #　インポート
from pygame.locals import *     #　pygameで定義済みの定数
import random

class Motion(pygame.sprite.Sprite):
    #　コンストラクタ
    def __init__(self, imagelist, x = 0, y = 0, width = 64, height = 64):
        super().__init__()
        self.imagelist = imagelist
        self.image = pygame.image.load(self.imagelist)
        self.rect = pygame.Rect(x, y, width, height)
        self.setcount()     #下のフレームカウンタの処理

    #フレームカウンタ
    def setcount(self,count=0):
        self.count = count

    #ショットとの関連付け
    def setshot(self,shotlist):
        self.shotlist = shotlist        #ショットのインスタンス情報

    #　更新用関数
    def update(self):
        self.rect.move_ip(-16, 0)
        if self.rect.x < -64:
            num1 = random.randint(0,6)
            num2 = random.randint(0,15)
            self.rect.y = num1 * 64
            self.rect.x = 800 + 64 * num2