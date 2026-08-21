"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279985, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279985, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.170798, 'e_o_k': [0.143951, 0.115160, 0.092128], 'p_i': 10, 'u_i': 2.4453},
        {'id': 1, 'e_m': 1.794803, 'e_o_k': [0.160174, 0.128139, 0.102511, 0.082009, 0.065607], 'p_i': 20, 'u_i': 4.4841},
        {'id': 2, 'e_m': 1.177503, 'e_o_k': [0.144775, 0.115820, 0.092656], 'p_i': 40, 'u_i': 2.2759},
        {'id': 3, 'e_m': 33.000115, 'e_o_k': [5.500019, 4.400015], 'p_i': 80, 'u_i': 4.2544},
        {'id': 4, 'e_m': 5.599820, 'e_o_k': [0.569087, 0.455270, 0.364216, 0.291373], 'p_i': 20, 'u_i': 1.1205},
        {'id': 5, 'e_m': 12.674573, 'e_o_k': [1.558349, 1.246679, 0.997343], 'p_i': 40, 'u_i': 1.0704},
        {'id': 6, 'e_m': 7.722689, 'e_o_k': [0.627983, 0.502387, 0.401909, 0.321527, 0.257222, 0.205778], 'p_i': 20, 'u_i': 1.5805},
        {'id': 7, 'e_m': 6.730050, 'e_o_k': [1.121675, 0.897340], 'p_i': 40, 'u_i': 2.6610},
    ]
    B_BUDGET = 215.279985
    return processors, tasks, B_BUDGET
