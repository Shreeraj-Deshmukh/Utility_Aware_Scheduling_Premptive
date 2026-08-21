"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.76001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.76001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.612548, 'e_o_k': [0.131127, 0.104902, 0.083921, 0.067137, 0.053710, 0.042968], 'p_i': 10, 'u_i': 3.8590},
        {'id': 1, 'e_m': 0.207665, 'e_o_k': [0.018533, 0.014826, 0.011861, 0.009489, 0.007591], 'p_i': 20, 'u_i': 3.6983},
        {'id': 2, 'e_m': 0.777677, 'e_o_k': [0.069402, 0.055522, 0.044418, 0.035534, 0.028427], 'p_i': 40, 'u_i': 3.0670},
        {'id': 3, 'e_m': 0.196245, 'e_o_k': [0.032708, 0.026166], 'p_i': 80, 'u_i': 2.2547},
        {'id': 4, 'e_m': 9.490767, 'e_o_k': [1.581794, 1.265436], 'p_i': 80, 'u_i': 3.3628},
        {'id': 5, 'e_m': 0.126599, 'e_o_k': [0.021100, 0.016880], 'p_i': 10, 'u_i': 1.9431},
        {'id': 6, 'e_m': 1.959380, 'e_o_k': [0.174861, 0.139889, 0.111911, 0.089529, 0.071623], 'p_i': 80, 'u_i': 4.2381},
        {'id': 7, 'e_m': 2.506802, 'e_o_k': [0.308213, 0.246571, 0.197257], 'p_i': 10, 'u_i': 1.5683},
    ]
    B_BUDGET = 71.760010
    return processors, tasks, B_BUDGET
