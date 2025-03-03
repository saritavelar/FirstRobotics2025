# Import statements
import wpilib
import math 
import wpilib.drive
from cscore import CameraServer
from wpilib.drive import MecanumDrive
from rev import SparkMax, SparkLowLevel

# States the CAN IDs of the motor controllers
RIGHT_FRONT_MOTOR = 1
LEFT_FRONT_MOTOR = 2
LEFT_REAR_MOTOR = 3
RIGHT_REAR_MOTOR = 5
INTAKE_MOTOR = 4

# Initializes both USB cameras on the robot
CameraServer.startAutomaticCapture(0)
CameraServer.startAutomaticCapture(1)

# Declaring the class so that the driver station is able
# to identify that this is the code that the roboRIO 
# will use to allow the robot to work properly.
class MyRobot(wpilib.TimedRobot):
    
    # Allows the motor variables to be called on anywhere in the program
    global RIGHT_FRONT_MOTOR,LEFT_FRONT_MOTOR,RIGHT_REAR_MOTOR,LEFT_REAR_MOTOR,INTAKE_MOTOR#,ELEVATOR_MOTOR

    #Initialize ur robot this parts makes everything work you set the robot up with al the "knowledge"
    def robotInit(self):
        
        # Stating each motor controler and the motor it is connected to.
        #right side motors
        self.rightFront = SparkMax(RIGHT_FRONT_MOTOR, SparkLowLevel.MotorType.kBrushed)
        self.rightRear = SparkMax(RIGHT_REAR_MOTOR, SparkLowLevel.MotorType.kBrushed)
        #left side motors
        self.leftFront = SparkMax(LEFT_FRONT_MOTOR, SparkLowLevel.MotorType.kBrushed)
        self.leftRear = SparkMax(LEFT_REAR_MOTOR, SparkLowLevel.MotorType.kBrushed)
        #intake and elevator motors
        self.intake = SparkMax(INTAKE_MOTOR, SparkLowLevel.MotorType.kBrushed)
        
        # Creates mecanum drive 
        self.drive = MecanumDrive(self.leftFront, self.leftRear, self.rightFront, self.rightRear)
        # Make the Xbox controller work
        self.controller = wpilib.XboxController(0)


# Here, a timer is created so that the autonomous periodic function can run conditionals based on time intervals.
    def autonomousInit(self):
        self.drive.driveCartesian(0,0,0)
        self.intake.set(0)
        self.timer = wpilib.Timer()
        self.timer.reset()
        self.timer.start()
        # The self.state variable allows the periodic function to run different conditions one after the other.
        self.state = 0
    
        
    def autonomousPeriodic(self):
        # time variabloe stores the time giver by the timer 
        time = self.timer.get()

        # state 0 tells the robot to move forward for 4 seconds 
        if self.state == 0:
            if time < 4.0:
                self.drive.driveCartesian(.25,0,0)
            else:
                self.drive.driveCartesian(0,0,0)
                self.intakeOn = 1 

        # state 1 tells the robot to turn the intake motor on 
        if self.state == 1:

            self.intake.set(.5)

            if time >= 6.0:
                self.intakeOn = 2 

        # state 2 stops the timer and turns off the intake motor 
        # (FYI, this can be done in state 1's if statement instead of making a new state)
        if self.state == 2:
            self.intake.set(0)
            self.timer.stop()

     
    def teleopPeriodic(self):
        # This part of the code runs repeatedly during teleop mode and where the robot "uses" the knowledge you gave it during the Initialize part

        # creates variables that store the values of the joystick inputs 
        leftY = -self.controller.getLeftY()  # Left joystick Y-axis (forward/backward)
        leftX = self.controller.getLeftX()  # Left joystick X-axis (left/right)
        rotation = self.controller.getRightX()  # Right joystick X-axis (turning)
        rightTrigger = self.controller.getRightTriggerAxis()
        
        # acceleration variables 
        
        if leftX == 0: 
            accelerationX = 0  
        else:
            accelerationX = .6 * (math.e**leftX) - .65
            
        if leftY == 0: 
            accelerationY = 0 
        else:     
            accelerationY = .6 * (math.e**leftY) - .65
        
        # drive cartesian allows the robot to move 
        self.drive.driveCartesian(accelerationY, accelerationX, rotation)
        #self.drive.driveCartesian(leftY, leftX, rotation)

        # prints the values of leftY and leftX in the driver stattion console
        print(f"Y Speed:{leftY}" + "\n" + f"X Speed: {leftX}")

        # turns intake motor on when right trigger is pressed 
        if (rightTrigger > 0.2):
            self.intake.set(.5)  # Motor Power (0-1 = 0%-100%, accordingly)
        else:
            self.intake.set(0)


if __name__ == "__main__":
    wpilib.run(MyRobot)
