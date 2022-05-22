import pygame                   #　pygameのインポート
from pygame.locals import *     #　pygameで定義済みの定数
from random import randint      #乱数の生成用
from random import choice
class Boss(pygame.sprite.Sprite):
    #　コンストラクタ
    def __init__(self, imagelist, x = 0, y = 0, life = 50, width = 128, height = 128, speed = 4, atacktime = 10,bossmove = 0):
        super().__init__()
        self.imagelist = imagelist
        self.image = pygame.image.load(self.imagelist[0])
        self.rect = pygame.Rect(x, y, width, height)
        self.setcount()     #下のフレームカウンタの処理
        self.speed = speed
        self.atacktime = atacktime
        self.life = life
        self.bossmove = bossmove
        self.movechoice = 1
        self.atackchoice = 1

    #フレームカウンタ
    def setcount(self,count=0):
        self.count = count

    def setshot2(self,bossshotlist):
        self.bossshotlist = bossshotlist

    #　更新用関数
    def update(self):
        global movechoice
        bossmovelist = [1,2,3,4,5]
        #アニメーション処理
        self.count += 1
        if self.count == 20:
            self.image = pygame.image.load(self.imagelist[1])
        if self.count == 40:
            self.image = pygame.image.load(self.imagelist[0])
            self.setcount()
        
        self.bossmove +=1
        if self.bossmove % 30 == 0:
            self.movechoice = choice(bossmovelist)
            self.atackchoice = choice(bossmovelist)
            print(self.movechoice)
            self.bossmove = 0
        
        if self.rect.y < (0 + 32) and self.life > 0:
            self.rect.move_ip(0, +4)

        if self.life <= 0:
            self.rect.move_ip(0, -4)

        if self.rect.y >= 32:
            if self.movechoice == 1 and self.rect.x > 0:
                self.rect.move_ip(-(self.speed), 0)
            if self.movechoice == 3 and self.rect.x > 0:
                self.rect.move_ip(-(self.speed), 0)
            if self.movechoice == 2 and self.rect.x < 392:
                self.rect.move_ip(+(self.speed), 0)
            if self.movechoice == 4 and self.rect.x < 392:
                self.rect.move_ip(+(self.speed), 0)
            if self.movechoice == 4:
                pass
        
        if self.life > 0:
            if self.count % self.atacktime == 0 and self.atackchoice in [1, 2, 3]:
                for shot in self.bossshotlist:
                    if shot.rect.y > 480:
                        shot.rect.x = self.rect.x + self.rect.width // 2 -16
                        shot.rect.y = self.rect.y + self.rect.height
                        break
            """if self.count % self.atacktime == 0 and self.atackchoice == 2:
                for shot in self.bossshotlist:
                    if shot.rect.y > 480:
                        shot.rect.x = self.rect.x + self.rect.width // 2 - 16
                        shot.rect.y = self.rect.y + self.rect.height
                        break
            if self.count % self.atacktime == 0 and self.atackchoice == 3:
                for shot in self.bossshotlist:
                    if shot.rect.y > 480:
                        shot.rect.x = self.rect.x + self.rect.width // 2 - 16
                        shot.rect.y = self.rect.y + self.rect.height
                        break"""