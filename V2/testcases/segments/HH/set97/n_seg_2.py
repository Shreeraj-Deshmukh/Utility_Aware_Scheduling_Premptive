"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639991, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.639991, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.701313, 'e_o_k': [0.545465, 0.436372], 'p_i': 10, 'u_i': 4.4298},
        {'id': 1, 'e_m': 6.860890, 'e_o_k': [5.336248, 4.268998], 'p_i': 20, 'u_i': 1.5050},
        {'id': 2, 'e_m': 0.414599, 'e_o_k': [0.322466, 0.257973], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 3.429684, 'e_o_k': [2.667532, 2.134025], 'p_i': 80, 'u_i': 2.5958},
        {'id': 4, 'e_m': 1.398858, 'e_o_k': [1.088000, 0.870400], 'p_i': 20, 'u_i': 1.3643},
        {'id': 5, 'e_m': 5.494678, 'e_o_k': [4.273638, 3.418910], 'p_i': 80, 'u_i': 4.2904},
        {'id': 6, 'e_m': 5.102592, 'e_o_k': [3.968683, 3.174946], 'p_i': 40, 'u_i': 4.4714},
        {'id': 7, 'e_m': 5.391763, 'e_o_k': [4.193593, 3.354875], 'p_i': 80, 'u_i': 4.7028},
    ]
    B_BUDGET = 176.639991
    return processors, tasks, B_BUDGET
