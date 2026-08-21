"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.987927, 'e_o_k': [0.411440, 0.329152, 0.263322, 0.210657, 0.168526], 'p_i': 10, 'u_i': 1.8790},
        {'id': 1, 'e_m': 7.460876, 'e_o_k': [3.107219, 2.485775, 1.988620, 1.590896, 1.272717], 'p_i': 20, 'u_i': 3.3534},
        {'id': 2, 'e_m': 8.597414, 'e_o_k': [4.932942, 3.946354, 3.157083], 'p_i': 40, 'u_i': 2.5184},
        {'id': 3, 'e_m': 9.058254, 'e_o_k': [3.772476, 3.017981, 2.414385, 1.931508, 1.545206], 'p_i': 80, 'u_i': 4.2996},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET
