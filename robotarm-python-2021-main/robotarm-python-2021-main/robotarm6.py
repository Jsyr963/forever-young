from RobotArm import RobotArm
import pygame
import sys
import random

robotArm = RobotArm('exercise 6')
for i in range(7):
    robotArm.moveRight()
for i in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    for i in range(2):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait(3)