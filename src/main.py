
from vex import *
import time

"""Fields chool Robotics, team 11555B"""

brain=Brain()
ControllerType.PRIMARY

controller = Controller(PRIMARY)

myVariable = 0
TChainToggle = 2 #1 is forward 2 is still 3 is reverse
piston = DigitalOut(brain.three_wire_port.b)

#double check ports

LeftD_F = Motor(Ports.PORT4,GearSetting.RATIO_18_1, True) #looks like the ratio 18 to 1 is the only we're using, other ones might give us either more torque or speed, have we messed arround with them?
LeftD_B = Motor(Ports.PORT3,GearSetting.RATIO_18_1, True)


RightD_F = Motor(Ports.PORT2,GearSetting.RATIO_18_1, False)
RightD_B = Motor(Ports.PORT1,GearSetting.RATIO_18_1, False)


imu1 = Inertial(Ports.PORT13) #what is this??? I dont remember putting this in - looks like inertial sensor inout slot? we need to learn how to use it-{matteo}
left_drive = MotorGroup(LeftD_F, LeftD_B,)
right_drive = MotorGroup(RightD_F, RightD_B)
drivetrain = DriveTrain(right_drive, left_drive)

intake = Motor(Ports.PORT11,GearSetting.RATIO_18_1, False)

Tchain = Motor(Ports.PORT6,GearSetting.RATIO_18_1, False)

def Tchain_ON():
    Tchain.set_velocity(100, PERCENT)
    Tchain.spin(FORWARD)

def Tchain_STOP():
    Tchain.set_stopping(BRAKE)
    Tchain.stop

"""def TchainMove():
    if TChainToggle == 1: Tchain.set_velocity(100, PERCENT)
    Tchain.spin(FORWARD)
    if TChainToggle == 2: Tchain.set_stopping(BRAKE)
    Tchain.stop
    if TChainToggle == 3: Tchain.set_velocity(100, PERCENT)
    Tchain.spin(REVERSE)""" #works to define the functions for the tchain 

is_driver = False #why do we need to have this here? Shouldn't this be presumed false by default?

def piston_in():
    piston.set(False)

def piston_out():
   piston.set(True)

def drive_stop():
    right_drive.set_stopping(BRAKE)
    left_drive.set_stopping(BRAKE)
    right_drive.stop()
    left_drive.stop()

def drive_drive():
    right_drive.set_velocity(100, PERCENT)
    left_drive.set_velocity(100, PERCENT)
    left_drive.spin(FORWARD)
    right_drive.spin(FORWARD)

def drive_slow():
    right_drive.set_velocity(95, PERCENT) #95% is sloW????
    left_drive.set_velocity(95, PERCENT)
    left_drive.spin(FORWARD)
    right_drive.spin(FORWARD)

def drive_reverse():
    right_drive.set_velocity(100, PERCENT)
    left_drive.set_velocity(100, PERCENT)
    left_drive.spin(REVERSE)
    right_drive.spin(REVERSE)

def drive_l():
    right_drive.set_velocity(100, PERCENT)
    left_drive.set_velocity(100, PERCENT)
    left_drive.spin(REVERSE)
    right_drive.spin(FORWARD)

def drive_r():
    right_drive.set_velocity(100, PERCENT)
    left_drive.set_velocity(100, PERCENT)
    left_drive.spin(FORWARD)
    right_drive.spin(REVERSE)


myVariable = 0 #what is this and why is it defined twice?



#controller.buttonUp.pressing()
#Lanch.spin_to_position(360, DEGREES)



#
#---------------------------------------------------------------#
# Axis 2 - Right drive - Ports 1, 2, 3,
# Axis 3 - Left drive - Ports 4, 5, 6,

# Axis 1 (X-axis of the Left Joystick): Controls left and right movement (turning).
# Axis 2 (Y-axis of the Right Joystick): Often used for controlling the speed of a mechanism (like an arm or a claw).
# Axis 3 (Y-axis of the Left Joystick): As mentioned, controls forward and backward movement.
# Axis 4 (X-axis of the Right Joystick): Controls left and right movement (turning or strafing).

