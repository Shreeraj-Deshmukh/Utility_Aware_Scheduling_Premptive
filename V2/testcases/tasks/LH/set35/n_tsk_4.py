"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.348629, 'e_o_k': [0.165339, 0.132271, 0.105817, 0.084654], 'p_i': 10, 'u_i': 1.6266},
        {'id': 1, 'e_m': 0.414411, 'e_o_k': [0.322320, 0.257856], 'p_i': 20, 'u_i': 2.5167},
        {'id': 2, 'e_m': 7.679884, 'e_o_k': [2.914346, 2.331477, 1.865181, 1.492145, 1.193716, 0.954973], 'p_i': 40, 'u_i': 3.7793},
        {'id': 3, 'e_m': 12.193553, 'e_o_k': [5.782851, 4.626280, 3.701024, 2.960819], 'p_i': 80, 'u_i': 1.9533},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
