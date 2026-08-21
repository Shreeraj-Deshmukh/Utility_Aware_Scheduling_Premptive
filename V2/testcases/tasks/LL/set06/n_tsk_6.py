"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200005, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200005, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.763835, 'e_o_k': [0.103521, 0.082817, 0.066253, 0.053003, 0.042402, 0.033922], 'p_i': 10, 'u_i': 4.5754},
        {'id': 1, 'e_m': 1.996751, 'e_o_k': [0.338203, 0.270562, 0.216450, 0.173160], 'p_i': 20, 'u_i': 3.5388},
        {'id': 2, 'e_m': 6.879753, 'e_o_k': [0.932398, 0.745918, 0.596735, 0.477388, 0.381910, 0.305528], 'p_i': 40, 'u_i': 1.2818},
        {'id': 3, 'e_m': 0.145853, 'e_o_k': [0.040515, 0.032412], 'p_i': 80, 'u_i': 2.2300},
        {'id': 4, 'e_m': 0.338485, 'e_o_k': [0.057332, 0.045865, 0.036692, 0.029354], 'p_i': 10, 'u_i': 1.1980},
        {'id': 5, 'e_m': 0.322269, 'e_o_k': [0.054585, 0.043668, 0.034934, 0.027947], 'p_i': 20, 'u_i': 3.9540},
    ]
    B_BUDGET = 55.200005
    return processors, tasks, B_BUDGET
