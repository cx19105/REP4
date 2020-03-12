import pygame, random
from car import Car
from colours import *

pygame.init()

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


class Window:
    def __init__(self):
        self.running = True
        self.full = False
        self.parking_area = (500, 500)
        self.size = [x+100 for x in self.parking_area]
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Car Parking")
        self.screen.fill(WHITE)
        self.all_sprites_list = pygame.sprite.Group()

    def add_car(self, new_car):
        random_coords = (random.randrange(50, (self.parking_area[0]+50-new_car.width)), random.randrange(50, (self.parking_area[1]+50-new_car.length)))
        new_car.rect.x, new_car.rect.y = random_coords
        iterations = 0
        while len(pygame.sprite.spritecollide(new_car, self.all_sprites_list, dokill= False)) != 0:
            random_coords = (random.randrange(50, (self.parking_area[0]+50-new_car.width)), random.randrange(50, (self.parking_area[1]+50-new_car.length)))
            new_car.rect.x, new_car.rect.y = random_coords
            if iterations > 10000:
                return False
            iterations += 1
        return True

    def print_data(self):
        number_of_cars = len(self.all_sprites_list)
        total_car_area = 0
        for car in self.all_sprites_list:
            total_car_area += (car.width * car.length)
        car_park_area = self.parking_area[0]*self.parking_area[1]
        percent_covered = round((total_car_area/car_park_area)*100, 2)
        return [str(number_of_cars), str(percent_covered)]

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
                    data = self.print_data()
                    print("Number of cars in car park:", data[0])
                    print("Percent of car park covered:", data[1])
                    self.full = True

            #Drawing the car park outline
            pygame.draw.rect(self.screen, BLACK, pygame.Rect(50, 50, self.parking_area[0], self.parking_area[1]), 2)
            


            self.all_sprites_list.update()
            self.all_sprites_list.draw(self.screen)

            pygame.display.flip()
            clock.tick(60)
 
if __name__ == "__main__":
    window = Window()
    window.loop()
    pygame.quit()
    



