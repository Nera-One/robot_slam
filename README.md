# robot_slam

Thin robot-specific wrapper around `slam_toolbox`.

This package does not copy SLAM Toolbox launch files. It includes the upstream
`online_async_launch.py` and passes a small robot-specific parameter file for
the NERA simulation topic and frame contract:

- scan: `/scan`
- map frame: `map`
- odom frame: `odom`
- base frame: `base_footprint`

## Mapping

```bash
ros2 launch robot_slam online_mapping.launch.py
```

Run this alongside the simulation sensor producer:

```bash
ros2 launch gazebo_simulation sim.launch.py
```
