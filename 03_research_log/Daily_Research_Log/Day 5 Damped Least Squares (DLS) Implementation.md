[Research Log - Day 5]
Date: July 5, 2026
Task: Inverse velocity algorithm optimization

Work Accomplished:
1. Implemented the Damped Least Squares (DLS) method in the 02_jacobian_dls_test.ipynb notebook.
2. Established a velocity limiting strategy to prevent excessively high joint velocities.
3. Compared the performance of the standard pseudo-inverse versus DLS under singular configurations.

Result Analysis:
The standard pseudo-inverse generated joint velocities exceeding 100 rad/s near singularities, whereas the DLS method successfully constrained velocities within a safe range by introducing a damping factor λ. DLS was confirmed as the core algorithm for inverse kinematics resolution.