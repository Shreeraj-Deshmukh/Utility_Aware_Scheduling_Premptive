"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280006, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280006, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.711870, 'e_o_k': [0.579328, 0.463463, 0.370770], 'p_i': 10, 'u_i': 2.3091},
        {'id': 1, 'e_m': 1.690864, 'e_o_k': [0.150898, 0.120719, 0.096575, 0.077260, 0.061808], 'p_i': 20, 'u_i': 2.8692},
        {'id': 2, 'e_m': 6.352169, 'e_o_k': [1.058695, 0.846956], 'p_i': 40, 'u_i': 2.5889},
        {'id': 3, 'e_m': 39.065784, 'e_o_k': [3.970100, 3.176080, 2.540864, 2.032691], 'p_i': 80, 'u_i': 2.9689},
        {'id': 4, 'e_m': 3.012756, 'e_o_k': [0.244987, 0.195990, 0.156792, 0.125433, 0.100347, 0.080277], 'p_i': 10, 'u_i': 3.8398},
        {'id': 5, 'e_m': 0.560985, 'e_o_k': [0.057011, 0.045609, 0.036487, 0.029189], 'p_i': 10, 'u_i': 4.2493},
        {'id': 6, 'e_m': 18.929059, 'e_o_k': [1.923685, 1.538948, 1.231158, 0.984927], 'p_i': 80, 'u_i': 2.6256},
        {'id': 7, 'e_m': 0.252478, 'e_o_k': [0.025658, 0.020527, 0.016421, 0.013137], 'p_i': 80, 'u_i': 2.8942},
    ]
    B_BUDGET = 215.280006
    return processors, tasks, B_BUDGET
