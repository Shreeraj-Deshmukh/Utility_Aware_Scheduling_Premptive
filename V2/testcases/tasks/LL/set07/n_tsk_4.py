"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.202122, 'e_o_k': [0.034235, 0.027388, 0.021910, 0.017528], 'p_i': 10, 'u_i': 3.9662},
        {'id': 1, 'e_m': 0.799851, 'e_o_k': [0.163904, 0.131123, 0.104898], 'p_i': 20, 'u_i': 1.8989},
        {'id': 2, 'e_m': 5.520404, 'e_o_k': [1.533446, 1.226756], 'p_i': 40, 'u_i': 3.5356},
        {'id': 3, 'e_m': 16.142812, 'e_o_k': [2.187800, 1.750240, 1.400192, 1.120153, 0.896123, 0.716898], 'p_i': 80, 'u_i': 1.2138},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
