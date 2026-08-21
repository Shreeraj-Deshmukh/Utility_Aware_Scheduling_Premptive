"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359991, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359991, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.587051, 'e_o_k': [0.129054, 0.103243, 0.082594, 0.066076, 0.052860, 0.042288], 'p_i': 10, 'u_i': 2.9192},
        {'id': 1, 'e_m': 2.099857, 'e_o_k': [0.213400, 0.170720, 0.136576, 0.109261], 'p_i': 20, 'u_i': 2.0454},
        {'id': 2, 'e_m': 15.075170, 'e_o_k': [1.225863, 0.980690, 0.784552, 0.627642, 0.502113, 0.401691], 'p_i': 40, 'u_i': 2.8602},
        {'id': 3, 'e_m': 34.244251, 'e_o_k': [5.707375, 4.565900], 'p_i': 80, 'u_i': 2.9521},
        {'id': 4, 'e_m': 1.708142, 'e_o_k': [0.284690, 0.227752], 'p_i': 10, 'u_i': 3.5497},
        {'id': 5, 'e_m': 6.625267, 'e_o_k': [0.673300, 0.538640, 0.430912, 0.344729], 'p_i': 40, 'u_i': 2.7971},
        {'id': 6, 'e_m': 3.677574, 'e_o_k': [0.299048, 0.239238, 0.191391, 0.153113, 0.122490, 0.097992], 'p_i': 80, 'u_i': 4.6429},
        {'id': 7, 'e_m': 11.916327, 'e_o_k': [1.986055, 1.588844], 'p_i': 80, 'u_i': 1.6248},
    ]
    B_BUDGET = 191.359991
    return processors, tasks, B_BUDGET
