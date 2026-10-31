[Research Log - Day 6]
Date: July 6, 2026
Task: Task-space closed-loop PID controller design

Work Accomplished:
1. Designed a Cartesian space PID control law: generating velocity correction commands based on position error.
2. Mapped commands to joint space: `dq = pinv(J) * dx_cmd`.
3. Developed the circular trajectory tracking simulation script (03_circular_trajectory_pid.ipynb).

Issues & Reflections:
The initial controller applied high PD gains directly to end-effector velocity control, overlooking the large initial pose error. In the first simulation, the end-effector trajectory completely diverged, resembling a tangled mess. The causes of this divergence required comprehensive debugging.