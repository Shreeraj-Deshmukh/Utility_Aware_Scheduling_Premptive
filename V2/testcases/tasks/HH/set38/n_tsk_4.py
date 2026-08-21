"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.132457, 'e_o_k': [1.721037, 1.376830, 1.101464, 0.881171, 0.704937], 'p_i': 10, 'u_i': 1.1882},
        {'id': 1, 'e_m': 3.835651, 'e_o_k': [1.597427, 1.277942, 1.022353, 0.817883, 0.654306], 'p_i': 20, 'u_i': 4.0368},
        {'id': 2, 'e_m': 6.828912, 'e_o_k': [5.311376, 4.249101], 'p_i': 40, 'u_i': 1.1650},
        {'id': 3, 'e_m': 1.939921, 'e_o_k': [0.920017, 0.736013, 0.588811, 0.471049], 'p_i': 80, 'u_i': 2.0635},
    ]
    B_BUDGET = 176.640006
    return processors, tasks, B_BUDGET
