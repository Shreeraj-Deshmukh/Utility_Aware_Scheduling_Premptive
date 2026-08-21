"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.64001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.106643, 'e_o_k': [0.860722, 0.688578], 'p_i': 10, 'u_i': 2.8789},
        {'id': 1, 'e_m': 3.625744, 'e_o_k': [2.080345, 1.664276, 1.331421], 'p_i': 20, 'u_i': 1.7162},
        {'id': 2, 'e_m': 0.770106, 'e_o_k': [0.598971, 0.479177], 'p_i': 40, 'u_i': 1.4626},
        {'id': 3, 'e_m': 39.103672, 'e_o_k': [30.413967, 24.331174], 'p_i': 80, 'u_i': 2.2690},
    ]
    B_BUDGET = 176.640010
    return processors, tasks, B_BUDGET
