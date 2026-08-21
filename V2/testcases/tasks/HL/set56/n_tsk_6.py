"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400006, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400006, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.838505, 'e_o_k': [0.788473, 0.630779], 'p_i': 10, 'u_i': 4.9667},
        {'id': 1, 'e_m': 0.364276, 'e_o_k': [0.054182, 0.043346, 0.034676, 0.027741, 0.022193], 'p_i': 20, 'u_i': 1.4132},
        {'id': 2, 'e_m': 1.483734, 'e_o_k': [0.304044, 0.243235, 0.194588], 'p_i': 40, 'u_i': 4.6321},
        {'id': 3, 'e_m': 0.441000, 'e_o_k': [0.065594, 0.052475, 0.041980, 0.033584, 0.026867], 'p_i': 80, 'u_i': 3.6983},
        {'id': 4, 'e_m': 5.872901, 'e_o_k': [0.873528, 0.698822, 0.559058, 0.447246, 0.357797], 'p_i': 20, 'u_i': 3.0670},
        {'id': 5, 'e_m': 12.934789, 'e_o_k': [3.592997, 2.874397], 'p_i': 80, 'u_i': 2.2547},
    ]
    B_BUDGET = 110.400006
    return processors, tasks, B_BUDGET
