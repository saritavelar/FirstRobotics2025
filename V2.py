# TODO: insert robot code here

#import statements

#import rev
import wpilib
import wpilib.drive
from wpilib.drive import MecanumDrive
from rev import SparkMax, SparkLowLevel
#from rev import CANSparkMax, MotorType 

RIGHT_FRONT_MOTOR = 1
LEFT_FRONT_MOTOR = 2
LEFT_REAR_MOTOR = 3
RIGHT_REAR_MOTOR = 5
INTAKE_MOTOR = 4
#ELEVATOR_MOTOR = 6

#Declare the class I'm sure why but you have to do this
class MyRobot(wpilib.TimedRobot):
    
    # Allows the motor variables to be called on anywhere in the program
    global RIGHT_FRONT_MOTOR,LEFT_FRONT_MOTOR,RIGHT_REAR_MOTOR,LEFT_REAR_MOTOR,INTAKE_MOTOR
    
    # States the CAN ID's of the motors 
    
    #this part of the code is for autonomous mode which we havent started yet so the "pass" tells the robot to ignore it for now
    def AutonomousInit(self):
            pass
        
    def AutonomousPeriodic(self):
            pass
        # Test each motor individually
        #self.leftFront.set(0.5)  # Test left front motor
        #self.leftRear.set(0.5)   # Test left rear motor
        #self.rightFront.set(0.5) # Test right front motor
        #self.rightRear.set(0.5)  # Test right rear motor

        # Add a delay to observe the motor behavior
       
        #if self.controller.getAButton():
        #    self.leftFront.set(0)  # Test left front motor
        #    self.leftRear.set(0)   # Test left rear motor
        #    self.rightFront.set(0) # Test right front motor
        #    self.rightRear.set(0)


    #Initialize ur robot this parts makes everything work you set the robot up with al the "knowledge"
    def robotInit(self):
        
        #Make the motors work using SparkMax 
        
        # right side motors
        self.rightFront = SparkMax(RIGHT_FRONT_MOTOR, SparkLowLevel.MotorType.kBrushed)
        self.rightRear = SparkMax(RIGHT_REAR_MOTOR, SparkLowLevel.MotorType.kBrushed)

        # left side motors
        self.leftFront = SparkMax(LEFT_FRONT_MOTOR, SparkLowLevel.MotorType.kBrushed)
        self.leftRear = SparkMax(LEFT_REAR_MOTOR, SparkLowLevel.MotorType.kBrushed)
        
        # coral intake motor
        self.intake = SparkMax(INTAKE_MOTOR, SparkLowLevel.MotorType.kBrushed)


        # Set right-side motors to be inverted
        self.leftFront.setInverted(True)
        self.leftRear.setInverted(False)
        self.rightFront.setInverted(False)
        self.rightRear.setInverted(True)
        self.intake.setInverted(False)

        # Creates mecanum drive 
        self.drive = MecanumDrive(self.leftFront, self.leftRear, self.rightFront, self.rightRear)
        
        # Make the Xbox controller work
        self.controller = wpilib.XboxController(0)
    
    
    def AutonomousInit(self):
            pass
        
    def AutonomousPeriodic(self):
            pass
       
 
    def teleopPeriodic(self):
        
        # This part of the code runs repeatedly during teleop mode and where the robot "uses" the knowledge you gave it during the Initialize part
        #self.drive.driveCartesian(self.controller.getX(), self.controller.getY(), self.controller.getZ())

        # Here, the controller gets the values inputted by the joysticks and bumper to allow the robot to function
        leftX = self.controller.getLeftX()  # Left joystick Y-axis (forward/backward)
        leftY = self.controller.getLeftY() 
        rotation = self.controller.getRightX()  # Right joystick X-axis (turning)
        rightTrigger = self.controller.getRightTriggerAxis()
        

        #print(f"leftX: {leftX}, leftY: {leftY}, rotation: {rotation}, rightTrigger: {rightTrigger}")


        self.drive.driveCartesian(leftX, leftY, rotation)
       
        if (rightTrigger > 0.2):
            self.intake.set(1)  # Full power forward (0.5 is 50% power)
        else:
            self.intake.set(0)
            

if __name__ == "__main__":
    wpilib.run(MyRobot)
    
    
