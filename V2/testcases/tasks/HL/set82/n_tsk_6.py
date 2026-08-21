"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400009, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400009, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.261165, 'e_o_k': [0.628101, 0.502481], 'p_i': 10, 'u_i': 4.0095},
        {'id': 1, 'e_m': 0.481091, 'e_o_k': [0.071557, 0.057245, 0.045796, 0.036637, 0.029310], 'p_i': 20, 'u_i': 4.5444},
        {'id': 2, 'e_m': 4.115053, 'e_o_k': [1.143070, 0.914456], 'p_i': 40, 'u_i': 4.8070},
        {'id': 3, 'e_m': 5.540102, 'e_o_k': [0.824028, 0.659222, 0.527378, 0.421902, 0.337522], 'p_i': 80, 'u_i': 3.8434},
        {'id': 4, 'e_m': 10.905856, 'e_o_k': [3.029404, 2.423524], 'p_i': 40, 'u_i': 3.7460},
        {'id': 5, 'e_m': 1.050550, 'e_o_k': [0.177939, 0.142351, 0.113881, 0.091105], 'p_i': 10, 'u_i': 2.3844},
    ]
    B_BUDGET = 110.400009
    return processors, tasks, B_BUDGET
