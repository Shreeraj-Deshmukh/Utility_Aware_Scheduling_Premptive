"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.527400, 'e_o_k': [0.071477, 0.057182, 0.045746, 0.036596, 0.029277, 0.023422], 'p_i': 10, 'u_i': 3.5665},
        {'id': 1, 'e_m': 4.435332, 'e_o_k': [0.751242, 0.600994, 0.480795, 0.384636], 'p_i': 20, 'u_i': 1.8299},
        {'id': 2, 'e_m': 12.827845, 'e_o_k': [3.563290, 2.850632], 'p_i': 40, 'u_i': 2.7998},
        {'id': 3, 'e_m': 16.383782, 'e_o_k': [4.551051, 3.640840], 'p_i': 80, 'u_i': 4.4830},
    ]
    B_BUDGET = 110.400003
    return processors, tasks, B_BUDGET
