"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399995, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399995, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.344563, 'e_o_k': [0.651267, 0.521014], 'p_i': 10, 'u_i': 3.5492},
        {'id': 1, 'e_m': 1.657669, 'e_o_k': [0.460463, 0.368371], 'p_i': 20, 'u_i': 2.1494},
        {'id': 2, 'e_m': 6.329967, 'e_o_k': [0.857887, 0.686309, 0.549047, 0.439238, 0.351390, 0.281112], 'p_i': 40, 'u_i': 1.9189},
        {'id': 3, 'e_m': 0.287931, 'e_o_k': [0.079981, 0.063985], 'p_i': 80, 'u_i': 2.3334},
        {'id': 4, 'e_m': 1.260703, 'e_o_k': [0.258341, 0.206673, 0.165338], 'p_i': 80, 'u_i': 2.9112},
        {'id': 5, 'e_m': 6.101064, 'e_o_k': [0.907464, 0.725971, 0.580777, 0.464622, 0.371697], 'p_i': 20, 'u_i': 2.1467},
    ]
    B_BUDGET = 110.399995
    return processors, tasks, B_BUDGET
