"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.283857, 'e_o_k': [0.339698, 0.271758, 0.217407, 0.173925, 0.139140], 'p_i': 10, 'u_i': 1.7421},
        {'id': 1, 'e_m': 1.330238, 'e_o_k': [0.180284, 0.144227, 0.115382, 0.092306, 0.073844, 0.059076], 'p_i': 20, 'u_i': 1.9951},
        {'id': 2, 'e_m': 2.256874, 'e_o_k': [0.626910, 0.501528], 'p_i': 40, 'u_i': 1.2617},
        {'id': 3, 'e_m': 3.894442, 'e_o_k': [0.527805, 0.422244, 0.337795, 0.270236, 0.216189, 0.172951], 'p_i': 80, 'u_i': 4.5683},
    ]
    B_BUDGET = 55.199993
    return processors, tasks, B_BUDGET
