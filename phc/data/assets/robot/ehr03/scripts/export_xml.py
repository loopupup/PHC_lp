from mujoco import mjcf

# 1. 加载 URDF 文件
mjcf_model = mjcf.from_path("/home/ehr/wxy/PBHC/description/robots/ehr03/urdf/ehr03.urdf")

# 2. 导出为 MJCF XML 文件
with open("converted_model.xml", "w") as f:
    f.write(mjcf_model.to_xml_string())
