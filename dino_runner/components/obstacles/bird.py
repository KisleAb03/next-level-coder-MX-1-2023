import random
from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    BIRD_HEIGTHS = [250, 290, 320]

    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.BIRD_HEIGTHS)
        self.index = 0
    

    def draw(self, screen):

    #resetea el valor de el index a 0 cuando llega a 10
        if self.index >= 10:
            self.index = 0
    ## por los primeros 5 tiempos la funcion draw llama la primera imagen del pajaro
        screen.blit(self.image[self.index//5], self.rect)
        self.index += 1
