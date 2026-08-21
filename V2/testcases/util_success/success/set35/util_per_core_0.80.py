"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359998, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359998, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.030917, 'e_o_k': [0.246464, 0.197171, 0.157737, 0.126190, 0.100952, 0.080761], 'p_i': 10, 'u_i': 3.9981},
        {'id': 1, 'e_m': 5.514618, 'e_o_k': [0.560429, 0.448343, 0.358674, 0.286939], 'p_i': 20, 'u_i': 1.1221},
        {'id': 2, 'e_m': 7.933469, 'e_o_k': [0.975427, 0.780341, 0.624273], 'p_i': 40, 'u_i': 1.0173},
        {'id': 3, 'e_m': 16.973375, 'e_o_k': [2.828896, 2.263117], 'p_i': 80, 'u_i': 4.7591},
        {'id': 4, 'e_m': 7.904232, 'e_o_k': [0.803276, 0.642620, 0.514096, 0.411277], 'p_i': 80, 'u_i': 4.6573},
        {'id': 5, 'e_m': 20.958678, 'e_o_k': [2.576887, 2.061509, 1.649207], 'p_i': 80, 'u_i': 3.1574},
        {'id': 6, 'e_m': 2.102076, 'e_o_k': [0.170934, 0.136747, 0.109398, 0.087518, 0.070014, 0.056012], 'p_i': 10, 'u_i': 2.6010},
        {'id': 7, 'e_m': 0.793590, 'e_o_k': [0.097573, 0.078058, 0.062446], 'p_i': 20, 'u_i': 2.4102},
    ]
    B_BUDGET = 191.359998
    return processors, tasks, B_BUDGET
