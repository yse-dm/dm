import pygame       #　インポート
from pygame.locals import *     #　pygameで定義済みの定数

class Lock(pygame.sprite.Sprite):
    #　コンストラクタ
    def __init__(self, image, x = 0, y = 0, width = 64, height = 64):
        super().__init__()
        self.image = image
        self.image = pygame.image.load(self.image)
        self.rect = pygame.Rect(x, y, width, height)
        self.setcount()     #下のフレームカウンタの処理

    #フレームカウンタ
    def setcount(self,count=0):
        self.count = count

    #def setlock(self,m_x,m_y):
       # self.rect.x = m_x
        #self.rect.y = m_y

    #　更新用関数
    def update(self):
        pass
        """for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                M_x,M_y = event.pos
                M_x -= 16
                M_y -= 16
                self.rect.x = M_x
                self.rect.y = M_y"""