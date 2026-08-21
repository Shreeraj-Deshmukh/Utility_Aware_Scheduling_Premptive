"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 125.119998, "H": 80, "J": 35, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.5, "seed": 1060, "set": 60, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.50"}
"""

_SPEC = '{"B": 125.119998, "H": 80, "J": 35, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.5, "seed": 1060, "set": 60, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.456621, 'e_o_k': [0.690810, 0.552648, 0.442118, 0.353695], 'p_i': 10, 'u_i': 4.9967},
        {'id': 1, 'e_m': 6.472983, 'e_o_k': [3.714006, 2.971205, 2.376964], 'p_i': 20, 'u_i': 3.1686},
        {'id': 2, 'e_m': 1.070031, 'e_o_k': [0.613952, 0.491162, 0.392929], 'p_i': 40, 'u_i': 1.4833},
        {'id': 3, 'e_m': 9.500976, 'e_o_k': [3.605410, 2.884328, 2.307462, 1.845970, 1.476776, 1.181421], 'p_i': 80, 'u_i': 1.9048},
        {'id': 4, 'e_m': 0.365435, 'e_o_k': [0.284228, 0.227382], 'p_i': 40, 'u_i': 4.4078},
        {'id': 5, 'e_m': 0.184044, 'e_o_k': [0.105599, 0.084479, 0.067583], 'p_i': 10, 'u_i': 3.6020},
        {'id': 6, 'e_m': 5.282667, 'e_o_k': [2.505330, 2.004264, 1.603411, 1.282729], 'p_i': 40, 'u_i': 4.8789},
        {'id': 7, 'e_m': 0.255688, 'e_o_k': [0.121261, 0.097009, 0.077607, 0.062086], 'p_i': 10, 'u_i': 3.0372},
    ]
    B_BUDGET = 125.119998
    return processors, tasks, B_BUDGET
