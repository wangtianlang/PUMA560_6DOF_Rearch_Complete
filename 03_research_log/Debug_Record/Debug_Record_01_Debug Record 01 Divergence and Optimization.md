[Debug Record - Part 01: Trajectory Divergence and Initial Debugging]
Date: July 6, 2026 - July 8, 2026
Related File: 02_notebooks/03_circular_trajectory_pid.ipynb
Author: Wang Tianlang

1. Initial Failure and Divergence
1.1 Phenomenon
The initial simulation of the task-space closed-loop PID controller completely diverged. The actual trajectory (blue line) failed to track the desired trajectory (red dashed line) and spread out violently. The position error oscillated between 0.2m and 1.4m, indicating a total loss of control.

1.2 Cause Analysis
Three primary causes were identified:
1. Singularity-induced velocity explosion. The initial joint angle (puma.qn) was close to an arm singularity, making the Jacobian matrix ill-conditioned. The standard pseudoinverse (np.linalg.pinv) generated physically impossible joint velocities, causing numerical integration to diverge instantly.
2. Excessive initial error and integral windup. The large distance between the initial pose and the desired circular center caused a massive instantaneous position error (e_p). The integral term accumulated this error, driving the controller output far beyond reasonable limits.
3. Overly high attitude gain. The attitude error calculation caused self-excited oscillation, and the high gain (50) led to high-frequency chattering.

1.3 Initial Solutions
1. Replaced the standard pseudoinverse with Damped Least Squares (DLS), introducing a damping factor (lambda = 0.1) to suppress joint velocity jumps near singularities.
2. Applied joint velocity limiting (np.clip(dq, -1.0, 1.0)) to prevent numerical integration overflow.
3. Retuned the controller: reduced position gain (100 to 50), drastically reduced attitude gain (50 to 5), and set the integral gain to zero (Ki = 0) to eliminate integral windup.
4. Adjusted the trajectory starting point to align with the robot's initial state, eliminating the initial transient shock.

1.4 First Result
The trajectory stopped diverging, but a new issue appeared: the actual trajectory (blue line) failed to complete a full circle and got stuck at a local point. The position error remained at approximately 0.05m and stopped decreasing.


2. Steady-State Error and Display Issues
2.1 Phenomenon
1. Steady-state error: The trajectory got stuck at 0.05m, unable to complete the circle.
2. Matplotlib warnings and encoding issues: Glyph warnings appeared, and Chinese titles/labels in the plot appeared as squares.

2.2 Cause Analysis
1. Steady-state error: The integral gain (Ki) was zero, and the velocity limit was too strict (plus or minus 1.0 rad/s). Pure PD control cannot eliminate steady-state error. The strict velocity limit prevented the robot from generating enough speed to reach the target when far away.
2. Encoding issue: The default Matplotlib font did not support Chinese characters.

2.3 Solutions
1. Restored a small integral term (e.g., Ki = 0.5) with anti-windup protection (np.clip(integral_e, -1.0, 1.0)).
2. Applied error clipping (np.clip(e, -0.1, 0.1)) to prevent integral explosion during the initial phase.
3. Relaxed the joint velocity limit to plus or minus 2.0 rad/s to ensure enough power to complete the circle.
4. Added Chinese font support (plt.rcParams['font.sans-serif'] = ['SimHei']).


3. Workspace, Singularity, and Dimensionality Reduction
3.1 Further Debugging Attempts
1. Workspace and Initial Pose Optimization: Used puma.qr (Ready Pose) and fixed the circular center at [0.5, 0, 0.5]. Result: The robot failed to move.
2. IK Initial State Failure: Attempted to use inverse kinematics (puma.ikine_LM) to position the robot at the trajectory start. Result: IK failed, and the robot reverted to the default pose.
3. Singularity Avoidance and Dimensionality Reduction: In puma.qr, the robot was near wrist singularity (theta5 = 0), causing Jacobian rank deficiency. Solution: Switched to a safe pose [0, -pi/4, pi/4, 0, pi/4, 0] and reduced control to 3-DOF position (X, Y, Z) only, ignoring attitude errors. Continued using DLS. Result: Trajectory stabilized, but initial error persisted.


