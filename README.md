def robotInit(self):
    """Robot initialization function"""
#Camera
self.CameraServer().launch()

#Left Motor & Reer
left_front = wpilib.PWMSparkMax(1)
left_rear = wpilib.PWMSparkMax(3)
left = wpilib.MotorControllerGroup(left_front, left_rear)

#Right Motor & Reer
right_front = wpilib.PWMSparkMax(2)
right_rear = wpilib.PWMSparkMax(4)
right = wpilib.MotorControllerGroup(right_front, right_rear)
right_front.setInverted(True)
right_rear.setInverted(True)

#DriveTrain
self.robotDrive = wpilib.drive.DifferentialDrive(left, right)

#Controller
self.driverController = wpilib.XboxController(0)

def teleopPeriodic(self):
    # Drive with tank drive.
    # That means that the Y axis of the left stick moves the left side of the robot forward and backward, and the Y axis of the right stick moves the right side of the robot forward and backward.
    self.robotDrive.tankDrive(
        -self.driverController.getRightY(), -self.driverController.getLeftY()
    )
