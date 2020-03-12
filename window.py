import pygame
pygame.init()

import random

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

class Car(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        width = 22
        length = 40
        colour = RED
        self.image = self.get_image(width, length)
        pygame.draw.rect(self.image, colour, [0, 0, width, length])
        self.rect = self.image.get_rect()

    def get_image(self, width, length):
        image = pygame.Surface([width, length])
        image.fill(WHITE)
        image.set_colorkey(WHITE)
        return image


class Window:
    def __init__(self):
        self.running = True
        self.full = False
        self.size = (600, 400)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Car Parking")
        self.screen.fill(WHITE)
        self.all_sprites_list = pygame.sprite.Group()

    def add_car(self, new_car):
        random_coords = (random.randrange(0, self.size[0]), random.randrange(0, self.size[1]))
        new_car.rect.x, new_car.rect.y = random_coords
        iterations = 0
        while len(pygame.sprite.spritecollide(new_car, self.all_sprites_list, dokill= False)) != 0:
            random_coords = (random.randrange(0, self.size[0]), random.randrange(0, self.size[1]))
            new_car.rect.x, new_car.rect.y = random_coords
            if iterations > 10000:
                return False
            iterations += 1
        return True

    def loop(self):
        clock=pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if self.full == False:
                new_car = Car()
                if self.add_car(new_car):
                    self.all_sprites_list.add(new_car)
                else:
                    self.full == True

            self.all_sprites_list.update()
            self.all_sprites_list.draw(self.screen)

            pygame.display.flip()
            clock.tick(60)
 
if __name__ == "__main__":
    window = Window()
    window.loop()
    pygame.quit()
    



