"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.570637, 'e_o_k': [1.070589, 0.856471, 0.685177, 0.548142, 0.438513], 'p_i': 10, 'u_i': 2.3680},
        {'id': 1, 'e_m': 3.479846, 'e_o_k': [2.706547, 2.165238], 'p_i': 20, 'u_i': 4.2120},
        {'id': 2, 'e_m': 5.793520, 'e_o_k': [4.506071, 3.604857], 'p_i': 40, 'u_i': 4.4653},
        {'id': 3, 'e_m': 17.928476, 'e_o_k': [13.944370, 11.155496], 'p_i': 80, 'u_i': 4.6069},
    ]
    B_BUDGET = 176.639993
    return processors, tasks, B_BUDGET
