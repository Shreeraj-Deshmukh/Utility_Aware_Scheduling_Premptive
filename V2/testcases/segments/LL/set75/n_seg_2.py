"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200006, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200006, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.446887, 'e_o_k': [0.124135, 0.099308], 'p_i': 10, 'u_i': 4.1325},
        {'id': 1, 'e_m': 0.001026, 'e_o_k': [0.000285, 0.000228], 'p_i': 20, 'u_i': 2.4718},
        {'id': 2, 'e_m': 6.562599, 'e_o_k': [1.822944, 1.458355], 'p_i': 40, 'u_i': 2.6491},
        {'id': 3, 'e_m': 2.341741, 'e_o_k': [0.650483, 0.520387], 'p_i': 80, 'u_i': 3.7785},
        {'id': 4, 'e_m': 0.177678, 'e_o_k': [0.049355, 0.039484], 'p_i': 10, 'u_i': 2.0110},
        {'id': 5, 'e_m': 0.341853, 'e_o_k': [0.094959, 0.075967], 'p_i': 10, 'u_i': 2.7392},
        {'id': 6, 'e_m': 6.037977, 'e_o_k': [1.677216, 1.341773], 'p_i': 80, 'u_i': 4.5700},
        {'id': 7, 'e_m': 0.689911, 'e_o_k': [0.191642, 0.153314], 'p_i': 20, 'u_i': 2.3393},
    ]
    B_BUDGET = 55.200006
    return processors, tasks, B_BUDGET
