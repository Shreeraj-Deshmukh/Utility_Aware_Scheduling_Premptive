"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520001, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520001, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.424078, 'e_o_k': [0.037846, 0.030277, 0.024222, 0.019377, 0.015502], 'p_i': 10, 'u_i': 4.9222},
        {'id': 1, 'e_m': 1.495796, 'e_o_k': [0.152012, 0.121609, 0.097288, 0.077830], 'p_i': 20, 'u_i': 1.9107},
        {'id': 2, 'e_m': 16.031199, 'e_o_k': [1.430676, 1.144541, 0.915633, 0.732506, 0.586005], 'p_i': 40, 'u_i': 1.7322},
        {'id': 3, 'e_m': 12.506250, 'e_o_k': [1.116098, 0.892878, 0.714303, 0.571442, 0.457154], 'p_i': 80, 'u_i': 1.5709},
        {'id': 4, 'e_m': 2.351508, 'e_o_k': [0.209856, 0.167885, 0.134308, 0.107446, 0.085957], 'p_i': 20, 'u_i': 3.7661},
        {'id': 5, 'e_m': 2.193878, 'e_o_k': [0.269739, 0.215791, 0.172633], 'p_i': 20, 'u_i': 1.0932},
        {'id': 6, 'e_m': 0.129462, 'e_o_k': [0.010527, 0.008422, 0.006738, 0.005390, 0.004312, 0.003450], 'p_i': 20, 'u_i': 2.8740},
        {'id': 7, 'e_m': 11.678074, 'e_o_k': [1.435829, 1.148663, 0.918930], 'p_i': 40, 'u_i': 4.9324},
    ]
    B_BUDGET = 143.520001
    return processors, tasks, B_BUDGET
