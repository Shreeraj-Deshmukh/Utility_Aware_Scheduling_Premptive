"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.446847, 'e_o_k': [0.075686, 0.060548, 0.048439, 0.038751], 'p_i': 10, 'u_i': 2.2748},
        {'id': 1, 'e_m': 1.831443, 'e_o_k': [0.310204, 0.248163, 0.198530, 0.158824], 'p_i': 20, 'u_i': 3.5166},
        {'id': 2, 'e_m': 0.329386, 'e_o_k': [0.055790, 0.044632, 0.035706, 0.028565], 'p_i': 40, 'u_i': 2.8575},
        {'id': 3, 'e_m': 20.440676, 'e_o_k': [3.040320, 2.432256, 1.945805, 1.556644, 1.245315], 'p_i': 80, 'u_i': 2.8209},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
