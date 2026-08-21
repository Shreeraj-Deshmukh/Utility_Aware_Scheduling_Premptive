"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200005, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200005, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.459408, 'e_o_k': [0.127613, 0.102091], 'p_i': 10, 'u_i': 4.1192},
        {'id': 1, 'e_m': 0.727754, 'e_o_k': [0.123265, 0.098612, 0.078889, 0.063111], 'p_i': 20, 'u_i': 2.9903},
        {'id': 2, 'e_m': 3.606706, 'e_o_k': [0.610892, 0.488714, 0.390971, 0.312777], 'p_i': 40, 'u_i': 3.9277},
        {'id': 3, 'e_m': 5.618102, 'e_o_k': [0.835629, 0.668503, 0.534803, 0.427842, 0.342274], 'p_i': 80, 'u_i': 2.3920},
        {'id': 4, 'e_m': 0.519589, 'e_o_k': [0.088006, 0.070405, 0.056324, 0.045059], 'p_i': 40, 'u_i': 2.2588},
        {'id': 5, 'e_m': 11.543030, 'e_o_k': [3.206397, 2.565118], 'p_i': 80, 'u_i': 4.0829},
    ]
    B_BUDGET = 55.200005
    return processors, tasks, B_BUDGET
