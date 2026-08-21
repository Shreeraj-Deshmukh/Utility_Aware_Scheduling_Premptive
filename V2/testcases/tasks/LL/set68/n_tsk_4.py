"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.002647, 'e_o_k': [0.169825, 0.135860, 0.108688, 0.086950], 'p_i': 10, 'u_i': 2.8933},
        {'id': 1, 'e_m': 3.267243, 'e_o_k': [0.442802, 0.354242, 0.283393, 0.226715, 0.181372, 0.145097], 'p_i': 20, 'u_i': 4.7664},
        {'id': 2, 'e_m': 2.699798, 'e_o_k': [0.553237, 0.442590, 0.354072], 'p_i': 40, 'u_i': 2.0608},
        {'id': 3, 'e_m': 5.510258, 'e_o_k': [0.819589, 0.655671, 0.524537, 0.419629, 0.335703], 'p_i': 80, 'u_i': 4.9277},
    ]
    B_BUDGET = 55.199997
    return processors, tasks, B_BUDGET
