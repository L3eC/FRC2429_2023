import commands2
from wpilib import SmartDashboard
from subsystems.turret import Turret
from subsystems.arm import Arm
from subsystems.vision import Vision

class ScoreByVision(commands2.CommandBase):

    def __init__(self, container, turret: Turret, arm: Arm, vision: Vision, color='green', wait_to_finish=True) -> None:
        super().__init__()
        self.setName('TurretMoveByVision')
        self.container = container
        self.turret = turret
        self.arm = arm
        self.vision = vision
        self.color = color
        self.turretSetpoint = 0
        self.armSetpoint = 0
        self.tolerance = 3  # for stepping to the next preset location
        self.wait_to_finish = wait_to_finish  # determine how long we wait to end

        self.addRequirements(self.turret)  # commandsv2 version of requirements

    def initialize(self) -> None:
        self.print_start_message()
        # tell the turret to go to turretPosition
        turretPosition = self.turret.get_angle()
        armPosition = self.arm.get_extension()

        # smarter to just grab this from networktables directly... less lag
        self.turretSetpoint = None
        self.armSetpoint = None
        if self.vision.camera_values[self.color]['targets'] > 0:
            self.turretSetpoint = turretPosition + self.vision.camera_values[self.color]['rotation_entry']
            self.armSetPoint = armPosition + :w
        self.vision.camera_values[self.color]['distance_entry']
        else:  # try to find another target for loading zone
            colors = ['green', 'yellow', 'purple']
            for color in colors:
                if self.vision.camera_values[color]['targets'] > 0:
                    self.turretSetpoint = turretPosition + self.vision.camera_values[self.color]['rotation_entry']
                    self.color = color
                    break
        if self.turretSetpoint is None:
            self.turretSetpoint = turretPosition

        print('\n', f'Vision angle is {self.turretSetpoint} on {self.color}')
        self.turret.set_turret_angle(angle=self.turretSetpoint, mode='smartmotion')

    def execute(self) -> None:  # nothing to do, the sparkmax is doing all the work
        pass

    def isFinished(self) -> bool:
        if self.wait_to_finish:  # wait for the turret to get within x degrees
            return abs(self.turret.get_angle() - self.turretSetpoint) < self.tolerance
        else:
            return True

    def end(self, interrupted: bool) -> None:
        end_time = self.container.get_enabled_time()
        message = 'Interrupted' if interrupted else 'Ended'
        print(f"** {message} {self.getName()} at {end_time:.1f} s at {self.turret.sparkmax_encoder.getPosition():.1f} after {end_time - self.start_time:.1f} s **")
        # SmartDashboard.putString(f"alert", f"** {message} {self.getName()} at {end_time:.1f} s after {end_time - self.start_time:.1f} s **")

    def print_start_message(self):
        self.start_time = round(self.container.get_enabled_time(), 2)
        print("\n" + f"** Started {self.getName()} at {self.start_time} s **", flush=True)
        SmartDashboard.putString("alert", f"** Started {self.getName()} at {self.start_time - self.container.get_enabled_time():2.2f} s **")