import rev 
from rev import SparkLowLevel
import wpilib

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Initialize Spark MAX motor controller
        self.motor = rev.SparkMax(1, SparkLowLevel.MotorType.kBrushed)  # CAN ID 1
        self.motor.setInverted(True)  # Invert motor if necessary
        self.motor.set(0)  # Set motor power to 0 (stop motor)
        
        self.controller = wpilib.XboxController(0)

    def teleop(self):
        # Set motor speed (e.g., full forward)
        rightTrigger = self.controller.getRightTriggerAxis()
        
        if (rightTrigger > 0.2):
            self.motor.set(1)  # Full power forward (1 is 100% power)
        else:
            self.motor.set(0)
        

if __name__ == "__main__":
    wpilib.run(MyRobot)
