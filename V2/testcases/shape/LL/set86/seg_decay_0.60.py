"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.050222, 'e_o_k': [0.012812, 0.007687, 0.004612], 'p_i': 10, 'u_i': 2.4144},
        {'id': 1, 'e_m': 0.206926, 'e_o_k': [0.064664, 0.038799], 'p_i': 20, 'u_i': 2.6559},
        {'id': 2, 'e_m': 1.190379, 'e_o_k': [0.258150, 0.154890, 0.092934, 0.055760, 0.033456], 'p_i': 40, 'u_i': 2.8681},
        {'id': 3, 'e_m': 6.971948, 'e_o_k': [2.178734, 1.307240], 'p_i': 80, 'u_i': 1.8896},
        {'id': 4, 'e_m': 0.550862, 'e_o_k': [0.119462, 0.071677, 0.043006, 0.025804, 0.015482], 'p_i': 20, 'u_i': 1.6645},
        {'id': 5, 'e_m': 0.291867, 'e_o_k': [0.063295, 0.037977, 0.022786, 0.013672, 0.008203], 'p_i': 40, 'u_i': 1.3774},
        {'id': 6, 'e_m': 1.611679, 'e_o_k': [0.503650, 0.302190], 'p_i': 80, 'u_i': 1.9412},
        {'id': 7, 'e_m': 17.018957, 'e_o_k': [5.318424, 3.191054], 'p_i': 80, 'u_i': 2.2237},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
