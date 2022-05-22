import pygame       #　インポート
from pygame.locals import *     #　pygameで定義済みの定数

class Player(pygame.sprite.Sprite):
    #　コンストラクタ
    def __init__(self, imagelist, x = 0, y = 0, width = 32, height = 32,atack = 1,life = 10,speed = 10,shotcount = 8):
        super().__init__()
        self.imagelist = imagelist
        self.image = pygame.image.load(self.imagelist[0])
        self.rect = pygame.Rect(x, y, width, height)
        self.life = life
        self.atack = atack
        self.speed = speed
        self.shotcount = shotcount
        self.image_a = pygame.image.load(self.imagelist[0])
        self.setcount()     #下のフレームカウンタの処理
        self.life_max = life

    #初期化関数
    def init(self):
        self.life = 10
        self.rect.x = 288

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
            self.image_a = pygame.image.load(self.imagelist[1])
        if self.count == 40:
            self.image = pygame.image.load(self.imagelist[0])
            self.image_a = pygame.image.load(self.imagelist[0])
            self.setcount() 

        #ライフチェック処理
        if self.life <= 0:
            return          #if文でreturnにひっかかれば下の移動処理は行われない

        #　キー入力に対応する
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT] == False and pressed[K_RIGHT] == False:
            self.image = self.image_a
        if pressed[K_LEFT] and self.rect.x > 0:
            self.rect.move_ip(-(self.speed), 0)
            self.image = pygame.image.load(self.imagelist[2])
        if pressed[K_RIGHT] and self.rect.x < 608:
            self.rect.move_ip(+(self.speed), 0)
            self.image = pygame.image.load(self.imagelist[3])
        if pressed[K_UP] and self.rect.y > 0:
            self.rect.move_ip(0, -(self.speed))
        if pressed[K_DOWN] and self.rect.y < 446:
            self.rect.move_ip(0, +(self.speed))
        if pressed[K_SPACE] and self.count % self.shotcount == 0:
            for shot in self.shotlist:
                if shot.rect.y < -64:
                    shot.rect.x = self.rect.x + 8
                    shot.rect.y = self.rect.y
                    break
