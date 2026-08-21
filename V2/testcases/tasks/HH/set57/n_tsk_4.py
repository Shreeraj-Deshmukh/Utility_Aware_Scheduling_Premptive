"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.462267, 'e_o_k': [0.219232, 0.175386, 0.140309, 0.112247], 'p_i': 10, 'u_i': 4.2108},
        {'id': 1, 'e_m': 3.806267, 'e_o_k': [2.183924, 1.747139, 1.397711], 'p_i': 20, 'u_i': 3.3354},
        {'id': 2, 'e_m': 18.908949, 'e_o_k': [8.967659, 7.174127, 5.739302, 4.591441], 'p_i': 40, 'u_i': 1.0371},
        {'id': 3, 'e_m': 7.258899, 'e_o_k': [3.023102, 2.418481, 1.934785, 1.547828, 1.238262], 'p_i': 80, 'u_i': 1.4152},
    ]
    B_BUDGET = 176.640006
    return processors, tasks, B_BUDGET
