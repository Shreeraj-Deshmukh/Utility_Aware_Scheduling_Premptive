"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.258301, 'e_o_k': [0.596755, 0.477404, 0.381923, 0.305539], 'p_i': 10, 'u_i': 4.9008},
        {'id': 1, 'e_m': 1.199160, 'e_o_k': [0.932680, 0.746144], 'p_i': 20, 'u_i': 4.5033},
        {'id': 2, 'e_m': 4.719366, 'e_o_k': [2.707833, 2.166266, 1.733013], 'p_i': 40, 'u_i': 2.6753},
        {'id': 3, 'e_m': 7.698219, 'e_o_k': [5.987504, 4.790003], 'p_i': 80, 'u_i': 4.2784},
    ]
    B_BUDGET = 88.319993
    return processors, tasks, B_BUDGET
