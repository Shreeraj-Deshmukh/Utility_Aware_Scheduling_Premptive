"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760002, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760002, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.038730, 'e_o_k': [0.003936, 0.003149, 0.002519, 0.002015], 'p_i': 10, 'u_i': 4.0574},
        {'id': 1, 'e_m': 1.849749, 'e_o_k': [0.165078, 0.132062, 0.105650, 0.084520, 0.067616], 'p_i': 20, 'u_i': 2.7090},
        {'id': 2, 'e_m': 2.810780, 'e_o_k': [0.285648, 0.228519, 0.182815, 0.146252], 'p_i': 40, 'u_i': 3.6072},
        {'id': 3, 'e_m': 3.115342, 'e_o_k': [0.253329, 0.202663, 0.162131, 0.129705, 0.103764, 0.083011], 'p_i': 80, 'u_i': 4.5999},
        {'id': 4, 'e_m': 0.289777, 'e_o_k': [0.029449, 0.023559, 0.018847, 0.015078], 'p_i': 20, 'u_i': 4.5815},
        {'id': 5, 'e_m': 3.286437, 'e_o_k': [0.267242, 0.213794, 0.171035, 0.136828, 0.109462, 0.087570], 'p_i': 20, 'u_i': 4.3913},
        {'id': 6, 'e_m': 1.333362, 'e_o_k': [0.222227, 0.177782], 'p_i': 80, 'u_i': 2.4366},
        {'id': 7, 'e_m': 7.958021, 'e_o_k': [0.647120, 0.517696, 0.414157, 0.331325, 0.265060, 0.212048], 'p_i': 40, 'u_i': 1.2704},
    ]
    B_BUDGET = 71.760002
    return processors, tasks, B_BUDGET
