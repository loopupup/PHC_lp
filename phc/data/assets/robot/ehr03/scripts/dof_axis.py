from urdfpy import URDF
import numpy as np

# 加载 URDF 文件（请替换为你的实际路径）
robot = URDF.load("/home/ehr/wxy/PBHC/description/robots/ehr03/urdf/ehr03.urdf")

# 提取 revolute / continuous 关节的旋转轴
axis_list = []
joint_names = []

for joint in robot.joints:
    if joint.joint_type in ["revolute", "continuous"]:
        axis = joint.axis if joint.axis is not None else np.array([1, 0, 0])
        axis_list.append(axis)
        joint_names.append(joint.name)

# 打印结果
print("可旋转关节及其旋转轴：")
for name, axis in zip(joint_names, axis_list):
    print(f"{name}: {axis}")

# 保存为 .npy 文件
dof_axis = np.array(axis_list, dtype=np.float32)
np.save("../dof_axis.npy", dof_axis)
print("✅ dof_axis.npy 已保存，shape =", dof_axis.shape)
