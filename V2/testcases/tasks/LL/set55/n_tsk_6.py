"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200006, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200006, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.549447, 'e_o_k': [0.430402, 0.344322], 'p_i': 10, 'u_i': 3.3617},
        {'id': 1, 'e_m': 1.136448, 'e_o_k': [0.192488, 0.153990, 0.123192, 0.098554], 'p_i': 20, 'u_i': 3.9677},
        {'id': 2, 'e_m': 1.290952, 'e_o_k': [0.174960, 0.139968, 0.111974, 0.089579, 0.071664, 0.057331], 'p_i': 40, 'u_i': 4.5134},
        {'id': 3, 'e_m': 6.789892, 'e_o_k': [1.391371, 1.113097, 0.890478], 'p_i': 80, 'u_i': 4.5874},
        {'id': 4, 'e_m': 3.175273, 'e_o_k': [0.650671, 0.520537, 0.416429], 'p_i': 80, 'u_i': 2.7347},
        {'id': 5, 'e_m': 2.511563, 'e_o_k': [0.514665, 0.411732, 0.329385], 'p_i': 80, 'u_i': 4.9671},
    ]
    B_BUDGET = 55.200006
    return processors, tasks, B_BUDGET
