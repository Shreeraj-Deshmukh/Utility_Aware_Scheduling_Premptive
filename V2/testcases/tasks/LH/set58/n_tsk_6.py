"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319991, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319991, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.852681, 'e_o_k': [0.663196, 0.530557], 'p_i': 10, 'u_i': 1.4573},
        {'id': 1, 'e_m': 2.529372, 'e_o_k': [1.053403, 0.842723, 0.674178, 0.539342, 0.431474], 'p_i': 20, 'u_i': 1.2598},
        {'id': 2, 'e_m': 0.360578, 'e_o_k': [0.136831, 0.109465, 0.087572, 0.070058, 0.056046, 0.044837], 'p_i': 40, 'u_i': 4.1820},
        {'id': 3, 'e_m': 3.676304, 'e_o_k': [2.859348, 2.287478], 'p_i': 80, 'u_i': 2.8729},
        {'id': 4, 'e_m': 1.338365, 'e_o_k': [0.767914, 0.614332, 0.491465], 'p_i': 20, 'u_i': 4.4646},
        {'id': 5, 'e_m': 0.663768, 'e_o_k': [0.516264, 0.413011], 'p_i': 10, 'u_i': 2.8456},
    ]
    B_BUDGET = 88.319991
    return processors, tasks, B_BUDGET
