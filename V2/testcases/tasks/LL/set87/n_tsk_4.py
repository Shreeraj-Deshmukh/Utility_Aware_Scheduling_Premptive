"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.661504, 'e_o_k': [0.281420, 0.225136, 0.180109, 0.144087], 'p_i': 10, 'u_i': 4.1671},
        {'id': 1, 'e_m': 0.341465, 'e_o_k': [0.069972, 0.055978, 0.044782], 'p_i': 20, 'u_i': 4.3098},
        {'id': 2, 'e_m': 1.861171, 'e_o_k': [0.315239, 0.252191, 0.201753, 0.161402], 'p_i': 40, 'u_i': 1.7953},
        {'id': 3, 'e_m': 13.619767, 'e_o_k': [1.845857, 1.476686, 1.181349, 0.945079, 0.756063, 0.604850], 'p_i': 80, 'u_i': 2.0773},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
