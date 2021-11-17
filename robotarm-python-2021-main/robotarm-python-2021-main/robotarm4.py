from RobotArm import RobotArm
import pygame
import sys
import random

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
for i in range(1):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
for i in range(1):
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
for i in range(1):
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
for i in range(1):
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.drop()
for i in range(1):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait(3)