from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    robot_name = 'ab2'
    
    urdf_path = os.path.join(
        get_package_share_directory('ab2_description'),
        'urdf',
        f'{robot_name}.urdf'
    )

    with open(urdf_path, 'r') as infp:
        robot_description_content = infp.read()

    return LaunchDescription([
        #Node(
        #    package='joint_state_publisher',
        #    executable='joint_state_publisher',
        #    name='joint_state_publisher',
        #    output='screen'
        #),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            #namespace=robot_name,
            output='screen'
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            #namespace=robot_name,
            output='screen',
            parameters=[{
                'robot_description': robot_description_content,
                'publish_frequency': 10.0
            }],
        ),
    ])
