"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319977, "H": 80, "J": 24, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.319977, "H": 80, "J": 24, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.823643, 'e_o_k': [0.192183, 0.192183, 0.192183, 0.192183, 0.192183, 0.192183], 'p_i': 10, 'u_i': 3.9772},
        {'id': 1, 'e_m': 0.017150, 'e_o_k': [0.006003, 0.006003, 0.006003, 0.006003], 'p_i': 20, 'u_i': 1.4627},
        {'id': 2, 'e_m': 1.462946, 'e_o_k': [1.024062, 1.024062], 'p_i': 40, 'u_i': 4.5040},
        {'id': 3, 'e_m': 0.827621, 'e_o_k': [0.386223, 0.386223, 0.386223], 'p_i': 80, 'u_i': 4.7123},
        {'id': 4, 'e_m': 0.489062, 'e_o_k': [0.136937, 0.136937, 0.136937, 0.136937, 0.136937], 'p_i': 20, 'u_i': 4.3702},
        {'id': 5, 'e_m': 0.934156, 'e_o_k': [0.326955, 0.326955, 0.326955, 0.326955], 'p_i': 40, 'u_i': 3.7678},
        {'id': 6, 'e_m': 7.716508, 'e_o_k': [2.700778, 2.700778, 2.700778, 2.700778], 'p_i': 80, 'u_i': 3.2312},
        {'id': 7, 'e_m': 5.023836, 'e_o_k': [2.344457, 2.344457, 2.344457], 'p_i': 40, 'u_i': 3.7207},
    ]
    B_BUDGET = 88.319977
    return processors, tasks, B_BUDGET
