import math
from wpimath import units
from wpimath.geometry import Translation2d
from wpimath.kinematics import SwerveDrive4Kinematics

class DriveConstants:
    # Driving Parameters - Note that these are not the maximum capable speeds of
    # the robot, rather the allowed maximum speeds
    kMaxSpeedMetersPerSecond = 4.8
    kMaxAngularSpeed = math.tau  # radians per second

    kDirectionSlewRate = 1.2  # radians per second
    kMagnitudeSlewRate = 1.8  # percent per second (1 = 100%)
    kRotationalSlewRate = 2.0  # percent per second (1 = 100%)

    # Chassis configuration
    kTrackWidth = units.inchesToMeters(26.5)
    # Distance between centers of right and left wheels on robot
    kWheelBase = units.inchesToMeters(26.5)

    # Distance between front and back wheels on robot
    kModulePositions = [
        Translation2d(kWheelBase / 2, kTrackWidth / 2),
        Translation2d(kWheelBase / 2, -kTrackWidth / 2),
        Translation2d(-kWheelBase / 2, kTrackWidth / 2),
        Translation2d(-kWheelBase / 2, -kTrackWidth / 2),
    ]
    kDriveKinematics = SwerveDrive4Kinematics(*kModulePositions)

    # Angular offsets of the modules relative to the chassis in radians
    kFrontLeftChassisAngularOffset = -math.pi / 2
    kFrontRightChassisAngularOffset = 0
    kBackLeftChassisAngularOffset = math.pi
    kBackRightChassisAngularOffset = math.pi / 2

    # SPARK MAX CAN IDs
    kFrontLeftDrivingCanId = 21
    kRearLeftDrivingCanId = 23
    kFrontRightDrivingCanId = 25
    kRearRightDrivingCanId = 27

    kFrontLeftTurningCanId = 20
    kRearLeftTurningCanId = 22
    kFrontRightTurningCanId = 24
    kRearRightTurningCanId = 26

    # Maximum values from each analog encoder because they're different for some reason
    kFrontLeftAnalogConversionFactor = math.tau/6.060
    kFrontRightAnalogConversionFactor = math.tau/6.176
    kRearLeftAnalogConversionFactor = math.tau/6.135
    kRearRightAnalogConversionFactor = math.tau/6.131

    # Values of encoders when wheels pointed straight forward in radians
    kFrontLeftAnalogStraight = 5.976 * kFrontLeftAnalogConversionFactor
    kFrontRightAnalogStraight = 3.285 * kFrontRightAnalogConversionFactor # or 1.168 
    kRearLeftAnalogStraight = 3.328 * kRearLeftAnalogConversionFactor
    kRearRightAnalogStraight = 6.094 * kRearRightAnalogConversionFactor


    kGyroReversed = False
