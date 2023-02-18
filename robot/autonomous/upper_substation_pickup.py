import commands2

import constants

from subsystems.elevator import Elevator
from commands.elevator_move import ElevatorMove

class UpperSubstationPickup(commands2.SequentialCommandGroup):  # change the name for your command

    def __init__(self, container) -> None:
        super().__init__()
        self.setName('UpperStationPickup')  # change this to something appropriate for this command
        self.container = container

        # Step 1.a
        # raise elevator to appropriate height
        self.addCommands(ElevatorMove(container=self.container, elevator=self.container.elevator,
                                      setpoint=Elevator.positions['upper_pickup'], wait_to_finish=False))

        # Step 1.b
        # Get turret into position - center on the cone/cube (vision processor)

        # Step 2.a
        # lower wrist to horizontal

        # Step 2.b
        # extend the arm fully / to the cone/cube

        # Step
        # Close the manipulator

        # Step
        # Retract arm



