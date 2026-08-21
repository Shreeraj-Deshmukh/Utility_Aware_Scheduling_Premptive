"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.549447, 'e_o_k': [1.205125, 0.964100], 'p_i': 10, 'u_i': 3.3617},
        {'id': 1, 'e_m': 1.136448, 'e_o_k': [0.538966, 0.431173, 0.344938, 0.275950], 'p_i': 20, 'u_i': 3.9677},
        {'id': 2, 'e_m': 1.290952, 'e_o_k': [0.489888, 0.391910, 0.313528, 0.250823, 0.200658, 0.160526], 'p_i': 40, 'u_i': 4.5134},
        {'id': 3, 'e_m': 6.789892, 'e_o_k': [3.895840, 3.116672, 2.493337], 'p_i': 80, 'u_i': 4.5874},
        {'id': 4, 'e_m': 3.175273, 'e_o_k': [1.821878, 1.457503, 1.166002], 'p_i': 80, 'u_i': 2.7347},
        {'id': 5, 'e_m': 2.511563, 'e_o_k': [1.441061, 1.152849, 0.922279], 'p_i': 80, 'u_i': 4.9671},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET
