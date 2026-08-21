"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.783783, 'e_o_k': [0.609609, 0.487687], 'p_i': 10, 'u_i': 1.2013},
        {'id': 1, 'e_m': 0.135220, 'e_o_k': [0.077585, 0.062068, 0.049654], 'p_i': 20, 'u_i': 4.4940},
        {'id': 2, 'e_m': 8.308601, 'e_o_k': [3.152930, 2.522344, 2.017875, 1.614300, 1.291440, 1.033152], 'p_i': 40, 'u_i': 4.9438},
        {'id': 3, 'e_m': 8.571659, 'e_o_k': [3.252755, 2.602204, 2.081763, 1.665410, 1.332328, 1.065863], 'p_i': 80, 'u_i': 2.3791},
    ]
    B_BUDGET = 88.320007
    return processors, tasks, B_BUDGET
