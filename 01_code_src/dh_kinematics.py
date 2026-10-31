# dh_kinematics.py
import numpy as np

def dh_transform(a, alpha, d, theta):
    ct = np.cos(theta)
    st = np.sin(theta)
    ca = np.cos(alpha)
    sa = np.sin(alpha)
    T = np.array([
        [ct, -st*ca, st*sa, a*ct],
        [st, ct*ca, -ct*sa, a*st],
        [0, sa, ca, d],
        [0, 0, 0, 1]
    ])
    return T

def forward_kinematics(joint_angles):
    dh_table = [
        [0,    np.pi/2, 0.15, joint_angles[0]],
        [0.35, 0,       0,    joint_angles[1]],
        [0.35, 0,       0,    joint_angles[2]],
        [0,    np.pi/2, 0.12, joint_angles[3]],
        [0,   -np.pi/2, 0.12, joint_angles[4]],
        [0,    0,       0.12, joint_angles[5]]
    ]
    T_total = np.eye(4)
    for row in dh_table:
        a, alpha, d, theta = row
        T_link = dh_transform(a, alpha, d, theta)
        T_total = T_total @ T_link
    xyz = T_total[:3, 3]
    return T_total, xyz