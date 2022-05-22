import pygame       #　インポート

class Back(pygame.sprite.Sprite):
    #　コンストラクタ
    def __init__(self, image, x = 0, y = 0, width = 640, height = 640):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = pygame.Rect(x, y, width, height)
    #　更新用関数
    def update(self):
        #self.rect.x += 4
        #if self.rect.x % 640 == 0:
        #    self.rect.x -= 640
        pass
    