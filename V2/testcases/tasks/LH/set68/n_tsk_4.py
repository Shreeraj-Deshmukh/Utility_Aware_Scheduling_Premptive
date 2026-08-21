"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.002647, 'e_o_k': [0.475510, 0.380408, 0.304326, 0.243461], 'p_i': 10, 'u_i': 2.8933},
        {'id': 1, 'e_m': 3.267243, 'e_o_k': [1.239846, 0.991877, 0.793502, 0.634801, 0.507841, 0.406273], 'p_i': 20, 'u_i': 4.7664},
        {'id': 2, 'e_m': 2.699798, 'e_o_k': [1.549064, 1.239251, 0.991401], 'p_i': 40, 'u_i': 2.0608},
        {'id': 3, 'e_m': 5.510258, 'e_o_k': [2.294848, 1.835878, 1.468703, 1.174962, 0.939970], 'p_i': 80, 'u_i': 4.9277},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET
