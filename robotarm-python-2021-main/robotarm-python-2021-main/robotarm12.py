from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
# Jouw python instructies zet je vanaf hier:

for Blokken in range(10):
    robotArm.moveRight() 
for Blokken in range(10):
    if robotArm.grab() and robotArm.scan() == 'red':
        for i in range(10):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(Blokken):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveLeft()
quit()
    
# Na jouw code wachten tot het sluiten van de window:
