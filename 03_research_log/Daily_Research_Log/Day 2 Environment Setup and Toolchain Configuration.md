[Research Log - Day 2]
Date: July 2, 2026
Task: Setting up the independent development environment

Work Accomplished:
1. Downloaded and installed Python 3.12.9. Ensured "Add Python to PATH" and "Disable path length limit" were selected during installation.
2. Created a virtual environment (.venv) in the project directory and installed core scientific libraries via pip: numpy, scipy, matplotlib, and roboticstoolbox-python.
3. Configured VS Code by installing the Python and Jupyter extensions, successfully linking the workspace to the .venv environment.

Issues & Solutions:
Encountered a syntax error while creating the virtual environment by mistakenly typing `python --m venv`. Corrected the parameter to `-m` after consulting the documentation. The PUMA560 model loaded successfully in the initial test script.