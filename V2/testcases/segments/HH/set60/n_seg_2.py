"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639993, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.639993, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.456621, 'e_o_k': [1.132928, 0.906342], 'p_i': 10, 'u_i': 4.9967},
        {'id': 1, 'e_m': 6.472983, 'e_o_k': [5.034542, 4.027634], 'p_i': 20, 'u_i': 3.1686},
        {'id': 2, 'e_m': 1.070031, 'e_o_k': [0.832246, 0.665797], 'p_i': 40, 'u_i': 1.4833},
        {'id': 3, 'e_m': 9.500976, 'e_o_k': [7.389648, 5.911718], 'p_i': 80, 'u_i': 4.1202},
        {'id': 4, 'e_m': 0.365435, 'e_o_k': [0.284228, 0.227382], 'p_i': 40, 'u_i': 4.7898},
        {'id': 5, 'e_m': 0.184044, 'e_o_k': [0.143145, 0.114516], 'p_i': 10, 'u_i': 3.8151},
        {'id': 6, 'e_m': 5.282667, 'e_o_k': [4.108741, 3.286993], 'p_i': 40, 'u_i': 2.4922},
        {'id': 7, 'e_m': 0.255688, 'e_o_k': [0.198868, 0.159095], 'p_i': 10, 'u_i': 1.4417},
    ]
    B_BUDGET = 176.639993
    return processors, tasks, B_BUDGET
