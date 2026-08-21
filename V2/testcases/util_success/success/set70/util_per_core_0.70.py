"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439994, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439994, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.962084, 'e_o_k': [0.327014, 0.261611], 'p_i': 10, 'u_i': 2.9208},
        {'id': 1, 'e_m': 7.956302, 'e_o_k': [0.646980, 0.517584, 0.414067, 0.331254, 0.265003, 0.212002], 'p_i': 20, 'u_i': 4.6964},
        {'id': 2, 'e_m': 18.503151, 'e_o_k': [2.274978, 1.819982, 1.455986], 'p_i': 40, 'u_i': 4.6519},
        {'id': 3, 'e_m': 6.440452, 'e_o_k': [1.073409, 0.858727], 'p_i': 80, 'u_i': 4.9020},
        {'id': 4, 'e_m': 1.091888, 'e_o_k': [0.088789, 0.071031, 0.056825, 0.045460, 0.036368, 0.029094], 'p_i': 80, 'u_i': 1.1409},
        {'id': 5, 'e_m': 5.531282, 'e_o_k': [0.493629, 0.394904, 0.315923, 0.252738, 0.202191], 'p_i': 40, 'u_i': 1.3844},
        {'id': 6, 'e_m': 8.314031, 'e_o_k': [0.741971, 0.593577, 0.474861, 0.379889, 0.303911], 'p_i': 80, 'u_i': 3.8571},
        {'id': 7, 'e_m': 0.140720, 'e_o_k': [0.023453, 0.018763], 'p_i': 20, 'u_i': 3.6185},
    ]
    B_BUDGET = 167.439994
    return processors, tasks, B_BUDGET
