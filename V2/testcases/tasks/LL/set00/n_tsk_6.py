"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.196494, 'e_o_k': [0.040265, 0.032212, 0.025770], 'p_i': 10, 'u_i': 3.6850},
        {'id': 1, 'e_m': 0.725173, 'e_o_k': [0.122827, 0.098262, 0.078609, 0.062888], 'p_i': 20, 'u_i': 3.7169},
        {'id': 2, 'e_m': 7.393519, 'e_o_k': [1.515065, 1.212052, 0.969642], 'p_i': 40, 'u_i': 3.7239},
        {'id': 3, 'e_m': 5.171126, 'e_o_k': [0.875868, 0.700695, 0.560556, 0.448445], 'p_i': 80, 'u_i': 1.9107},
        {'id': 4, 'e_m': 4.027507, 'e_o_k': [0.599046, 0.479237, 0.383390, 0.306712, 0.245369], 'p_i': 80, 'u_i': 1.7322},
        {'id': 5, 'e_m': 0.885421, 'e_o_k': [0.131696, 0.105357, 0.084286, 0.067429, 0.053943], 'p_i': 20, 'u_i': 1.5709},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
