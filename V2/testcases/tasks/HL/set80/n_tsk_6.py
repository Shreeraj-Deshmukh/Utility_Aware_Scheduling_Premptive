"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.356968, 'e_o_k': [0.060462, 0.048370, 0.038696, 0.030957], 'p_i': 10, 'u_i': 4.6156},
        {'id': 1, 'e_m': 0.792605, 'e_o_k': [0.134249, 0.107399, 0.085919, 0.068735], 'p_i': 20, 'u_i': 1.3815},
        {'id': 2, 'e_m': 1.215817, 'e_o_k': [0.249143, 0.199314, 0.159451], 'p_i': 40, 'u_i': 2.2542},
        {'id': 3, 'e_m': 26.585889, 'e_o_k': [3.603127, 2.882502, 2.306001, 1.844801, 1.475841, 1.180673], 'p_i': 80, 'u_i': 3.1493},
        {'id': 4, 'e_m': 6.230606, 'e_o_k': [1.055319, 0.844256, 0.675404, 0.540324], 'p_i': 20, 'u_i': 4.3022},
        {'id': 5, 'e_m': 4.033887, 'e_o_k': [0.546704, 0.437363, 0.349890, 0.279912, 0.223930, 0.179144], 'p_i': 80, 'u_i': 4.8493},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET
