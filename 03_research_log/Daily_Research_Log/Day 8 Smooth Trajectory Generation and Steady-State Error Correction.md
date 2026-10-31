[Research Log - Day 8]
Date: July 8, 2026
Task: Resolving steady-state error and achieving smooth start

Work Accomplished:
1. Analyzed steady-state error: pure feedback control exhibits tracking lag. Introduced a "velocity feedforward + position feedback" control law to anticipate the trajectory.
2. Improved trajectory planning: Adopted Quintic Time Scaling to ensure zero initial and final velocity and acceleration, achieving a smooth, shock-free start.
3. Re-plotted error curves, standardizing the calculation of 3D position errors at the same instant and dimension.

Result Analysis:
Steady-state error was eliminated, and tracking lag was significantly reduced. However, due to independent joint clipping altering the motion direction, the trajectory still exhibited slight distortion in specific regions.