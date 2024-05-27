# from launch import LaunchDescription
# from ament_index_python.packages import get_package_share_directory
# from launch_ros.actions import Node
# import os.path

# def generate_launch_description():
#     pkg_project = get_package_share_directory('gazebo_python')
    
#     return LaunchDescription([
#         Node(
#              package='rviz2',
#              namespace='',
#              executable='rviz2',
#              name='rviz2',
#             arguments=['-d', os.path.join(pkg_project, 'configs', 'custom.rviz')]
#         )
#     ])


# import os.path

# from ament_index_python.packages import get_package_share_directory
# from launch import LaunchDescription
# from launch.actions import DeclareLaunchArgument, OpaqueFunction
# from launch.conditions import IfCondition
# from launch.substitutions import LaunchConfiguration
# from launch_ros.actions import Node


# def generate_launch_description():

#     declared_arguments = []
#     declared_arguments.append(
#         DeclareLaunchArgument(
#                 'sdf_file',
#                 description='The name of the robot sdf model.'
#             )
#     )
#     declared_arguments.append(
#         DeclareLaunchArgument(
#                 'rviz',
#                 default_value='true',
#                 description='Open RViz.'
#             )
#     )
#     return LaunchDescription(
#         declared_arguments + [OpaqueFunction(function=launch_setup)]
#     )

# def launch_setup(context, *args, **kwargs):
#     sdf_file = LaunchConfiguration('sdf_file')
#     rviz_launch_arg = LaunchConfiguration('rviz')

#     # Get the parser plugin convert sdf to urdf using robot_description topic
#     with open(sdf_file.perform(context), 'r') as infp:
#         robot_desc = infp.read()
#     robot_state_publisher = Node(
#         package='robot_state_publisher',
#         executable='robot_state_publisher',
#         name='robot_state_publisher',
#         parameters=[
#             {'use_sim_time': True},
#             {'robot_description': robot_desc},
#         ]
#     )

#     joint_state_sliders = Node(
#          package="joint_state_publisher_gui",
#         executable="joint_state_publisher_gui",
#          name="joint_state_publisher_gui",
#     )

#     # Launch rviz
#     rviz_config = os.path.join(get_package_share_directory('gazebo_python'),'configs', 'custom.rviz')
#     rviz = Node(
#         package='rviz2',
#         executable='rviz2',
#         arguments=['-d', rviz_config],
#         condition=IfCondition(rviz_launch_arg),
#         parameters=[
#             {'use_sim_time': True},
#         ]
#     )

#     return [
#         #joint_state_sliders,
#         robot_state_publisher,
#         rviz
#     ]
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
    sdf_file = os.path.join(pkg_project, 'models', 'assn_2.sdf')
    
    with open(sdf_file, 'r') as infp:
        robot_desc = infp.read()			
         
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='both',
        parameters=[
            {'use_sim_time': True},
            {'robot_description': robot_desc}
        ],
        remappings=[
            ('/robot_description', '/sdformat_urdf/robot_description')
        ]
    ) 	 		

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_project, 'launch', 'assn_2.launch.py')),
            launch_arguments={'sdf': sdf_file}.items()
    	)
    
   
        
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', os.path.join(pkg_project, 'configs', 'custom.rviz')],
        output='screen'
    )	        

    return LaunchDescription([
        robot_state_publisher,
        rviz,	
        gz_sim            
       
        
    ])