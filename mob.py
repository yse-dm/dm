import pygame                   #　pygameのインポート
from pygame.locals import *     #　pygameで定義済みの定数
from random import randint      #乱数の生成用
from random import choice

class Mob(pygame.sprite.Sprite):
    #　コンストラクタ
    def __init__(self, imagelist, x = 0, y = 0, width = 32, height = 32, speed = 8,shotcount = 40):
        super().__init__()
        self.imagelist = imagelist
        self.image = pygame.image.load(self.imagelist[0])
        self.rect = pygame.Rect(x, y, width, height)
        self.setcount()     #下のフレームカウンタの処理
        self.speed = speed
        self.shotcount = shotcount

    #フレームカウンタ
    def setcount(self,count=0):
        self.count = count

    def setshot(self,shotlist):
        self.shotlist = shotlist 

    #　更新用関数
    def update(self):
        #アニメーション処理
        self.count += 1
        if self.count == 20:
            self.image = pygame.image.load(self.imagelist[1])
        if self.count == 40:
            self.image = pygame.image.load(self.imagelist[0])
            self.setcount()
        
          #　落下処理
        self.rect.move_ip(0,self.speed)
        if self.rect.y > 480:
            num = randint(0,10)
            self.rect.y = num * -64
            self.rect.x = 64 * num

        if self.count % self.shotcount == 0:
            for shot in self.shotlist:
                if shot.rect.y > 480:
                    shot.rect.x = self.rect.x + self.rect.width // 2 -16
                    shot.rect.y = self.rect.y + self.rect.height
                    break