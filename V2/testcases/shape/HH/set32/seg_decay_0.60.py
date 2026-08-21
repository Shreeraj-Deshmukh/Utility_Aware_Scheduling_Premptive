"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639985, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.639985, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.015283, 'e_o_k': [0.616497, 0.369898, 0.221939, 0.133163, 0.079898], 'p_i': 10, 'u_i': 2.6437},
        {'id': 1, 'e_m': 1.338137, 'e_o_k': [0.786030, 0.471618, 0.282971, 0.169782, 0.101869, 0.061122], 'p_i': 20, 'u_i': 2.4707},
        {'id': 2, 'e_m': 1.215369, 'e_o_k': [0.713915, 0.428349, 0.257010, 0.154206, 0.092523, 0.055514], 'p_i': 40, 'u_i': 1.1046},
        {'id': 3, 'e_m': 11.427473, 'e_o_k': [9.999039, 5.999423], 'p_i': 80, 'u_i': 3.2848},
        {'id': 4, 'e_m': 4.192750, 'e_o_k': [2.697542, 1.618525, 0.971115, 0.582669], 'p_i': 40, 'u_i': 2.0063},
        {'id': 5, 'e_m': 0.541048, 'e_o_k': [0.348101, 0.208860, 0.125316, 0.075190], 'p_i': 10, 'u_i': 1.2869},
        {'id': 6, 'e_m': 5.660701, 'e_o_k': [4.953113, 2.971868], 'p_i': 20, 'u_i': 2.7193},
        {'id': 7, 'e_m': 0.655144, 'e_o_k': [0.573251, 0.343950], 'p_i': 40, 'u_i': 1.9085},
    ]
    B_BUDGET = 176.639985
    return processors, tasks, B_BUDGET
