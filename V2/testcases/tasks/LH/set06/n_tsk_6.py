"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319992, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319992, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.763835, 'e_o_k': [0.289858, 0.231887, 0.185509, 0.148407, 0.118726, 0.094981], 'p_i': 10, 'u_i': 4.5754},
        {'id': 1, 'e_m': 1.996751, 'e_o_k': [0.946969, 0.757575, 0.606060, 0.484848], 'p_i': 20, 'u_i': 3.5388},
        {'id': 2, 'e_m': 6.879753, 'e_o_k': [2.610714, 2.088571, 1.670857, 1.336685, 1.069348, 0.855479], 'p_i': 40, 'u_i': 1.2818},
        {'id': 3, 'e_m': 0.145853, 'e_o_k': [0.113441, 0.090753], 'p_i': 80, 'u_i': 2.2300},
        {'id': 4, 'e_m': 0.338485, 'e_o_k': [0.160528, 0.128423, 0.102738, 0.082190], 'p_i': 10, 'u_i': 1.1980},
        {'id': 5, 'e_m': 0.322269, 'e_o_k': [0.152838, 0.122270, 0.097816, 0.078253], 'p_i': 20, 'u_i': 3.9540},
    ]
    B_BUDGET = 88.319992
    return processors, tasks, B_BUDGET
