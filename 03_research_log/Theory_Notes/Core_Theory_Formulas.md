[Core Theoretical Formulas and Derivation Notes]

This document summarizes the core mathematical formulas used in the kinematics modeling and task-space control simulation for the 6-DOF robot manipulator.

1. Standard DH Transformation Matrix
   Describes the transformation between consecutive link frames:
   T(i-1 to i) = 
   [ cθi  -sθi*cα(i-1)   sθi*sα(i-1)   a(i-1)*cθi ]
   [ sθi   cθi*cα(i-1)  -cθi*sα(i-1)   a(i-1)*sθi ]
   [ 0     sα(i-1)       cα(i-1)       di         ]
   [ 0     0             0             1          ]

2. Geometric Jacobian Matrix
   Establishes the mapping from joint space velocity to Cartesian space velocity:
   ΔX = J(q) * Δq
   For a revolute joint, the i-th column of the Jacobian is:
   Ji = [ zi-1 x (pe - pi-1) ; zi-1 ]
   The first 3 rows (position part) are extracted for position control: J ∈ R^(3x6).

3. Quintic Time Scaling
   Used to generate smooth trajectories with zero initial and final velocities/accelerations:
   h(s) = 10s^3 - 15s^4 + 6s^5
   ḣ(s) = (30s^2 - 60s^3 + 30s^4) / T_total
   where s = t / T_total is the normalized time.

4. Task-Space Feedforward + P Feedback Control Law
   The Cartesian velocity command is computed as:
   dx_cmd = v_d + Kp * e
   where v_d is the feedforward velocity, e is the 3D position error, and Kp is the diagonal proportional gain matrix.

5. Adaptive Damped Least Squares (DLS)
   Used to resolve inverse kinematics near singularities. The damping factor λ is adjusted adaptively based on the minimum singular value σ_min:
   ratio = clip(σ_min / σ_threshold, 0, 1)
   λ = λ_min + (λ_max - λ_min) * (1 - ratio^2)
   Joint velocity resolution: dq = J^T * (J*J^T + λ^2*I_3)^(-1) * dx_cmd
   (Project parameters: σ_threshold=0.03, λ_min=1e-4, λ_max=0.02)

6. Global Speed Scaling
   Preserves the direction of the end-effector motion by scaling all joint velocities uniformly:
   speed_scale = max(1.0, max(|dq|) / dq_max)
   dq = dq / speed_scale
   (Project parameter: dq_max = 1.5 rad/s)