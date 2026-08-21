"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.471954, 'e_o_k': [0.218937, 0.175149, 0.140119, 0.112096, 0.089676], 'p_i': 10, 'u_i': 1.2401},
        {'id': 1, 'e_m': 2.545723, 'e_o_k': [0.378648, 0.302918, 0.242334, 0.193868, 0.155094], 'p_i': 20, 'u_i': 2.2762},
        {'id': 2, 'e_m': 13.299632, 'e_o_k': [1.978170, 1.582536, 1.266029, 1.012823, 0.810258], 'p_i': 40, 'u_i': 1.0661},
        {'id': 3, 'e_m': 15.442209, 'e_o_k': [2.615550, 2.092440, 1.673952, 1.339162], 'p_i': 80, 'u_i': 2.9903},
    ]
    B_BUDGET = 110.399997
    return processors, tasks, B_BUDGET
