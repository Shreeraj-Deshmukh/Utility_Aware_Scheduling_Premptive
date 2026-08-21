"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639994, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639994, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.201708, 'e_o_k': [0.456021, 0.364817, 0.291854, 0.233483, 0.186786, 0.149429], 'p_i': 10, 'u_i': 4.4924},
        {'id': 1, 'e_m': 2.441029, 'e_o_k': [1.400591, 1.120473, 0.896378], 'p_i': 20, 'u_i': 4.2054},
        {'id': 2, 'e_m': 17.653473, 'e_o_k': [7.352113, 5.881690, 4.705352, 3.764282, 3.011425], 'p_i': 40, 'u_i': 2.8306},
        {'id': 3, 'e_m': 1.130039, 'e_o_k': [0.878920, 0.703136], 'p_i': 80, 'u_i': 2.8504},
        {'id': 4, 'e_m': 0.811483, 'e_o_k': [0.307940, 0.246352, 0.197081, 0.157665, 0.126132, 0.100906], 'p_i': 10, 'u_i': 1.4385},
        {'id': 5, 'e_m': 1.693371, 'e_o_k': [0.642597, 0.514077, 0.411262, 0.329009, 0.263208, 0.210566], 'p_i': 80, 'u_i': 4.3024},
    ]
    B_BUDGET = 176.639994
    return processors, tasks, B_BUDGET
