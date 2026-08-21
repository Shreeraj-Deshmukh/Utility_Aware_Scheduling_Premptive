"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 80.959998, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.2, "seed": 1033, "set": 33, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.20"}
"""

_SPEC = '{"B": 80.959998, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.2, "seed": 1033, "set": 33, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.20"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.048193, 'e_o_k': [0.009876, 0.007900, 0.006320], 'p_i': 10, 'u_i': 4.1859},
        {'id': 1, 'e_m': 3.648051, 'e_o_k': [0.747551, 0.598041, 0.478433], 'p_i': 20, 'u_i': 1.3758},
        {'id': 2, 'e_m': 5.612216, 'e_o_k': [1.150044, 0.920035, 0.736028], 'p_i': 40, 'u_i': 3.6848},
        {'id': 3, 'e_m': 0.963244, 'e_o_k': [0.267568, 0.214054], 'p_i': 80, 'u_i': 1.6851},
        {'id': 4, 'e_m': 5.443451, 'e_o_k': [0.809652, 0.647721, 0.518177, 0.414542, 0.331633], 'p_i': 20, 'u_i': 1.3700},
        {'id': 5, 'e_m': 1.362619, 'e_o_k': [0.202674, 0.162139, 0.129712, 0.103769, 0.083015], 'p_i': 10, 'u_i': 3.3252},
        {'id': 6, 'e_m': 1.225919, 'e_o_k': [0.340533, 0.272426], 'p_i': 80, 'u_i': 4.3008},
        {'id': 7, 'e_m': 2.933902, 'e_o_k': [0.496935, 0.397548, 0.318038, 0.254431], 'p_i': 80, 'u_i': 2.2362},
    ]
    B_BUDGET = 80.959998
    return processors, tasks, B_BUDGET
