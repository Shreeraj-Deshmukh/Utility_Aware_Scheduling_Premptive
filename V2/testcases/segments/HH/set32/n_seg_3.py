"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.015283, 'e_o_k': [0.582539, 0.466032, 0.372825], 'p_i': 10, 'u_i': 2.6437},
        {'id': 1, 'e_m': 1.338137, 'e_o_k': [0.767784, 0.614227, 0.491382], 'p_i': 20, 'u_i': 2.0395},
        {'id': 2, 'e_m': 1.215369, 'e_o_k': [0.697343, 0.557874, 0.446300], 'p_i': 40, 'u_i': 3.8865},
        {'id': 3, 'e_m': 11.427473, 'e_o_k': [6.556747, 5.245397, 4.196318], 'p_i': 80, 'u_i': 3.2848},
        {'id': 4, 'e_m': 4.192750, 'e_o_k': [2.405676, 1.924541, 1.539633], 'p_i': 40, 'u_i': 2.0063},
        {'id': 5, 'e_m': 0.541048, 'e_o_k': [0.310437, 0.248350, 0.198680], 'p_i': 10, 'u_i': 1.2869},
        {'id': 6, 'e_m': 5.660701, 'e_o_k': [3.247943, 2.598355, 2.078684], 'p_i': 20, 'u_i': 2.7193},
        {'id': 7, 'e_m': 0.655144, 'e_o_k': [0.375902, 0.300722, 0.240577], 'p_i': 40, 'u_i': 1.9085},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET
