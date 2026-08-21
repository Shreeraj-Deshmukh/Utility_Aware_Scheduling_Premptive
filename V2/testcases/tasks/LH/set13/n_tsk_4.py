"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.130152, 'e_o_k': [0.074678, 0.059742, 0.047794], 'p_i': 10, 'u_i': 3.2721},
        {'id': 1, 'e_m': 0.967654, 'e_o_k': [0.752620, 0.602096], 'p_i': 20, 'u_i': 2.5377},
        {'id': 2, 'e_m': 4.222704, 'e_o_k': [3.284326, 2.627461], 'p_i': 40, 'u_i': 2.5387},
        {'id': 3, 'e_m': 18.642755, 'e_o_k': [8.841415, 7.073132, 5.658505, 4.526804], 'p_i': 80, 'u_i': 1.0056},
    ]
    B_BUDGET = 88.320001
    return processors, tasks, B_BUDGET
