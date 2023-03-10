import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import BULLET, SCREEN_WIDTH, BULLET_SPEED

class Bullet(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = BULLET
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    
    def update(self):
        self.rect.x += BULLET_SPEED
        if self.rect.right > SCREEN_WIDTH:
            self.kill()
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)