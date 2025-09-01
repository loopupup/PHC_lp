from urdfpy import URDF
import numpy as np

# 加载 URDF 文件
robot = URDF.load("/home/ehr/wxy/PBHC/description/robots/ehr03/urdf/ehr03.urdf")

# 存储信息
joint_names = []
efforts = []
velocities = []

for joint in robot.joints:
    if joint.joint_type in ["revolute", "continuous"]:
        joint_names.append(joint.name)

        if joint.limit is not None:
            efforts.append(joint.limit.effort)
            velocities.append(joint.limit.velocity)
        else:
            efforts.append(0.0)
            velocities.append(0.0)

# 打印格式：一行名字，一行 effort，一行 velocity
print(",".join(joint_names))
print(",".join(f"{eff:.6f}" for eff in efforts))
print(",".join(f"{vel:.6f}" for vel in velocities))

# 可选保存为 .npz 文件
np.savez("../dof_limit_info.npz",
         joint_names=np.array(joint_names),
         efforts=np.array(efforts, dtype=np.float32),
         velocities=np.array(velocities, dtype=np.float32))
print("✅ 输出完成并已保存 dof_limit_info.npz")
