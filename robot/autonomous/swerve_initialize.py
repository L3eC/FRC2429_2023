import commands2
from wpimath.kinematics import SwerveModuleState
from wpimath.geometry import Rotation2d
from subsystems.driveconstants import DriveConstants

class SwerveInitialize(commands2.CommandBase):
        def __init__(self, swerve):
            self.drive = swerve

        def runsWhenDisabled(self) -> bool:
             return True

        def end(self, interrupted: bool):
            commands2.ScheduleCommand(self.drive.setModuleStates(
                                     (SwerveModuleState(0, Rotation2d()),
                                     SwerveModuleState(0, Rotation2d()),
                                     SwerveModuleState(0, Rotation2d()),
                                     SwerveModuleState(0, Rotation2d()))))

        # TODO: Make this work