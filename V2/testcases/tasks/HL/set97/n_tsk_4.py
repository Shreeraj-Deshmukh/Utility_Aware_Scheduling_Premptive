"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.191048, 'e_o_k': [0.201736, 0.161389, 0.129111, 0.103289], 'p_i': 10, 'u_i': 4.3067},
        {'id': 1, 'e_m': 4.049834, 'e_o_k': [0.548865, 0.439092, 0.351274, 0.281019, 0.224815, 0.179852], 'p_i': 20, 'u_i': 4.0634},
        {'id': 2, 'e_m': 8.671761, 'e_o_k': [1.777000, 1.421600, 1.137280], 'p_i': 40, 'u_i': 4.9615},
        {'id': 3, 'e_m': 20.928759, 'e_o_k': [2.836429, 2.269143, 1.815314, 1.452251, 1.161801, 0.929441], 'p_i': 80, 'u_i': 2.0301},
    ]
    B_BUDGET = 110.400009
    return processors, tasks, B_BUDGET
