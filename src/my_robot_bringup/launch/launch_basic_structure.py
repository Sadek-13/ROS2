from launch import LaunchDescription 
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    first_node_name = Node(
        package="",
        executable=""
    )
    
    second_node_name = Node(
        package="",
        executable=""
    )
    
    
    ld.add_action(first_node_name)
    ld.add_action(second_node_name)
    return ld