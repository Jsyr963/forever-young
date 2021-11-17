from RobotArm import RobotArm
import pygame
import sys
import random

robotArm = RobotArm('exercise 1')

# Jouw python instructies zet je vanaf hier:
for i in range(1):
    robotArm.moveRight()
    robotArm.grab()
for i in range(1):
    robotArm.moveLeft()
    robotArm.drop()

    # Na jouw code wachten tot het sluiten van de window:
robotArm.wait(3)