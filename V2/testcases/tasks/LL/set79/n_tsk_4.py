"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.748978, 'e_o_k': [0.153479, 0.122783, 0.098227], 'p_i': 10, 'u_i': 4.6460},
        {'id': 1, 'e_m': 2.001687, 'e_o_k': [0.271284, 0.217027, 0.173622, 0.138898, 0.111118, 0.088894], 'p_i': 20, 'u_i': 1.6535},
        {'id': 2, 'e_m': 0.867381, 'e_o_k': [0.129013, 0.103211, 0.082568, 0.066055, 0.052844], 'p_i': 40, 'u_i': 3.3613},
        {'id': 3, 'e_m': 16.266664, 'e_o_k': [2.755194, 2.204155, 1.763324, 1.410659], 'p_i': 80, 'u_i': 3.4647},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET
