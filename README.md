## FRC2429_2023

### Code repo for 2023 using robotpy
FRC robot code for the 2023 robot using robotpy-commands-v2.
 
* This is a work in progress designed to integrate the robot simulation of autonomous and pathweaver trajectories with jupyter notebooks testing our code. 

#### Organization
* robot - 2023 robot code - elevator bot with pneumatic gripper
* gui  - 2023 version of the python dashboard
* sim  - utilities for the simulation (field images, etc)
* other_robots  - code for practie bots, characterization, etc


---
#### Where's the other stuff?
* training notebooks are here: https://github.com/aesatchien/FRC_training
* vision system (image processing on the pi) is here:  https://github.com/aesatchien/FRC2429_vision

#### Installation
Clone the git and install on your own machine:
Use "git clone https://github.com/aesatchien/FRC2429_2023.git" from the git bash (or any git aware) shell to download.  If you don't have git and you just want to look at the code, you can download the repository from the links on the right.

Notes on how to install python and the necessary accessories (particularly the robotpy libraries) that will get all of this running:
https://docs.google.com/document/d/1oS4aMhn9Rf_kpubbQ_JGEtOcRR36LoU-QbJQERZtyIU/edit#heading=h.665ussze99ev but may be a bit cryptic.  I'll help if you need it.
basically, in your python environment you'll need a `pip install robotpy[all]` and if you are working on anything else several more packages.

Once everything is installed, you need to go to the folder with robot.py.  From there, commands like

```python robot.py sim```

should bring up the simulator and allow you to check to see if your gamepad is recognized (you can also use the keyboard) and should be able to let you drive a virtual robot around the field if you have a gamepad. 