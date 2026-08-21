"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680015, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680015, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.893774, 'e_o_k': [0.109890, 0.087912, 0.070330], 'p_i': 10, 'u_i': 4.1325},
        {'id': 1, 'e_m': 0.002051, 'e_o_k': [0.000208, 0.000167, 0.000133, 0.000107], 'p_i': 20, 'u_i': 2.4718},
        {'id': 2, 'e_m': 13.125199, 'e_o_k': [1.067298, 0.853838, 0.683070, 0.546456, 0.437165, 0.349732], 'p_i': 40, 'u_i': 1.1369},
        {'id': 3, 'e_m': 4.683481, 'e_o_k': [0.475964, 0.380771, 0.304617, 0.243693], 'p_i': 80, 'u_i': 2.0116},
        {'id': 4, 'e_m': 0.355356, 'e_o_k': [0.028896, 0.023117, 0.018494, 0.014795, 0.011836, 0.009469], 'p_i': 10, 'u_i': 3.8042},
        {'id': 5, 'e_m': 0.683705, 'e_o_k': [0.069482, 0.055586, 0.044469, 0.035575], 'p_i': 10, 'u_i': 3.9295},
        {'id': 6, 'e_m': 12.075953, 'e_o_k': [1.484748, 1.187799, 0.950239], 'p_i': 80, 'u_i': 2.7392},
        {'id': 7, 'e_m': 1.379822, 'e_o_k': [0.112203, 0.089762, 0.071810, 0.057448, 0.045958, 0.036767], 'p_i': 20, 'u_i': 3.4812},
    ]
    B_BUDGET = 95.680015
    return processors, tasks, B_BUDGET
