6-DOF Robot Kinematics and Task-Space Control Research

This repository contains the complete independent research project on the kinematics modeling and task-space closed-loop 3D position control for a 6-DOF PUMA 560 serial robot manipulator.

Project Highlights
Kinematics: Standard Denavit-Hartenberg (DH) modeling and geometric Jacobian derivation.
Control Strategy: Velocity feedforward + Proportional (P) feedback control.
Optimization: Adaptive Damped Least Squares (DLS) for singularity handling, Quintic Time Scaling for smooth trajectory generation, and Global Speed Scaling.
Result: Achieved a highly precise sub-millimeter tracking error (Maximum: 0.1393 mm, RMS: 0.0840 mm).

Repository Structure
01_code_src/: Core Python source files for kinematics and control.
02_notebooks/: Jupyter Notebooks containing simulations and data visualization.
03_research_log/: Daily research logs and detailed debugging records.
04_paper_overleaf/: LaTeX source code and the final research paper (PDF).
05_literature/: Reference notes.

Tools Used
Python, NumPy, SciPy, Matplotlib, Robotics Toolbox for Python.
