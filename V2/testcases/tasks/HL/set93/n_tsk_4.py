"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.421301, 'e_o_k': [0.410112, 0.328090, 0.262472, 0.209977], 'p_i': 10, 'u_i': 4.8908},
        {'id': 1, 'e_m': 2.540034, 'e_o_k': [0.377801, 0.302241, 0.241793, 0.193434, 0.154747], 'p_i': 20, 'u_i': 3.7143},
        {'id': 2, 'e_m': 4.920392, 'e_o_k': [0.731853, 0.585482, 0.468386, 0.374709, 0.299767], 'p_i': 40, 'u_i': 4.3200},
        {'id': 3, 'e_m': 24.628672, 'e_o_k': [3.337870, 2.670296, 2.136237, 1.708989, 1.367191, 1.093753], 'p_i': 80, 'u_i': 3.1069},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET
