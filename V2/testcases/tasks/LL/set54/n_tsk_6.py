"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199992, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199992, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.363511, 'e_o_k': [0.202807, 0.162245, 0.129796, 0.103837, 0.083070], 'p_i': 10, 'u_i': 4.2653},
        {'id': 1, 'e_m': 0.224102, 'e_o_k': [0.030372, 0.024298, 0.019438, 0.015550, 0.012440, 0.009952], 'p_i': 20, 'u_i': 3.8195},
        {'id': 2, 'e_m': 8.637417, 'e_o_k': [1.170610, 0.936488, 0.749190, 0.599352, 0.479482, 0.383586], 'p_i': 40, 'u_i': 1.2105},
        {'id': 3, 'e_m': 0.668357, 'e_o_k': [0.136958, 0.109567, 0.087653], 'p_i': 80, 'u_i': 1.7971},
        {'id': 4, 'e_m': 0.183998, 'e_o_k': [0.037705, 0.030164, 0.024131], 'p_i': 20, 'u_i': 3.9776},
        {'id': 5, 'e_m': 0.758160, 'e_o_k': [0.112768, 0.090214, 0.072171, 0.057737, 0.046190], 'p_i': 40, 'u_i': 2.5595},
    ]
    B_BUDGET = 55.199992
    return processors, tasks, B_BUDGET
