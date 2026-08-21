"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640008, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640008, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.344563, 'e_o_k': [1.823549, 1.458839], 'p_i': 10, 'u_i': 3.5492},
        {'id': 1, 'e_m': 1.657669, 'e_o_k': [1.289298, 1.031438], 'p_i': 20, 'u_i': 2.1494},
        {'id': 2, 'e_m': 6.329967, 'e_o_k': [2.402082, 1.921666, 1.537333, 1.229866, 0.983893, 0.787114], 'p_i': 40, 'u_i': 1.9189},
        {'id': 3, 'e_m': 0.287931, 'e_o_k': [0.223946, 0.179157], 'p_i': 80, 'u_i': 2.3334},
        {'id': 4, 'e_m': 1.260703, 'e_o_k': [0.723354, 0.578683, 0.462947], 'p_i': 80, 'u_i': 2.9112},
        {'id': 5, 'e_m': 6.101064, 'e_o_k': [2.540900, 2.032720, 1.626176, 1.300941, 1.040753], 'p_i': 20, 'u_i': 2.1467},
    ]
    B_BUDGET = 176.640008
    return processors, tasks, B_BUDGET
