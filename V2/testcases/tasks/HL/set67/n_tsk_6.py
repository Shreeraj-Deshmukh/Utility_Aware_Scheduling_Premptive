"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.560347, 'e_o_k': [0.772416, 0.617933, 0.494347, 0.395477], 'p_i': 10, 'u_i': 1.8147},
        {'id': 1, 'e_m': 0.119200, 'e_o_k': [0.020190, 0.016152, 0.012921, 0.010337], 'p_i': 20, 'u_i': 2.7697},
        {'id': 2, 'e_m': 5.951871, 'e_o_k': [0.806644, 0.645315, 0.516252, 0.413002, 0.330401, 0.264321], 'p_i': 40, 'u_i': 2.4720},
        {'id': 3, 'e_m': 2.781198, 'e_o_k': [0.772555, 0.618044], 'p_i': 80, 'u_i': 3.3220},
        {'id': 4, 'e_m': 8.400858, 'e_o_k': [2.333572, 1.866857], 'p_i': 80, 'u_i': 2.5309},
        {'id': 5, 'e_m': 0.988657, 'e_o_k': [0.202594, 0.162075, 0.129660], 'p_i': 20, 'u_i': 3.7128},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
