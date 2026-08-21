"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.40001, "H": 80, "J": 35, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.40001, "H": 80, "J": 35, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.456621, 'e_o_k': [0.334702, 0.200821, 0.120493, 0.072296], 'p_i': 10, 'u_i': 4.9967},
        {'id': 1, 'e_m': 6.472983, 'e_o_k': [1.651271, 0.990763, 0.594458], 'p_i': 20, 'u_i': 3.1686},
        {'id': 2, 'e_m': 1.070031, 'e_o_k': [0.272967, 0.163780, 0.098268], 'p_i': 40, 'u_i': 1.4833},
        {'id': 3, 'e_m': 9.500976, 'e_o_k': [1.993189, 1.195914, 0.717548, 0.430529, 0.258317, 0.154990], 'p_i': 80, 'u_i': 1.9048},
        {'id': 4, 'e_m': 0.365435, 'e_o_k': [0.114199, 0.068519], 'p_i': 40, 'u_i': 4.4078},
        {'id': 5, 'e_m': 0.184044, 'e_o_k': [0.046950, 0.028170, 0.016902], 'p_i': 10, 'u_i': 3.6020},
        {'id': 6, 'e_m': 5.282667, 'e_o_k': [1.213848, 0.728309, 0.436985, 0.262191], 'p_i': 40, 'u_i': 4.8789},
        {'id': 7, 'e_m': 0.255688, 'e_o_k': [0.058752, 0.035251, 0.021151, 0.012690], 'p_i': 10, 'u_i': 3.0372},
    ]
    B_BUDGET = 110.400010
    return processors, tasks, B_BUDGET
