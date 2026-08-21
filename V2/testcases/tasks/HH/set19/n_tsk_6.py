"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640013, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640013, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.925700, 'e_o_k': [1.634930, 1.307944, 1.046355, 0.837084, 0.669667], 'p_i': 10, 'u_i': 2.5478},
        {'id': 1, 'e_m': 2.605172, 'e_o_k': [1.235515, 0.988412, 0.790730, 0.632584], 'p_i': 20, 'u_i': 1.9017},
        {'id': 2, 'e_m': 0.892438, 'e_o_k': [0.694118, 0.555295], 'p_i': 40, 'u_i': 4.1004},
        {'id': 3, 'e_m': 6.763993, 'e_o_k': [3.207856, 2.566284, 2.053028, 1.642422], 'p_i': 80, 'u_i': 2.6358},
        {'id': 4, 'e_m': 0.047869, 'e_o_k': [0.027466, 0.021973, 0.017578], 'p_i': 20, 'u_i': 4.3577},
        {'id': 5, 'e_m': 6.716685, 'e_o_k': [3.185420, 2.548336, 2.038669, 1.630935], 'p_i': 40, 'u_i': 4.2383},
    ]
    B_BUDGET = 176.640013
    return processors, tasks, B_BUDGET
