"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439987, "H": 80, "J": 47, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439987, "H": 80, "J": 47, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.444944, 'e_o_k': [0.074157, 0.059326], 'p_i': 10, 'u_i': 2.4482},
        {'id': 1, 'e_m': 8.570359, 'e_o_k': [0.870971, 0.696777, 0.557422, 0.445937], 'p_i': 20, 'u_i': 4.8654},
        {'id': 2, 'e_m': 11.538579, 'e_o_k': [1.923097, 1.538477], 'p_i': 40, 'u_i': 2.4832},
        {'id': 3, 'e_m': 8.698045, 'e_o_k': [0.883948, 0.707158, 0.565727, 0.452581], 'p_i': 80, 'u_i': 1.7299},
        {'id': 4, 'e_m': 0.517230, 'e_o_k': [0.063594, 0.050875, 0.040700], 'p_i': 10, 'u_i': 4.6595},
        {'id': 5, 'e_m': 0.390808, 'e_o_k': [0.039716, 0.031773, 0.025418, 0.020335], 'p_i': 10, 'u_i': 1.6443},
        {'id': 6, 'e_m': 2.865930, 'e_o_k': [0.477655, 0.382124], 'p_i': 10, 'u_i': 1.9160},
        {'id': 7, 'e_m': 1.524008, 'e_o_k': [0.123927, 0.099142, 0.079313, 0.063451, 0.050761, 0.040608], 'p_i': 10, 'u_i': 1.4840},
    ]
    B_BUDGET = 167.439987
    return processors, tasks, B_BUDGET
