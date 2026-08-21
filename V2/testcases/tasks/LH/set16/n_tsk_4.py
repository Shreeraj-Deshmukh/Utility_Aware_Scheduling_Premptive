"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.141807, 'e_o_k': [0.433290, 0.346632, 0.277306, 0.221845, 0.177476, 0.141981], 'p_i': 10, 'u_i': 1.6837},
        {'id': 1, 'e_m': 2.144447, 'e_o_k': [1.667903, 1.334322], 'p_i': 20, 'u_i': 2.3942},
        {'id': 2, 'e_m': 4.652828, 'e_o_k': [1.937756, 1.550204, 1.240164, 0.992131, 0.793705], 'p_i': 40, 'u_i': 1.1399},
        {'id': 3, 'e_m': 4.982100, 'e_o_k': [1.890597, 1.512477, 1.209982, 0.967986, 0.774388, 0.619511], 'p_i': 80, 'u_i': 4.6324},
    ]
    B_BUDGET = 88.320001
    return processors, tasks, B_BUDGET
