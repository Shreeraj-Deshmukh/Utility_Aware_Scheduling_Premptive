"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319988, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319988, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.293027, 'e_o_k': [0.138969, 0.111175, 0.088940, 0.071152], 'p_i': 10, 'u_i': 1.2737},
        {'id': 1, 'e_m': 0.748915, 'e_o_k': [0.311899, 0.249520, 0.199616, 0.159693, 0.127754], 'p_i': 20, 'u_i': 1.7815},
        {'id': 2, 'e_m': 1.607964, 'e_o_k': [0.762584, 0.610068, 0.488054, 0.390443], 'p_i': 40, 'u_i': 4.6156},
        {'id': 3, 'e_m': 23.444197, 'e_o_k': [11.118521, 8.894817, 7.115854, 5.692683], 'p_i': 80, 'u_i': 1.3815},
    ]
    B_BUDGET = 88.319988
    return processors, tasks, B_BUDGET
