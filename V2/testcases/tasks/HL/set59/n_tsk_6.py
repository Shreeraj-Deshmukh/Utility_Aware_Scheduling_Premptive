"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399995, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399995, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.764237, 'e_o_k': [1.045621, 0.836497], 'p_i': 10, 'u_i': 3.1325},
        {'id': 1, 'e_m': 1.021954, 'e_o_k': [0.283876, 0.227101], 'p_i': 20, 'u_i': 4.7073},
        {'id': 2, 'e_m': 5.644478, 'e_o_k': [0.764984, 0.611987, 0.489590, 0.391672, 0.313337, 0.250670], 'p_i': 40, 'u_i': 3.8560},
        {'id': 3, 'e_m': 0.828627, 'e_o_k': [0.169801, 0.135840, 0.108672], 'p_i': 80, 'u_i': 2.5226},
        {'id': 4, 'e_m': 5.146392, 'e_o_k': [0.871679, 0.697343, 0.557874, 0.446300], 'p_i': 40, 'u_i': 1.7775},
        {'id': 5, 'e_m': 0.923490, 'e_o_k': [0.256525, 0.205220], 'p_i': 10, 'u_i': 2.7606},
    ]
    B_BUDGET = 110.399995
    return processors, tasks, B_BUDGET
