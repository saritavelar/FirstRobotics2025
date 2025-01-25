#import statements
from wpilib import RobotDrive
from wpilib.drive import MeccanumDrive
from rev import CANSparkMax, MotorType
import constants

#Declare the class I'm sure why but you have to do this
class MyRobot(wpilib.TimedRobot):

#this part of the code is for autonomous mode which we havent started yet so the "pass" tells the robot to ignore it for now
    def AutonomousInit(self):
          pass
    def AutonomousPeriodic(self):
         pass
    

#Initialize ur robot this parts makes everything work you set the robot up with al the "knowledge"
    def robotInit(self): 
        #Make the motors work using CANSparkMax
        self.right1 = rev.CANSparkMax(
        constants.kRightMotor1Port, rev.MotorType.kBrushless)
        self.right2 = rev.CANSparkMax(
            constants.kRightMotor2Port, rev.MotorType.kBrushless)
        self.left1 = rev.CANSparkMax(
            constants.kLeftMotor1Port, rev.MotorType.kBrushless)
        self.left2 = rev.CANSparkMax(
            constants.kLeftMotor2Port, rev.MotorType.kBrushless)

#Limit the speed of the motors (I hope this is what this means lol)
        self.right1.setSmartCurrentLimit(constants.kDriveCurrentLimit)
        self.right2.setSmartCurrentLimit(constants.kDriveCurrentLimit)
        self.left1.setSmartCurrentLimit(constants.kDriveCurrentLimit)
        self.left2.setSmartCurrentLimit(constants.kDriveCurrentLimit)

#Make the MeccanumDrive work
        self.drive = MeccanumDrive(self.left1, self.left2, self.right1, self.right2)
#Make the Xbox controller work
        '''self.controller = wpilib.XboxController(0)'''
    def teleopPeriodic(self):
#This part of the code runs repeatedly during teleop mode and where the robot "uses" the knowlegde you gave it during the Intialize part
            self.drive.driveCartesian(self.stick.getX(), self.stick.getY(), self.stick.getZ())

#okay so TBH the following code is what chatgbt told me to do change how the controller controls the drive
           ''' left_y = self.controller.getLeftY()  # Left joystick Y-axis (forward/backward)
            right_y = self.controller.getRightY()  # Right joystick Y-axis (forward/backward)
            rotation = self.controller.getRightX()  # Right joystick X-axis (turning)
            self.robot_drive.driveCartesian(left_y, right_y, rotation)'''
