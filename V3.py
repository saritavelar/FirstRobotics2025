import wpilib
import wpilib.drive
from wpilib.drive import MecanumDrive
from rev import SparkMax, SparkLowLevel

#Declare the class I'm sure why but you have to do this
class MyRobot(wpilib.TimedRobot):
    
    # Allows the motor variables to be called on anywhere in the program
    global RIGHT_FRONT_MOTOR,LEFT_FRONT_MOTOR,RIGHT_REAR_MOTOR,LEFT_REAR_MOTOR,INTAKE_MOTOR,ELEVATOR_MOTOR
    
    # States the CAN ID of each motor
    RIGHT_FRONT_MOTOR = 1
    LEFT_FRONT_MOTOR = 2
    RIGHT_REAR_MOTOR = 5
    LEFT_REAR_MOTOR = 3
    INTAKE_MOTOR = 4
    ELEVATOR_MOTOR = 6

    #Initialize ur robot this parts makes everything work you set the robot up with al the "knowledge"
    def robotInit(self):
        
    #Make the motors work using SparkMax 
        
        # right side motors
        self.rightFront = SparkMax(RIGHT_FRONT_MOTOR, SparkLowLevel.MotorType.kBrushed)
        self.rightRear = SparkMax(RIGHT_REAR_MOTOR, SparkLowLevel.MotorType.kBrushed)
        # left side motors
        self.leftFront = SparkMax(LEFT_FRONT_MOTOR, SparkLowLevel.MotorType.kBrushed)
        self.leftRear = SparkMax(LEFT_REAR_MOTOR, SparkLowLevel.MotorType.kBrushed)
        # intake and elevator motors
        self.intake = SparkMax(INTAKE_MOTOR, SparkLowLevel.MotorType.kBrushed)
        self.elevator = SparkMax(ELEVATOR_MOTOR, SparkLowLevel.MotorType.kBrushed)
        
        # Creates mecanum drive 
        self.drive = MecanumDrive(self.leftFront, self.leftRear, self.rightFront, self.rightRear)
        # Make the Xbox controller work
        self.controller = wpilib.XboxController(0)


    #this part of the code is for autonomous mode which we havent started yet so the "pass" tells the robot to ignore it for now
    def AutonomousInit(self):
        
        self.timer = wpilib.Timer()
        self.timer.start()
    
        
    def AutonomousPeriodic(self):
    
        if self.timer.get() < 3.0: 
            self.drive.driveCartesian(0,0.25,0)
        else:
            self.drive.driveCartesian(0,0,0)
        
     
    def teleopPeriodic(self):
        
        # This part of the code runs repeatedly during teleop mode and where the robot "uses" the knowledge you gave it during the Initialize part

        # Here, the controller gets the values inputted by the joysticks and bumper to allow the robot to function
        leftY = -self.controller.getLeftY()  # Left joystick Y-axis (forward/backward)
        leftX = self.controller.getLeftX()  # Right joystick Y-axis (forward/backward)
        rotation = self.controller.getRightX()  # Right joystick X-axis (turning)
        rightTrigger = self.controller.getRightTriggerAxis()
        
        
        self.drive.driveCartesian(leftY, leftX, rotation)
       
        if (rightTrigger > 0.2):
            self.intake.set(1)  # Motor Power (0-1 = 0%-100%, accordingly)
        else:
            self.intake.set(0)

if __name__ == "__main__":
    wpilib.run(MyRobot)
