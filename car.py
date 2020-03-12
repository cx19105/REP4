from colours import *
import pygame

class Car(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.width = 22
        self.length = 40
        colour = RED
        self.image = self.get_image(self.width, self.length)
        pygame.draw.rect(self.image, colour, [0, 0, self.width, self.length])
        self.rect = self.image.get_rect()

    def get_image(self, width, length):
        image = pygame.Surface([width, length])
        image.fill(WHITE)
        image.set_colorkey(WHITE)
        return image