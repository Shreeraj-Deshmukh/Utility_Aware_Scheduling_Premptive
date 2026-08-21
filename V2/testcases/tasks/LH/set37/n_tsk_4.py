"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.246332, 'e_o_k': [1.747147, 1.397717], 'p_i': 10, 'u_i': 1.0738},
        {'id': 1, 'e_m': 0.630515, 'e_o_k': [0.299025, 0.239220, 0.191376, 0.153101], 'p_i': 20, 'u_i': 3.3187},
        {'id': 2, 'e_m': 1.942619, 'e_o_k': [1.114617, 0.891694, 0.713355], 'p_i': 40, 'u_i': 4.5515},
        {'id': 3, 'e_m': 7.622048, 'e_o_k': [5.928260, 4.742608], 'p_i': 80, 'u_i': 3.0521},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET
