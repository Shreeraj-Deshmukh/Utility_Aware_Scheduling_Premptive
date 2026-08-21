"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 28, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "freq", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 28, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "freq", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.7, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.7, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.786850, 'e_o_k': [0.327698, 0.262159, 0.209727, 0.167782, 0.134225], 'p_i': 10, 'u_i': 3.6650},
        {'id': 1, 'e_m': 0.744352, 'e_o_k': [0.282465, 0.225972, 0.180778, 0.144622, 0.115698, 0.092558], 'p_i': 20, 'u_i': 1.3163},
        {'id': 2, 'e_m': 0.568045, 'e_o_k': [0.269398, 0.215518, 0.172415, 0.137932], 'p_i': 40, 'u_i': 1.2768},
        {'id': 3, 'e_m': 6.876570, 'e_o_k': [3.945573, 3.156458, 2.525167], 'p_i': 80, 'u_i': 1.7506},
        {'id': 4, 'e_m': 2.991189, 'e_o_k': [1.716256, 1.373005, 1.098404], 'p_i': 40, 'u_i': 4.5685},
        {'id': 5, 'e_m': 0.337006, 'e_o_k': [0.140352, 0.112282, 0.089825, 0.071860, 0.057488], 'p_i': 10, 'u_i': 2.7344},
        {'id': 6, 'e_m': 0.443917, 'e_o_k': [0.345269, 0.276215], 'p_i': 40, 'u_i': 1.1398},
        {'id': 7, 'e_m': 5.148870, 'e_o_k': [2.144342, 1.715473, 1.372379, 1.097903, 0.878322], 'p_i': 80, 'u_i': 4.8954},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET
