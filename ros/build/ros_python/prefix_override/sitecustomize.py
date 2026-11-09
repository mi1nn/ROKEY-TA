import sys
if sys.prefix == '/Users/min/miniconda3/envs/ros':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/Users/min/orca/ROKEY-TA/ros/install/ros_python'