def driver():
    global r_pos
    global l_pos
    global is_driver
    global mode
    is_driver=True
    while True:
        right_drive.set_velocity(controller.axis2.position(), PERCENT)
        right_drive.spin(FORWARD)

        left_drive.set_velocity(controller.axis3.position(), PERCENT)
        left_drive.spin(FORWARD)

        """if controller.buttonY.pressed(TchainMove):
            if TChainToggle == 2: TChainToggle = 1 
            elif TChainToggle == 3: TChainToggle = 1
            elif TChainToggle == 1: TChainToggle = 2

        if controller.buttonRight.pressed(TchainMove):
            if TChainToggle == 2: TChainToggle = 3 
            elif TChainToggle == 3: TChainToggle = 2
            elif TChainToggle == 1: TChainToggle = 3""" #Does all the Tchain stuff and makes it toggleable in coordination with the function up top

        if controller.buttonX.pressing():
            Tchain.stop()

        if controller.buttonY.pressing():
            Tchain.set_velocity(100, PERCENT)
            Tchain.spin(FORWARD)
          
        if controller.buttonRight.pressing():
            Tchain.set_velocity(100, PERCENT)
            Tchain.spin(REVERSE) #position in code adjusted but actual code hasn't been.

        if controller.buttonA.pressing():
            piston_out()

        if controller.buttonB.pressing():
            piston_in()

        if controller.buttonUp.pressing():
            intake.set_velocity(100, PERCENT)
            intake.spin(FORWARD)

        if controller.buttonDown.pressing():
            intake.stop()
        
        if controller.buttonLeft.pressing():
            intake.set_velocity(100, PERCENT)
            intake.spin(REVERSE)

        

        #if controller.buttonL1.pressing():
        #if controller.buttonL2.pressing(): 
        """controller L1 or L2 button could be for the hanging extension at the end??"""
            

#---------------------------------------------------------------#
# Up - both 90
# Right - Right 90
# Left - Left 90
# Down - Both In


#in_r.set_stopping(HOLD)
#in_r.set_position(90)
#drivetrain.(FORWARD)
#time.sleep(0.5)
#drivetrain.stop
# Replace the MODE parameter with one of the following options:
# BRAKE: will cause the Drivetrain to come to an immediate stop.
# #HOLD: will cause the Drivetrain to come to an immediate stop, and returns it to its stopped position if moved.



# if controller.buttonUp.pressing(): # type: ignore
#time.sleep(0.1)

# if controller.buttonDown.pressing(): # type: ignore

# if controller.buttonR2.pressing(): # type: ignore


# if controller.buttonL2.pressing(): # type: ignore

#if controller.buttonL1.pressing():

# if controller.buttonR1.pressing():

# if controller.buttonRight.pressing():
# if controller.buttonLeft.pressing():

# if controller.buttonLeft.pressing(): # type: ignore
# in_l.set_velocity(70, PERCENT)


def autonomous():
    global r_pos
    global l_pos
    global is_driver
    is_driver = False
    piston_in()
    left_drive.set_velocity(80, PERCENT)
    left_drive.spin(REVERSE)
    right_drive.set_velocity(80, PERCENT)
    right_drive.spin(REVERSE) 
    time.sleep(0.6)
    """piston_out()
    right_drive.stop()
    left_drive.stop()
    time.sleep(1)
    right_drive.set_velocity(80, PERCENT)
    right_drive.spin(FORWARD)
    left_drive.set_velocity(80, PERCENT)
    left_drive.spin(FORWARD)
    time.sleep(1)
    left_drive.set_velocity(100, PERCENT)
    left_drive.spin(REVERSE)
    right_drive.set_velocity(100, PERCENT)
    right_drive.spin(REVERSE) 
    time.sleep(0.5)"""
    Tchain_ON()
    time.sleep(2)
    Tchain_STOP() #the robot should have the ring on it
    left_drive.set_velocity(80, PERCENT)
    left_drive.spin(REVERSE)
    right_drive.set_velocity(80, PERCENT)
    right_drive.spin(REVERSE)
    time.sleep(0.6)

    

#problems with auton currently are that it knocks the mobile goal into the center thing and isnt able to the ring onto it
#might be able to fix this by slowing the speed. We can speed it up once we know it can do the things it needs to


competition = Competition(driver,autonomous)


#drivetrain.stop
# Replace the MODE parameter with one of the following options:
# BRAKE: will cause the Drivetrain to come to an immediate stop.
# #HOLD: will cause the Drivetrain to come to an immediate stop, and returns it to its stopped position if moved.
