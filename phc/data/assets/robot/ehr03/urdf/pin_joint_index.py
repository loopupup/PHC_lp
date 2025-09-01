#
# In this short script, we show how to use RobotWrapper
# integrating different kinds of viewers
#
 
from pathlib import Path
from sys import argv
 
import pinocchio as pin
from pinocchio.robot_wrapper import RobotWrapper
from pinocchio.visualize import GepettoVisualizer, MeshcatVisualizer
 
# Load the URDF model with RobotWrapper
# Conversion with str seems to be necessary when executing this file with ipython
 
model_path = "/home/eir/ehr_ros2_control/src/ehr_description/ehr03_description/urdf"
mesh_dir = "/home/eir/ehr_ros2_control/src/ehr_description/ehr03_description/meshes"
urdf_filename = "ehr03_pin.urdf"
urdf_model_path = model_path + "/" + urdf_filename
 
robot = RobotWrapper.BuildFromURDF(urdf_model_path, mesh_dir) # fixed joint

# alias
model = robot.model
data = robot.data

for idx, name in enumerate(model.names):
    print(f"Index: {idx}, Joint name: {name}")
 
# do whatever, e.g. compute the center of mass position expressed in the world frame
q0 = robot.q0
com = robot.com(q0)
 
# This last command is similar to:
com2 = pin.centerOfMass(model, data, q0)
print("Center of mass position in the world frame:", com)
 