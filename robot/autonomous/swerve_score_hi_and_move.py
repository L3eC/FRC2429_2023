import commands2
import math
from wpimath.trajectory import TrajectoryConfig, TrajectoryGenerator
from wpimath.geometry import Pose2d, Rotation2d
from wpimath.controller import PIDController, ProfiledPIDControllerRadians

from subsystems.autoconstants import AutoConstants
from subsystems.driveconstants import DriveConstants
from score_hi_cone_from_stow import ScoreHiConeFromStow

class SwerveScoreHiAndMove(commands2.SequentialCommandGroup):
    def __init__(self, container):
        self.container = container

        self.setName("SwerveScoreHiAndMove")

        self.addCommands(ScoreHiConeFromStow(container=self.container))

        config = TrajectoryConfig(
            AutoConstants.kMaxSpeedMetersPerSecond,
            AutoConstants.kMaxAccelerationMetersPerSecondSquared,
        )
        # Add kinematics to ensure max speed is actually obeyed
        config.setKinematics(DriveConstants.kDriveKinematics)

        four_meter_trajectory = TrajectoryGenerator.generateTrajectory(
            Pose2d(0, 0, Rotation2d(3*math.pi/2)),
            Pose2d(0, 4, Rotation2d(3*math.pi/2))
        )

        thetaController = ProfiledPIDControllerRadians(
            AutoConstants.kPThetaController,
            0,
            0,
            AutoConstants.kThetaControllerConstraints,
        )
        thetaController.enableContinuousInput(-math.pi, math.pi)

        swerveControllerCommand = commands2.Swerve4ControllerCommand(
            four_meter_trajectory,
            self.container.drive.getPose,  # Functional interface to feed supplier
            DriveConstants.kDriveKinematics,
            # Position controllers
            PIDController(AutoConstants.kPXController, 0, 0),
            PIDController(AutoConstants.kPYController, 0, 0),
            thetaController,
            self.container.drive.setModuleStates,
            [self.container.drive],
        )

        # Reset odometry to the starting pose of the trajectory.
        self.container.drive.resetOdometry(four_meter_trajectory.initialPose())

        # Run path following command, then stop at the end.
        self.addCommands(swerveControllerCommand.andThen(lambda: self.container.drive.drive(0, 0, 0, False, False)))
