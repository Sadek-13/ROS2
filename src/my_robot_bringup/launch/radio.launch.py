from launch import LaunchDescription 
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    robot_news= ["Giskard", "BB8", "Dannel", "Jander", "C3P0"]
    
    robot_news_station_nodes = []
    
    for name in robot_news:
        robot_news_station_nodes.append(Node(
            package= "my_py_pkg",
            executable= "robot_news_station",
            name= "robot_news_station" + name.lower(),
            parameters=[{"robot_news": name}]
        ))
    
    Smartphone = Node(
        package="my_py_pkg",
        executable="smartphone",
        name="Smartphone"
    )
    
    for node in robot_news_station_nodes:
        ld.add_action(node)
    ld.add_action(Smartphone)
    return ld