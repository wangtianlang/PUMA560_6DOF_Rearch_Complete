import numpy as np
from dh_kinematics import forward_kinematics
from jacobian_ik import numerical_jacobian

# PID控制器
class CartesianPID:
    def __init__(self, Kp=2.5, Ki=0.15, Kd=0.6):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.integral = np.zeros(3)
        self.last_err = np.zeros(3)

    def compute(self, err, dt):
        self.integral += err * dt
        derr = (err - self.last_err) / dt
        self.last_err = err.copy()
        vel_cmd = self.Kp * err + self.Ki * self.integral + self.Kd * derr
        return vel_cmd

# DLS求解关节增量
def dls_delta_q(q, vel_cmd, lam=0.01):
    J = numerical_jacobian(q)
    JJT = J @ J.T
    inv_mat = np.linalg.inv(JJT + lam**2 * np.eye(3))
    dq = J.T @ inv_mat @ vel_cmd
    return dq