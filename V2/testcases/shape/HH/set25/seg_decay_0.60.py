"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639994, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.639994, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.599440, 'e_o_k': [1.399510, 0.839706], 'p_i': 10, 'u_i': 2.3541},
        {'id': 1, 'e_m': 5.185523, 'e_o_k': [3.703945, 2.222367, 1.333420], 'p_i': 20, 'u_i': 4.5958},
        {'id': 2, 'e_m': 2.922224, 'e_o_k': [1.880108, 1.128065, 0.676839, 0.406103], 'p_i': 40, 'u_i': 4.0042},
        {'id': 3, 'e_m': 7.584490, 'e_o_k': [6.636429, 3.981858], 'p_i': 80, 'u_i': 1.4529},
        {'id': 4, 'e_m': 1.038987, 'e_o_k': [0.610307, 0.366184, 0.219711, 0.131826, 0.079096, 0.047457], 'p_i': 40, 'u_i': 4.9580},
        {'id': 5, 'e_m': 1.421690, 'e_o_k': [0.835109, 0.501066, 0.300639, 0.180384, 0.108230, 0.064938], 'p_i': 20, 'u_i': 2.0799},
        {'id': 6, 'e_m': 3.169787, 'e_o_k': [2.773563, 1.664138], 'p_i': 40, 'u_i': 1.2465},
        {'id': 7, 'e_m': 0.366143, 'e_o_k': [0.261530, 0.156918, 0.094151], 'p_i': 10, 'u_i': 3.7304},
    ]
    B_BUDGET = 176.639994
    return processors, tasks, B_BUDGET
