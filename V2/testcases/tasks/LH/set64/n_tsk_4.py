"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.485558, 'e_o_k': [0.618688, 0.494950, 0.395960, 0.316768, 0.253415], 'p_i': 10, 'u_i': 1.3731},
        {'id': 1, 'e_m': 3.834434, 'e_o_k': [2.200085, 1.760068, 1.408054], 'p_i': 20, 'u_i': 1.2580},
        {'id': 2, 'e_m': 1.048626, 'e_o_k': [0.497316, 0.397853, 0.318282, 0.254626], 'p_i': 40, 'u_i': 4.0597},
        {'id': 3, 'e_m': 2.680548, 'e_o_k': [1.116364, 0.893091, 0.714473, 0.571578, 0.457263], 'p_i': 80, 'u_i': 2.2779},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
