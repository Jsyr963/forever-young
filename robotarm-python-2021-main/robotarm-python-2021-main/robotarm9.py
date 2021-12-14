from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')
# Jouw python instructies zet je vanaf hier:

for i in range(1, 6):
    for i in range(i):
        robotArm.grab()
        for moveRight in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for moveLeft in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()
quit()

    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()