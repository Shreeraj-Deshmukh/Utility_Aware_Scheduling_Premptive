"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360017, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360017, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.642370, 'e_o_k': [0.201931, 0.161545, 0.129236], 'p_i': 10, 'u_i': 4.1932},
        {'id': 1, 'e_m': 2.235298, 'e_o_k': [0.372550, 0.298040], 'p_i': 20, 'u_i': 2.7154},
        {'id': 2, 'e_m': 1.267925, 'e_o_k': [0.155892, 0.124714, 0.099771], 'p_i': 40, 'u_i': 4.3253},
        {'id': 3, 'e_m': 27.232014, 'e_o_k': [2.767481, 2.213985, 1.771188, 1.416950], 'p_i': 80, 'u_i': 1.0005},
        {'id': 4, 'e_m': 6.506856, 'e_o_k': [0.580693, 0.464554, 0.371643, 0.297315, 0.237852], 'p_i': 80, 'u_i': 1.9051},
        {'id': 5, 'e_m': 4.883049, 'e_o_k': [0.435779, 0.348623, 0.278899, 0.223119, 0.178495], 'p_i': 20, 'u_i': 2.2450},
        {'id': 6, 'e_m': 14.097553, 'e_o_k': [2.349592, 1.879674], 'p_i': 40, 'u_i': 3.5907},
        {'id': 7, 'e_m': 10.958914, 'e_o_k': [1.347408, 1.077926, 0.862341], 'p_i': 40, 'u_i': 4.3441},
    ]
    B_BUDGET = 191.360017
    return processors, tasks, B_BUDGET
