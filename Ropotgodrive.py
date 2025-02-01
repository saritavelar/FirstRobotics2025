#import statements
import rev
import wpilib
import wpilib.drive
from constants import constants
from wpilib.drive import MeccanumDrive
from rev import CANSparkMax, MotorType

#Declare the class I'm sure why but you have to do this
class MyRobot(wpilib.TimedRobot):


#this part of the code is for autonomous mode which we havent started yet so the "pass" tells the robot to ignore it for now
    def AutonomousInit(self):
          pass
    def AutonomousPeriodic(self):
         pass
    

#Initialize ur robot this parts makes everything work you set the robot up with al the "knowledge"
    def robotInit(self):
        kRightMotor1Port = 1
        kRightMotor2Port = 3
        kLeftMotor1Port = 2
        kLeftMotor2Port = 4
        shooterMotorPort = 5




#Make the motors work using CANSparkMax
        self.right1 = rev.CANSparkMax(1,kRightMotor1Port, rev.MotorType.kBrushed)
        self.right3 = rev.CANSparkMax(3, kRightMotor2Port, rev.MotorType.kBrushed)


        self.left2 = rev.CANSparkMax(2,kLeftMotor1Port, rev.MotorType.kBrushed)
        self.left4 = rev.CANSparkMax(4,kLeftMotor2Port, rev.MotorType.kBrushed)
        self.shooterMotor = rev.CANSparkMax(shooterMotorPort, rev.MotorType.kBrushed)

        # Set right-side motors to be inverted
        self.right1.setInverted(True)
        self.right3.setInverted(True)

#Make the MeccanumDrive work
        self.drive = MeccanumDrive(self.left2, self.left4, self.right1, self.right3)
#Make the Xbox controller work
        self.controller = wpilib.XboxController(0)
        self.drive = MeccanumDrive(self.left2, self.left4, self.right1, self.right3)
        
        #Limit the speed of the motors (I hope this is what this means lol)
        self.right1.setSmartCurrentLimit(constants.kDriveCurrentLimit)
        self.right2.setSmartCurrentLimit(constants.kDriveCurrentLimit)
        self.left1.setSmartCurrentLimit(constants.kDriveCurrentLimit)
        self.left2.setSmartCurrentLimit(constants.kDriveCurrentLimit)

    def teleopPeriodic(self):
        # This part of the code runs repeatedly during teleop mode and where the robot "uses" the knowledge you gave it during the Initialize part
        self.drive.driveCartesian(self.controller.getX(), self.controller.getY(), self.controller.getZ())

        # okay so TBH the following code is what chatgpt told me to do to change how the controller controls the drive
        left_y = self.controller.getLeftY()  # Left joystick Y-axis (forward/backward)
        right_y = self.controller.getRightY()  # Right joystick Y-axis (forward/backward)
        rotation = self.controller.getRightX()  # Right joystick X-axis (turning)
        self.drive.driveCartesian(left_y, right_y, rotation)

        if self.driverController.getRightTriggerAxis() > 0.2:
            self.shooterMotor.set(0.5)  # 1 is full speed so 0.5 is half speed go higher number if it doesn't work.
        else:
            self.shooterMotor.set(0)

if __name__ == "__main__":
    wpilib.run(MyRobot)

 
