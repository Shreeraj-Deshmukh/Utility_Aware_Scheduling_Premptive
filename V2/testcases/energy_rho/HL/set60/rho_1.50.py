"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 128.799998, "H": 80, "J": 35, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.5, "seed": 1060, "set": 60, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.50"}
"""

_SPEC = '{"B": 128.799998, "H": 80, "J": 35, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.5, "seed": 1060, "set": 60, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.456621, 'e_o_k': [0.246718, 0.197374, 0.157899, 0.126319], 'p_i': 10, 'u_i': 4.9967},
        {'id': 1, 'e_m': 6.472983, 'e_o_k': [1.326431, 1.061145, 0.848916], 'p_i': 20, 'u_i': 3.1686},
        {'id': 2, 'e_m': 1.070031, 'e_o_k': [0.219269, 0.175415, 0.140332], 'p_i': 40, 'u_i': 1.4833},
        {'id': 3, 'e_m': 9.500976, 'e_o_k': [1.287646, 1.030117, 0.824094, 0.659275, 0.527420, 0.421936], 'p_i': 80, 'u_i': 1.9048},
        {'id': 4, 'e_m': 0.365435, 'e_o_k': [0.101510, 0.081208], 'p_i': 40, 'u_i': 4.4078},
        {'id': 5, 'e_m': 0.184044, 'e_o_k': [0.037714, 0.030171, 0.024137], 'p_i': 10, 'u_i': 3.6020},
        {'id': 6, 'e_m': 5.282667, 'e_o_k': [0.894761, 0.715809, 0.572647, 0.458117], 'p_i': 40, 'u_i': 4.8789},
        {'id': 7, 'e_m': 0.255688, 'e_o_k': [0.043308, 0.034646, 0.027717, 0.022173], 'p_i': 10, 'u_i': 3.0372},
    ]
    B_BUDGET = 128.799998
    return processors, tasks, B_BUDGET
