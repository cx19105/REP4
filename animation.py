
from window import Window
import pygame
from colours import *
from car import Car

pygame.init()


class Animate(Window):
    def __init__(self, aspect_ratio, height):
        super().__init__(aspect_ratio, height)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Car Parking")
        self.screen.fill(WHITE)
    
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
                    print("Number of cars in car park:", str(data[0]))
                    print("Percent of car park covered:", str(data[1]))
                    pygame.display.flip()

                    

            #Drawing the car park outline
            pygame.draw.rect(self.screen, BLACK, pygame.Rect(50, 50, self.parking_area[0], self.parking_area[1]), 2)

            self.all_sprites_list.update()
            self.all_sprites_list.draw(self.screen)

            
            clock.tick(240)

if __name__ == "__main__":
    animation = Animate(2.5, 300)
    #data = get_data(100, 1000, 0.2, 3)
    animation.loop()
