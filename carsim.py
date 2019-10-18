import os
from math import sin, tan, radians, degrees, copysign
import pygame
from pygame.math import Vector2

# local import
import car_model

# Get image of car
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "car.png")
car_image = pygame.image.load(image_path)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GAME_TICKS = 60

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Car Sim")
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.ticks = GAME_TICKS
        self.exit = False
        self.car_image = None

    ''' processes the simulation '''
    def run(self):
        # Create car model
        car = car_model.Car(self.width/2, self.height/2)

        while not self.exit:
            # Convert time from milliseconds to seconds
            dt = self.clock.get_time() / 1000

            # Event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            # User input
            pressed = pygame.key.get_pressed()
            self.controls(car, dt, pressed)

            # Logic
            car.update(dt)

            # Drawing
            self.draw(car)

            # Update the clock (Called once per frame)
            self.clock.tick(self.ticks)
        ''' End of while not self.exit '''

        pygame.quit()

    ''' defines the controls of the car '''
    def controls(self, car, dt, pressed):
        if pressed[pygame.K_LEFT]:
            car.steer_angle += 1
        elif pressed[pygame.K_RIGHT]:
            car.steer_angle -= 1
        if pressed[pygame.K_UP]:
            car.accel += 0.1
        elif pressed[pygame.K_DOWN]:
            car.accel -= 0.1
        else:
            car.accel = 0
        car.accel = max(-car.max_accel, min(car.accel, car.max_accel))
        car.steer_angle = max(-car.max_steer, min(car.steer_angle, car.max_steer))

    ''' Draws the screen and objects '''
    def draw(self, car):
        self.screen.fill((0,0,0))
        self.car_image = pygame.transform.scale(car_image, (30,15))
        rotated = pygame.transform.rotate(self.car_image, car.angle)
        rect = rotated.get_rect()
        self.screen.blit(rotated, car.position - (rect.width / 2, rect.height / 2))
        pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()