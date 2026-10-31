[Research Log - Day 4]
Date: July 4, 2026
Task: Geometric Jacobian matrix and singularity analysis

Work Accomplished:
1. Derived the 6x6 geometric Jacobian matrix in the base coordinate frame.
2. Computed the Jacobian matrix of PUMA560 at the zero configuration and applied Singular Value Decomposition (SVD).
3. Introduced the Yoshikawa manipulability index to analyze singular configurations (e.g., fully extended arm, aligned wrist).

Result Analysis:
It was found that as the robot approaches a singularity, the minimum singular value of the Jacobian approaches zero rapidly. Directly using the pseudo-inverse to solve for joint velocities at this point generates physically impossible, extremely high-velocity commands, causing controller failure. Damped Least Squares (DLS) was planned for the subsequent design.