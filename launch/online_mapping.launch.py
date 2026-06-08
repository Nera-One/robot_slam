import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    pkg_robot_slam = get_package_share_directory("robot_slam")
    pkg_slam_toolbox = get_package_share_directory("slam_toolbox")

    slam_params_file = LaunchConfiguration("slam_params_file")
    use_sim_time = LaunchConfiguration("use_sim_time")
    autostart = LaunchConfiguration("autostart")
    use_lifecycle_manager = LaunchConfiguration("use_lifecycle_manager")

    default_params_file = os.path.join(
        pkg_robot_slam,
        "config",
        "online_mapping.yaml",
    )
    slam_toolbox_launch = os.path.join(
        pkg_slam_toolbox,
        "launch",
        "online_async_launch.py",
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "slam_params_file",
                default_value=default_params_file,
                description="Robot-specific SLAM Toolbox parameter file.",
            ),
            DeclareLaunchArgument(
                "use_sim_time",
                default_value="true",
                description="Use simulation clock.",
            ),
            DeclareLaunchArgument(
                "autostart",
                default_value="true",
                description="Configure and activate SLAM Toolbox automatically.",
            ),
            DeclareLaunchArgument(
                "use_lifecycle_manager",
                default_value="false",
                description="Let an external lifecycle manager activate SLAM Toolbox.",
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(slam_toolbox_launch),
                launch_arguments={
                    "slam_params_file": slam_params_file,
                    "use_sim_time": use_sim_time,
                    "autostart": autostart,
                    "use_lifecycle_manager": use_lifecycle_manager,
                }.items(),
            ),
        ]
    )
