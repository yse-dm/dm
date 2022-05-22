import pygame       #　インポート

class Shot(pygame.sprite.Sprite):
    #　コンストラクタ
    def __init__(self, image, x = 0, y = 0, width = 16, height = 16,speed = 8):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
    #　更新用関数
    def update(self):
        self.rect.move_ip(0, -(self.speed))
        if self.rect.y < -64:
            self.rect.x = 640