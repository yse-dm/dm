import pygame                   #　pygameのインポート
from pygame.locals import *     #　pygameで定義済みの定数
from random import randint      #乱数の生成用

class Enemy02(pygame.sprite.Sprite):
    #　コンストラクタ
    def __init__(self, imagelist, x = 0, y = 0, width = 64, height = 64):
        super().__init__()
        self.imagelist = imagelist
        self.image = pygame.image.load(self.imagelist[0])
        self.rect = pygame.Rect(x, y, width, height)
        self.setcount()     #下のフレームカウンタの処理

    #フレームカウンタ
    def setcount(self,count=0):
        self.count = count

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
        self.rect.move_ip(-4, 0)
        if self.rect.x < -64:
            num = randint(0,6)
            self.rect.y = num * 64
            self.rect.x = 800 + 64 * num