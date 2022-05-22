import pygame   #インポート

class Display(pygame.sprite.Sprite):
    #コンストラクタ
    def __init__(self, image,x = 0, y = 0,width = 640,height = 640):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = pygame.Rect(x,y,width,height)       #左上の座標,右にいくつか,下にいくつかというようにパラメータは書く　　二点の座標を書くのではない
    #更新用関数
    def update(self):
        pass