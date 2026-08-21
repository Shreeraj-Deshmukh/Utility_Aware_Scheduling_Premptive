"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.067652, 'e_o_k': [0.218781, 0.175025, 0.140020], 'p_i': 10, 'u_i': 4.1455},
        {'id': 1, 'e_m': 0.714972, 'e_o_k': [0.121100, 0.096880, 0.077504, 0.062003], 'p_i': 20, 'u_i': 1.8811},
        {'id': 2, 'e_m': 2.996480, 'e_o_k': [0.614033, 0.491226, 0.392981], 'p_i': 40, 'u_i': 4.6061},
        {'id': 3, 'e_m': 14.605935, 'e_o_k': [2.172468, 1.737974, 1.390379, 1.112303, 0.889843], 'p_i': 80, 'u_i': 1.8658},
    ]
    B_BUDGET = 55.200002
    return processors, tasks, B_BUDGET
