"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.258301, 'e_o_k': [0.213127, 0.170502, 0.136401, 0.109121], 'p_i': 10, 'u_i': 4.9008},
        {'id': 1, 'e_m': 1.199160, 'e_o_k': [0.333100, 0.266480], 'p_i': 20, 'u_i': 4.5033},
        {'id': 2, 'e_m': 4.719366, 'e_o_k': [0.967083, 0.773667, 0.618933], 'p_i': 40, 'u_i': 2.6753},
        {'id': 3, 'e_m': 7.698219, 'e_o_k': [2.138394, 1.710715], 'p_i': 80, 'u_i': 4.2784},
    ]
    B_BUDGET = 55.200002
    return processors, tasks, B_BUDGET
