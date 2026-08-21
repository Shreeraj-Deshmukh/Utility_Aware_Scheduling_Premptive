"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.413770, 'e_o_k': [1.099599, 0.879679], 'p_i': 10, 'u_i': 1.1650},
        {'id': 1, 'e_m': 1.499929, 'e_o_k': [0.711348, 0.569079, 0.455263, 0.364210], 'p_i': 20, 'u_i': 2.0635},
        {'id': 2, 'e_m': 3.678693, 'e_o_k': [2.861205, 2.288964], 'p_i': 40, 'u_i': 4.3065},
        {'id': 3, 'e_m': 2.202121, 'e_o_k': [0.835656, 0.668525, 0.534820, 0.427856, 0.342285, 0.273828], 'p_i': 80, 'u_i': 1.2855},
        {'id': 4, 'e_m': 2.780337, 'e_o_k': [1.055076, 0.844061, 0.675249, 0.540199, 0.432159, 0.345727], 'p_i': 80, 'u_i': 4.6522},
        {'id': 5, 'e_m': 0.587570, 'e_o_k': [0.244704, 0.195763, 0.156611, 0.125289, 0.100231], 'p_i': 20, 'u_i': 4.9928},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET
