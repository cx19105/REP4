import pygame, random
from car import Car
from colours import *

pygame.init()

class Window:
    def __init__(self, aspect_ratio, height):
        self.running = True
        self.full = False
        self.parking_area = (round(aspect_ratio*height), height)
        self.size = [x+100 for x in self.parking_area]
        #self.screen = pygame.display.set_mode(self.size)
        #pygame.display.set_caption("Car Parking")
        #self.screen.fill(WHITE)
        self.all_sprites_list = pygame.sprite.Group()

    def add_car(self, new_car):
        if (self.parking_area[0]+50-new_car.width) < 50 or (self.parking_area[1]+50-new_car.length) < 50:
            return False
        
        random_coords = (random.randrange(50, (self.parking_area[0]+50-new_car.width)), random.randrange(50, (self.parking_area[1]+50-new_car.length)))
        new_car.rect.x, new_car.rect.y = random_coords
        iterations = 0
        while len(pygame.sprite.spritecollide(new_car, self.all_sprites_list, dokill= False)) != 0:
            random_coords = (random.randrange(50, (self.parking_area[0]+50-new_car.width)), random.randrange(50, (self.parking_area[1]+50-new_car.length)))
            new_car.rect.x, new_car.rect.y = random_coords
            if iterations > 1000:
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
        return [number_of_cars, percent_covered]

    def loop(self):
        #clock=pygame.time.Clock()
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
                    print("Number of cars in car park:", str(data[0]))
                    print("Percent of car park covered:", str(data[1]))
                    #pygame.display.flip()
                    return data
                    

            #Drawing the car park outline
            #pygame.draw.rect(self.screen, BLACK, pygame.Rect(50, 50, self.parking_area[0], self.parking_area[1]), 2)

            #self.all_sprites_list.update()
            #self.all_sprites_list.draw(self.screen)

            
            #clock.tick(240)





