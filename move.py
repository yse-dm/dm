import pygame       #　インポート
from pygame.locals import *     #　pygameで定義済みの定数

class Move(pygame.sprite.Sprite):
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

    #ショットとの関連付け
    def setshot(self,shotlist):
        self.shotlist = shotlist        #ショットのインスタンス情報

    #　更新用関数
    def update(self):
        #アニメーション処理
        self.count += 1
        if self.count == 20:
            self.image = pygame.image.load(self.imagelist[1])
        if self.count == 40:
            self.image = pygame.image.load(self.imagelist[0])
            self.setcount() 