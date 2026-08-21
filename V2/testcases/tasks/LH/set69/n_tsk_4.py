"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.066996, 'e_o_k': [0.025423, 0.020339, 0.016271, 0.013017, 0.010413, 0.008331], 'p_i': 10, 'u_i': 3.0227},
        {'id': 1, 'e_m': 1.196503, 'e_o_k': [0.930614, 0.744491], 'p_i': 20, 'u_i': 1.4869},
        {'id': 2, 'e_m': 1.568472, 'e_o_k': [0.899943, 0.719954, 0.575963], 'p_i': 40, 'u_i': 4.8069},
        {'id': 3, 'e_m': 23.541076, 'e_o_k': [9.804113, 7.843290, 6.274632, 5.019706, 4.015765], 'p_i': 80, 'u_i': 1.7670},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET
