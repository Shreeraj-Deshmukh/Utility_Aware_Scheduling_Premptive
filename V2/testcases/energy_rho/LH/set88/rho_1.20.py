"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 98.624013, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.2, "seed": 1088, "set": 88, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.20"}
"""

_SPEC = '{"B": 98.624013, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.2, "seed": 1088, "set": 88, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.20"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.343272, 'e_o_k': [0.196959, 0.157568, 0.126054], 'p_i': 10, 'u_i': 3.5588},
        {'id': 1, 'e_m': 0.791370, 'e_o_k': [0.615510, 0.492408], 'p_i': 20, 'u_i': 1.0875},
        {'id': 2, 'e_m': 2.553569, 'e_o_k': [1.211042, 0.968834, 0.775067, 0.620054], 'p_i': 40, 'u_i': 2.9446},
        {'id': 3, 'e_m': 0.112895, 'e_o_k': [0.053541, 0.042833, 0.034266, 0.027413], 'p_i': 80, 'u_i': 2.5289},
        {'id': 4, 'e_m': 5.014202, 'e_o_k': [2.088257, 1.670605, 1.336484, 1.069187, 0.855350], 'p_i': 40, 'u_i': 2.8941},
        {'id': 5, 'e_m': 2.695419, 'e_o_k': [1.022852, 0.818281, 0.654625, 0.523700, 0.418960, 0.335168], 'p_i': 40, 'u_i': 4.5618},
        {'id': 6, 'e_m': 0.133194, 'e_o_k': [0.103595, 0.082876], 'p_i': 10, 'u_i': 3.9189},
        {'id': 7, 'e_m': 2.191761, 'e_o_k': [1.039453, 0.831563, 0.665250, 0.532200], 'p_i': 40, 'u_i': 2.1344},
    ]
    B_BUDGET = 98.624013
    return processors, tasks, B_BUDGET
