"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639994, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639994, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.067388, 'e_o_k': [0.052413, 0.041931], 'p_i': 10, 'u_i': 2.5143},
        {'id': 1, 'e_m': 5.132687, 'e_o_k': [2.137602, 1.710081, 1.368065, 1.094452, 0.875562], 'p_i': 20, 'u_i': 1.6130},
        {'id': 2, 'e_m': 7.548845, 'e_o_k': [4.331304, 3.465043, 2.772035], 'p_i': 40, 'u_i': 1.3758},
        {'id': 3, 'e_m': 1.400496, 'e_o_k': [0.803563, 0.642850, 0.514280], 'p_i': 80, 'u_i': 3.6848},
        {'id': 4, 'e_m': 3.078148, 'e_o_k': [2.394115, 1.915292], 'p_i': 10, 'u_i': 1.6851},
        {'id': 5, 'e_m': 0.451694, 'e_o_k': [0.188116, 0.150493, 0.120394, 0.096316, 0.077052], 'p_i': 20, 'u_i': 1.3700},
    ]
    B_BUDGET = 176.639994
    return processors, tasks, B_BUDGET
