"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279992, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279992, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.378632, 'e_o_k': [0.212277, 0.169821, 0.135857, 0.108686, 0.086949], 'p_i': 10, 'u_i': 1.8232},
        {'id': 1, 'e_m': 3.776179, 'e_o_k': [0.336998, 0.269599, 0.215679, 0.172543, 0.138035], 'p_i': 20, 'u_i': 4.2323},
        {'id': 2, 'e_m': 12.009601, 'e_o_k': [1.071775, 0.857420, 0.685936, 0.548749, 0.438999], 'p_i': 40, 'u_i': 3.7021},
        {'id': 3, 'e_m': 10.048209, 'e_o_k': [1.235435, 0.988348, 0.790679], 'p_i': 80, 'u_i': 1.4717},
        {'id': 4, 'e_m': 2.685098, 'e_o_k': [0.330135, 0.264108, 0.211286], 'p_i': 10, 'u_i': 2.9634},
        {'id': 5, 'e_m': 11.248792, 'e_o_k': [1.003878, 0.803103, 0.642482, 0.513986, 0.411189], 'p_i': 80, 'u_i': 1.6416},
        {'id': 6, 'e_m': 4.516843, 'e_o_k': [0.403098, 0.322478, 0.257982, 0.206386, 0.165109], 'p_i': 20, 'u_i': 4.1520},
        {'id': 7, 'e_m': 3.125233, 'e_o_k': [0.317605, 0.254084, 0.203267, 0.162614], 'p_i': 10, 'u_i': 2.8128},
    ]
    B_BUDGET = 215.279992
    return processors, tasks, B_BUDGET
