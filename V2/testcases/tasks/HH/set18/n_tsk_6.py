"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639985, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639985, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.359767, 'e_o_k': [0.780194, 0.624155, 0.499324], 'p_i': 10, 'u_i': 4.6061},
        {'id': 1, 'e_m': 0.835820, 'e_o_k': [0.348093, 0.278474, 0.222779, 0.178223, 0.142579], 'p_i': 20, 'u_i': 1.8658},
        {'id': 2, 'e_m': 2.695014, 'e_o_k': [2.096122, 1.676897], 'p_i': 40, 'u_i': 4.6317},
        {'id': 3, 'e_m': 7.874175, 'e_o_k': [3.279345, 2.623476, 2.098781, 1.679024, 1.343220], 'p_i': 80, 'u_i': 4.1058},
        {'id': 4, 'e_m': 3.900102, 'e_o_k': [2.237764, 1.790211, 1.432169], 'p_i': 40, 'u_i': 1.5782},
        {'id': 5, 'e_m': 7.178543, 'e_o_k': [2.989636, 2.391709, 1.913367, 1.530694, 1.224555], 'p_i': 20, 'u_i': 1.2072},
    ]
    B_BUDGET = 176.639985
    return processors, tasks, B_BUDGET
