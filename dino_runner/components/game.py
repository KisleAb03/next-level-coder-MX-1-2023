import pygame
import random

from dino_runner.utils.constants import (
    BG,
    CLOUD,
    ICON,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
    FPS,
    FONT_ARIAL)


from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.player_hearts.heart_manager import HeartManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = SCREEN_WIDTH + random.randint(800, 1000)
        self.y_pos_cloud = random.randint(50, 100)
        

        self.bullets = []
        self.bullet_count = 0
        
        self.death_count = 0

        
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.heart_manager = HeartManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        pygame.mixer.music.load('dino_runner/assets/Sounds/game_sound.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

        
    
    def increase_score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        if self.points % 1000 == 0:
            pygame.mixer.music.load('dino_runner/assets/Sounds/thousand_points.wav')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(1.0)

        self.player.check_invincibility()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.playing = False


    def update(self):
        pygame.mixer.music.load('dino_runner/assets/Sounds/game_sound.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)
        user_input = pygame.key.get_pressed()
        
        self.change_screen_color()
        self.player.update(user_input, self.screen)
        self.update_bullets()
        self.obstacle_manager.update(self.game_speed, self)
        
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        self.increase_score()

    def draw(self):
        self.clock.tick(FPS)
        
        self.draw_background()
        self.draw_cloud()
        self.player.draw(self.screen)
        
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.power_up_manager.draw(self.screen)
        self.heart_manager.draw(self.screen)
        
        pygame.display.update()
        pygame.display.flip()
       

    def change_screen_color(self):
        color = (255, 255, 255) if (pygame.time.get_ticks() // 1000) % 30 < 15 else (0, 0, 0)
        self.screen.fill(color)
        

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def draw_cloud(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
        self.x_pos_cloud -= self.game_speed
        if self.x_pos_cloud <= -image_width:
            self.x_pos_cloud = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y_pos_cloud = random.randint(50, 100)

    def draw_score(self):
        font = pygame.font.Font(FONT_ARIAL, 23)
        surface = font.render( "Points: " + str(self.points), True, (0, 187, 45))
        rect = surface.get_rect()
        rect.x = 950
        rect.y = 10
        self.screen.blit(surface, rect)

    def update_bullets(self):# metodo actualiza balas y las elimina cuando salen de la pantalla
        for bullet in self.bullets:
            bullet.update()  
            if bullet.rect.right < 0:  
                self.bullets.remove(bullet)

    
        
    