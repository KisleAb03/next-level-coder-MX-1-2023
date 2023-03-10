import pygame
import random
from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import (
    SMALL_CACTUS,
    LARGE_CACTUS,
    BIRD)

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        pygame.mixer.music.load('dino_runner/assets/Sounds/loss_live.wav')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.3)
    
    def update(self, game_speed, game):

        if len(self.obstacles) == 0:
            if random.randint(0,2) == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0,2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0,2) == 2:
                self.obstacles.append(Bird(BIRD))
    
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                if  not game.player.shield and not game.player.hammer:

                    game.heart_manager.reduce_heart()
                    

                if game.heart_manager.heart_count < 1:
                    pygame.time.delay(300)
                    game.playing = False
                    break
                
                else:
                    self.obstacles.remove(obstacle)
                    
            for bullet in game.bullets:
                if obstacle.rect.colliderect(bullet.rect):
                    game.score += 1
                    game.obstacles.remove(obstacle)
                    game.bullets.remove(bullet)
                    break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
