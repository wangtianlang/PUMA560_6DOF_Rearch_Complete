[Research Log - Day 7]
Date: July 7, 2026
Task: Trajectory tracking divergence diagnosis and correction

Work Accomplished:
1. Diagnosed the causes of divergence: excessive initial error leading to integral windup; high PD gains causing high-frequency oscillation; pseudo-inverse causing velocity explosion near singularities.
2. Implemented corrections:
   - Removed the derivative term (D) and reduced proportional feedback gain.
   - Introduced an anti-windup mechanism for the integral term.
   - Added joint velocity limiting.
3. Re-ran the simulation.

Result Analysis:
The trajectory no longer diverged, and the controller stabilized. However, the actual trajectory (blue line) failed to complete a full circle, and the position error got stuck at 0.05m without decreasing further, exhibiting "steady-state error" and localized "stalling."