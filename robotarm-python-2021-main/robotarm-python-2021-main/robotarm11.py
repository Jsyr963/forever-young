from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
# Jouw python instructies zet je vanaf hier:

for Blokken in range(10):
    robotArm.moveRight()
for Blokken in range(10):
    if robotArm.grab() and robotArm.scan() == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveLeft()
quit()

# Na jouw code wachten tot het sluiten van de window: