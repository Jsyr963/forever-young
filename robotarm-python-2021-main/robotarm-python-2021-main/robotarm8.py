from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
for i in range(1):
    robotArm.moveRight()
    for i in range(7):
        robotArm.grab()
        for i in range(8):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(8):
            robotArm.moveLeft()
quit()
# Na jouw code wachten tot het sluiten van de window: