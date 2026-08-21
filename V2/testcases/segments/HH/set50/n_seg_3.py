"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640006, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640006, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.195644, 'e_o_k': [0.686025, 0.548820, 0.439056], 'p_i': 10, 'u_i': 1.3138},
        {'id': 1, 'e_m': 1.074656, 'e_o_k': [0.616606, 0.493285, 0.394628], 'p_i': 20, 'u_i': 3.5906},
        {'id': 2, 'e_m': 3.707536, 'e_o_k': [2.127275, 1.701820, 1.361456], 'p_i': 40, 'u_i': 2.7107},
        {'id': 3, 'e_m': 9.930702, 'e_o_k': [5.697944, 4.558355, 3.646684], 'p_i': 80, 'u_i': 4.0673},
        {'id': 4, 'e_m': 0.251715, 'e_o_k': [0.144427, 0.115541, 0.092433], 'p_i': 10, 'u_i': 2.2713},
        {'id': 5, 'e_m': 1.973974, 'e_o_k': [1.132608, 0.906086, 0.724869], 'p_i': 80, 'u_i': 2.2740},
        {'id': 6, 'e_m': 23.874105, 'e_o_k': [13.698257, 10.958606, 8.766885], 'p_i': 80, 'u_i': 2.9164},
        {'id': 7, 'e_m': 2.464327, 'e_o_k': [1.413958, 1.131166, 0.904933], 'p_i': 40, 'u_i': 4.5766},
    ]
    B_BUDGET = 176.640006
    return processors, tasks, B_BUDGET
