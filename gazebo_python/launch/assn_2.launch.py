from launch import LaunchDescription
from launch_ros.actions import Node
import os
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
	
	pkg_project = get_package_share_directory('gazebo_python')
	pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')

	gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),
        launch_arguments={'gz_args': os.path.join(pkg_project, 'models', 'assn_2.sdf')}.items(),
    	)
	
	bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/world/empty/model/assn_2/joint_state@sensor_msgs/msg/JointState@ignition.msgs.Model',
    				'/clock@rosgraph_msgs/Clock@ignition.msgs.Clock'],
        output='screen'
    )

	return LaunchDescription([
		gz_sim,
		bridge
		])