"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320001, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320001, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.089178, 'e_o_k': [0.037140, 0.029712, 0.023770, 0.019016, 0.015213], 'p_i': 10, 'u_i': 3.3453},
        {'id': 1, 'e_m': 3.187689, 'e_o_k': [1.829002, 1.463202, 1.170561], 'p_i': 20, 'u_i': 2.8841},
        {'id': 2, 'e_m': 0.550156, 'e_o_k': [0.315663, 0.252530, 0.202024], 'p_i': 40, 'u_i': 2.2513},
        {'id': 3, 'e_m': 6.838438, 'e_o_k': [3.243162, 2.594529, 2.075623, 1.660499], 'p_i': 80, 'u_i': 1.5109},
        {'id': 4, 'e_m': 1.062595, 'e_o_k': [0.609685, 0.487748, 0.390199], 'p_i': 10, 'u_i': 1.6396},
        {'id': 5, 'e_m': 0.524077, 'e_o_k': [0.300700, 0.240560, 0.192448], 'p_i': 20, 'u_i': 4.1445},
    ]
    B_BUDGET = 88.320001
    return processors, tasks, B_BUDGET
