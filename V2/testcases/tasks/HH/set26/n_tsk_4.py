"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.863900, 'e_o_k': [1.086787, 0.869429, 0.695544, 0.556435, 0.445148, 0.356118], 'p_i': 10, 'u_i': 2.2803},
        {'id': 1, 'e_m': 2.474738, 'e_o_k': [0.939108, 0.751287, 0.601029, 0.480823, 0.384659, 0.307727], 'p_i': 20, 'u_i': 3.9685},
        {'id': 2, 'e_m': 9.121090, 'e_o_k': [7.094181, 5.675345], 'p_i': 40, 'u_i': 1.4001},
        {'id': 3, 'e_m': 12.947663, 'e_o_k': [6.140491, 4.912393, 3.929914, 3.143931], 'p_i': 80, 'u_i': 2.1780},
    ]
    B_BUDGET = 176.639995
    return processors, tasks, B_BUDGET
