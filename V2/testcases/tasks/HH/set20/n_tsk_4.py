"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.135760, 'e_o_k': [2.372977, 1.898381, 1.518705], 'p_i': 10, 'u_i': 2.1828},
        {'id': 1, 'e_m': 2.474534, 'e_o_k': [1.419814, 1.135851, 0.908681], 'p_i': 20, 'u_i': 3.4051},
        {'id': 2, 'e_m': 6.247662, 'e_o_k': [2.962983, 2.370387, 1.896309, 1.517047], 'p_i': 40, 'u_i': 2.6596},
        {'id': 3, 'e_m': 8.520465, 'e_o_k': [3.233328, 2.586662, 2.069330, 1.655464, 1.324371, 1.059497], 'p_i': 80, 'u_i': 2.1030},
    ]
    B_BUDGET = 176.639997
    return processors, tasks, B_BUDGET
