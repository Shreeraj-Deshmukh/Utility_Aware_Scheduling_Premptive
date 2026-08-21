"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440008, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440008, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.126759, 'e_o_k': [0.010308, 0.008246, 0.006597, 0.005278, 0.004222, 0.003378], 'p_i': 10, 'u_i': 2.1441},
        {'id': 1, 'e_m': 2.009294, 'e_o_k': [0.179316, 0.143453, 0.114762, 0.091810, 0.073448], 'p_i': 20, 'u_i': 1.5180},
        {'id': 2, 'e_m': 17.657424, 'e_o_k': [1.794454, 1.435563, 1.148450, 0.918760], 'p_i': 40, 'u_i': 2.4726},
        {'id': 3, 'e_m': 27.360283, 'e_o_k': [3.363969, 2.691175, 2.152940], 'p_i': 80, 'u_i': 4.1932},
        {'id': 4, 'e_m': 9.288637, 'e_o_k': [1.548106, 1.238485], 'p_i': 80, 'u_i': 2.7154},
        {'id': 5, 'e_m': 7.574635, 'e_o_k': [0.931308, 0.745046, 0.596037], 'p_i': 40, 'u_i': 4.3253},
        {'id': 6, 'e_m': 8.161169, 'e_o_k': [0.829387, 0.663510, 0.530808, 0.424646], 'p_i': 80, 'u_i': 1.0005},
        {'id': 7, 'e_m': 3.837270, 'e_o_k': [0.342450, 0.273960, 0.219168, 0.175335, 0.140268], 'p_i': 40, 'u_i': 1.9051},
    ]
    B_BUDGET = 167.440008
    return processors, tasks, B_BUDGET
