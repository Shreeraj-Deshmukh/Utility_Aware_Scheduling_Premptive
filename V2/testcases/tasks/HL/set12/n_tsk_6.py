"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.558373, 'e_o_k': [0.319339, 0.255471, 0.204377], 'p_i': 10, 'u_i': 2.7610},
        {'id': 1, 'e_m': 4.935764, 'e_o_k': [1.371045, 1.096836], 'p_i': 20, 'u_i': 2.5980},
        {'id': 2, 'e_m': 6.473715, 'e_o_k': [1.798254, 1.438603], 'p_i': 40, 'u_i': 2.9083},
        {'id': 3, 'e_m': 15.590869, 'e_o_k': [3.194850, 2.555880, 2.044704], 'p_i': 80, 'u_i': 4.8275},
        {'id': 4, 'e_m': 2.417965, 'e_o_k': [0.359645, 0.287716, 0.230173, 0.184138, 0.147311], 'p_i': 80, 'u_i': 3.8825},
        {'id': 5, 'e_m': 0.208424, 'e_o_k': [0.042710, 0.034168, 0.027334], 'p_i': 20, 'u_i': 1.8333},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET
