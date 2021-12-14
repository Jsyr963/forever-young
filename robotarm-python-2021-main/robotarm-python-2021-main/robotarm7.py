from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')
# Jouw python instructies zet je vanaf hier:
for i in range(5):
    robotArm.moveRight()
    for i in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    robotArm.moveRight()
quit()

# Na jouw code wachten tot het sluiten van de window:
