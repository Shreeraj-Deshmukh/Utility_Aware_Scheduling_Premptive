"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.240758, 'e_o_k': [1.766142, 1.412913, 1.130331, 0.904264, 0.723412], 'p_i': 10, 'u_i': 3.0940},
        {'id': 1, 'e_m': 3.393953, 'e_o_k': [1.413474, 1.130779, 0.904623, 0.723699, 0.578959], 'p_i': 20, 'u_i': 2.1175},
        {'id': 2, 'e_m': 0.541246, 'e_o_k': [0.205391, 0.164313, 0.131450, 0.105160, 0.084128, 0.067302], 'p_i': 40, 'u_i': 3.6512},
        {'id': 3, 'e_m': 15.415630, 'e_o_k': [7.310936, 5.848749, 4.678999, 3.743199], 'p_i': 80, 'u_i': 2.9125},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET
