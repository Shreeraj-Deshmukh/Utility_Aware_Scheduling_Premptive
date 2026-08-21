"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199991, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199991, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.496415, 'e_o_k': [0.067278, 0.053822, 0.043058, 0.034446, 0.027557, 0.022046], 'p_i': 10, 'u_i': 2.9591},
        {'id': 1, 'e_m': 2.106412, 'e_o_k': [0.313305, 0.250644, 0.200515, 0.160412, 0.128330], 'p_i': 20, 'u_i': 3.3490},
        {'id': 2, 'e_m': 6.598735, 'e_o_k': [1.832982, 1.466386], 'p_i': 40, 'u_i': 1.0216},
        {'id': 3, 'e_m': 2.207762, 'e_o_k': [0.452410, 0.361928, 0.289543], 'p_i': 80, 'u_i': 4.0085},
        {'id': 4, 'e_m': 0.027756, 'e_o_k': [0.005688, 0.004550, 0.003640], 'p_i': 20, 'u_i': 1.9931},
        {'id': 5, 'e_m': 4.086773, 'e_o_k': [0.837453, 0.669963, 0.535970], 'p_i': 80, 'u_i': 2.4773},
    ]
    B_BUDGET = 55.199991
    return processors, tasks, B_BUDGET
