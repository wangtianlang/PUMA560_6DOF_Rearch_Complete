import numpy as np
from dh_kinematics import forward_kinematics

# 微小扰动，数值微分求雅可比
delta = 1e-6

def numerical_jacobian(q):
    n = len(q)
    _, x0 = forward_kinematics(q)
    J = np.zeros((3, n))
    for i in range(n):
        q_pert = q.copy()
        q_pert[i] += delta
        _, x_pert = forward_kinematics(q_pert)
        J[:, i] = (x_pert - x0) / delta
    return J

def dls_inverse_kinematics(q_init, x_target, max_iter=100, tol=1e-4, lam=0.01):
    q = np.array(q_init, dtype=float)
    I = np.eye(3)
    for _ in range(max_iter):
        _, x_current = forward_kinematics(q)
        err = x_target - x_current
        if np.linalg.norm(err) < tol:
            break
        J = numerical_jacobian(q)
        # DLS核心公式
        JJT = J @ J.T
        damped_inv = np.linalg.inv(JJT + lam**2 * I)
        dq = J.T @ damped_inv @ err
        q += dq
    return q