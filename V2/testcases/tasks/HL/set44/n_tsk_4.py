"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.579975, 'e_o_k': [0.086265, 0.069012, 0.055209, 0.044168, 0.035334], 'p_i': 10, 'u_i': 4.1808},
        {'id': 1, 'e_m': 5.974661, 'e_o_k': [0.809733, 0.647786, 0.518229, 0.414583, 0.331666, 0.265333], 'p_i': 20, 'u_i': 4.1927},
        {'id': 2, 'e_m': 4.376857, 'e_o_k': [0.896897, 0.717518, 0.574014], 'p_i': 40, 'u_i': 3.7566},
        {'id': 3, 'e_m': 26.707844, 'e_o_k': [5.472919, 4.378335, 3.502668], 'p_i': 80, 'u_i': 3.2050},
    ]
    B_BUDGET = 110.400007
    return processors, tasks, B_BUDGET
