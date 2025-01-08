# FirstRobotics2025
#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#
#change for new branch
import wpilib
#from wpilib.cameraserver import CameraServer
from wpilib import Timer
import wpilib.drive


class MyRobot(wpilib.TimedRobot):
    """
    This is a demo program showing the use of the DifferentialDrive class.
    Runs the motors with split arcade steering and an Xbox controller.
    """

    def robotInit(self):
        """Robot initialization function"""
#Camera
        #self.CameraServer().launch()
# Left Motor & Reer
        left_front = wpilib.PWMSparkMax(3)
        left_rear = wpilib.PWMSparkMax(2)
        left = wpilib.MotorControllerGroup(left_front, left_rear)

# Right Motor & Reer
        right_front = wpilib.PWMSparkMax(5)
        right_rear = wpilib.PWMSparkMax(4)
        right = wpilib.MotorControllerGroup(right_front, right_rear)

        self.robotDrive = wpilib.drive.DifferentialDrive(left, right)
        self.driverController = wpilib.XboxController(0)

        # We need to invert one side of the drivetrain so that positive voltages
        # result in both sides moving forward. Depending on how your robot's
        # gearbox is constructed, you might have to invert the left side instead.
        right_front.setInverted(True)
        right_rear.setInverted(True)

        #Shooter Motors 
        shootermotor1 = wpilib.PWMSparkMax(6)
        shootermotor2 = wpilib.PWMSparkMax(7)
        self.shooterMotor = wpilib.MotorControllerGroup(shootermotor1, shootermotor2)
        shootermotor2.setInverted(True)

        #Inatke Motor
        self.intakeMotor =  wpilib.PWMSparkMax(0)

        #Timer
        self.timer =Timer()

    #def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        #self.timer.restart()

    #def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds
        #if self.timer.get() < 2.0:
            # Drive forwards half speed, make sure to turn input squaring off
           # self.robotDrive.arcadeDrive(0.5, 0, squareInputs=False)
       # else:
          #  self.robotDrive.stopMotor()

    def teleopPeriodic(self):
        # Drive with tank drive.
        # That means that the Y axis of the left stick moves the left side of the robot forward and backward, and the Y axis of the right stick moves the right side of the robot forward and backward.
        self.robotDrive.tankDrive(
            -self.driverController.getRightY(), -self.driverController.getLeftY()
        )

        #shooter right trigger
        if self.driverController.getRightTriggerAxis() > 0.2:
             self.shooterMotor.set(1) #fastest speed
        else:
            self.shooterMotor.set(0)
        #intake left trigger 
        if self.driverController.getLeftTriggerAxis() > 0.2:
           self.intakeMotor.set(0.9) #0.9 worked so the disc doesnt get stuck
        else:
            self.intakeMotor.set(0)
        

        # reverse intake (maybe)
        if self.driverController.leftBumper():            
                self.intakeMotor.set(-0.5)
        else:
                self.intakeMotor.set(0)