4. Major Breakthrough: Zero Initial Error and Smooth Start
4.1 Phenomenon
Previous debugging was always stuck on the initial error. The robot would either experience velocity explosion due to a sudden jump or fail to catch up and get stuck.

4.2 Cause Analysis
The starting point of the desired trajectory did not coincide with the robot's current end-effector position, creating a massive instantaneous step error.

4.3 Final Solutions
1. Zero Initial Error Strategy: Set the circle center to start - [radius, 0, 0], ensuring the desired trajectory starts exactly from the robot's current end-effector position at t = 0.
2. Quintic Time Scaling: Adopted h(s) = 10s^3 - 15s^4 + 6s^5, ensuring zero initial and final velocity and acceleration, achieving a smooth, shock-free start.
3. Feedforward + P Feedback: Changed the control law to dx_cmd = v_d + Kp * e, eliminating tracking lag.
4. Adaptive DLS and Global Speed Scaling: Dynamically adjusted the damping factor based on the minimum singular value and scaled joint velocities proportionally instead of independent clipping.

4.4 Final Result
The maximum position error was reduced from approximately 73 mm to 0.1393 mm. The actual trajectory (blue line) perfectly overlapped the desired circular trajectory (red dashed line). The minimum Jacobian singular value remained safe (0.239915), and no speed scaling was triggered throughout the 500 steps (0/500). The controller demonstrated excellent stability and robustness.



[Debug Record - Part 02: Comprehensive Controller Optimization]
Date: July 8, 2026
Related File: 02_notebooks/03_circular_trajectory_pid.ipynb
Author: Wang Tianlang

1. Background and Summary
Although the initial task-space PID controller achieved basic tracking, it exhibited oscillation, steady-state error, and singularity divergence. This optimization focused on control parameters, feedforward mechanisms, singularity handling, velocity limiting, and trajectory planning.

2. Specific Optimization Measures and Principles

2.1 Control Parameter and Structure Optimization
Problem: High PD gains applied directly to end-effector velocity caused severe oscillation.
Solution: Removed the derivative term (D), reduced proportional gain, and adopted a smoother feedback structure to eliminate high-frequency chattering.

2.2 Introduction of Target Velocity Feedforward
Problem: Pure position feedback exhibited tracking lag and steady-state error.
Solution: Adopted a composite Feedforward plus P Feedback strategy. The feedforward term provides the nominal trajectory velocity, while the feedback term only corrects small deviations, achieving smooth tracking and accurate correction.

2.3 Singularity Avoidance and Stable Resolution
Problem: Standard pseudoinverse produced extremely high joint velocities near singularities.
Solution: Replaced with Adaptive Damped Least Squares (DLS). Dynamically adjusted the damping factor based on the minimum Jacobian singular value to monitor stability.

2.4 Velocity Limiting Strategy Optimization
Problem: Independent joint clipping altered joint velocity ratios and distorted the end-effector trajectory.
Solution: Switched to Global Speed Scaling. Joint velocities are scaled proportionally if the maximum velocity exceeds the limit, preserving the direction of the end-effector motion.

2.5 Smooth Trajectory Start
Problem: The original trajectory had continuous position but non-zero initial velocity, causing shock and lag.
Solution: Applied Quintic Time Scaling, ensuring zero initial and final velocity and acceleration for a smooth, shock-free start.

2.6 Error Evaluation and Plotting Standardization
Problem: Error plots had overlapping curves and inconsistent time steps.
Solution: Calculated the 3D position error norm at the same instant, standardized log lengths and time sequences, used a new figure canvas for each plot, and specified error units (mm).

3. Optimization Results and Conclusion
Accuracy Improvement: Maximum position error reduced from 73 mm to 0.1393 mm. The actual trajectory (blue line) and desired trajectory (red dashed line) perfectly overlapped.
Stability Improvement: The minimum Jacobian singular value remained within a safe range throughout. Speed scaling was never triggered, indicating a highly stable and robust controller.

4. Future Work
Organize the optimized code and data figures, and proceed to the paper writing phase (04_paper_overleaf).