import pygame
from pygame.math import Vector2
from math import sin, cos, tan, radians, degrees, copysign


class Car:
    def __init__(self, x, y, angle=90.0, length = 60, max_steer=60, max_accel=20.0):
        self.position = Vector2(x,y)
        self.velocity = Vector2(0.0,0.0)
        self.accel = 0.0
        self.steer_angle = 0.0
        self.angle = angle
        self.speed = 0.0
        # Constants
        self.length = length

        # Thresholds for input
        self.max_accel = max_accel
        self.max_steer = max_steer

    ''' Update the vehicle information '''
    def update(self, dt):
        self.speed += self.accel * dt
        self.angle = self.steer_angle

        # Air resistance and friction
        if(self.speed > 0):
            self.speed -= 0.01
        else:
            self.speed = 0

        self.position.x += self.speed

        # Print Characteristics
        print("SPEED="+str(self.speed))
        print("STEERANGLE="+str(self.steer_angle))
        print("ANGLE="+str(self.angle))
        print("VEL="+str(self.velocity))
        print("POS="+str(self.position))
        print("ACCEL="+str(self.accel))
