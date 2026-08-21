"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.131316, 'e_o_k': [0.879912, 0.703930], 'p_i': 10, 'u_i': 4.8131},
        {'id': 1, 'e_m': 6.732434, 'e_o_k': [2.803846, 2.243077, 1.794461, 1.435569, 1.148455], 'p_i': 20, 'u_i': 1.8577},
        {'id': 2, 'e_m': 7.823287, 'e_o_k': [4.488771, 3.591017, 2.872814], 'p_i': 40, 'u_i': 4.0468},
        {'id': 3, 'e_m': 12.373163, 'e_o_k': [5.153031, 4.122425, 3.297940, 2.638352, 2.110681], 'p_i': 80, 'u_i': 2.5682},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
