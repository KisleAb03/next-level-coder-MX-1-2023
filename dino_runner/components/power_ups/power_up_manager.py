import random
import pygame 
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.points = 0
        self.when_appears = 0
        self.option_numbers = list(range(1, 10))   

    def generate_power_ups(self, points):
        self.points = points
        power_up_type = random.randint(0,1)

        if len(self.power_ups) == 0:
            if power_up_type == 0:
                if self.when_appears == self.points:
                    print("genrating power up")
                    self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                    self.power_ups.append(Shield())
            elif power_up_type == 1:
                if self.when_appears == self.points:
                    print("genrating power up")
                    self.when_appears = random.randint(self.when_appears + 200, 500 + self.when_appears)
                    self.power_ups.append(Hammer())
                
        return self.power_ups

    def update(self, points, game_speed, player):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                if power_up.type == SHIELD_TYPE:
                    player.shield = True
                    pygame.mixer.music.load('dino_runner/assets/Sounds/shield.wav')
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.load('dino_runner/assets/Sounds/game_sound.wav')
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.3)
                else:
                    player.hammer = True
                    pygame.mixer.music.load('dino_runner/assets/Sounds/hammer.wav')
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.load('dino_runner/assets/Sounds/game_sound.wav')
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.3)

                player.type = power_up.type
                start_time = pygame.time.get_ticks()
                time_random = random.randrange(5, 8)
                player.power_ups_time_up = start_time + (time_random * 1000)
                self.power_ups.remove(power_up)

                

        
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
