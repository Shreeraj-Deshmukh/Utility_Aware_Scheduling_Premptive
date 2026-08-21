"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320007, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320007, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.779187, 'e_o_k': [0.447074, 0.357659, 0.286128], 'p_i': 10, 'u_i': 2.7610},
        {'id': 1, 'e_m': 2.467882, 'e_o_k': [1.919464, 1.535571], 'p_i': 20, 'u_i': 2.5980},
        {'id': 2, 'e_m': 3.236858, 'e_o_k': [2.517556, 2.014045], 'p_i': 40, 'u_i': 2.9083},
        {'id': 3, 'e_m': 7.795435, 'e_o_k': [4.472790, 3.578232, 2.862586], 'p_i': 80, 'u_i': 4.8275},
        {'id': 4, 'e_m': 1.208982, 'e_o_k': [0.503503, 0.402802, 0.322242, 0.257793, 0.206235], 'p_i': 80, 'u_i': 3.8825},
        {'id': 5, 'e_m': 0.104212, 'e_o_k': [0.059794, 0.047835, 0.038268], 'p_i': 20, 'u_i': 1.8333},
    ]
    B_BUDGET = 88.320007
    return processors, tasks, B_BUDGET
