"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.272733, 'e_o_k': [0.946521, 0.757217, 0.605774, 0.484619, 0.387695], 'p_i': 10, 'u_i': 2.5944},
        {'id': 1, 'e_m': 9.445309, 'e_o_k': [3.933672, 3.146938, 2.517550, 2.014040, 1.611232], 'p_i': 20, 'u_i': 4.8069},
        {'id': 2, 'e_m': 3.305264, 'e_o_k': [1.567537, 1.254030, 1.003224, 0.802579], 'p_i': 40, 'u_i': 1.7136},
        {'id': 3, 'e_m': 1.426372, 'e_o_k': [0.594039, 0.475231, 0.380185, 0.304148, 0.243318], 'p_i': 80, 'u_i': 3.6562},
    ]
    B_BUDGET = 176.639997
    return processors, tasks, B_BUDGET
