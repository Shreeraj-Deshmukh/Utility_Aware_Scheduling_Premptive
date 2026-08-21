"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680002, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680002, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.789693, 'e_o_k': [0.080253, 0.064203, 0.051362, 0.041090], 'p_i': 10, 'u_i': 4.2289},
        {'id': 1, 'e_m': 0.245294, 'e_o_k': [0.040882, 0.032706], 'p_i': 20, 'u_i': 3.6434},
        {'id': 2, 'e_m': 3.310794, 'e_o_k': [0.269223, 0.215378, 0.172303, 0.137842, 0.110274, 0.088219], 'p_i': 40, 'u_i': 4.1771},
        {'id': 3, 'e_m': 1.628519, 'e_o_k': [0.165500, 0.132400, 0.105920, 0.084736], 'p_i': 80, 'u_i': 4.0903},
        {'id': 4, 'e_m': 2.051152, 'e_o_k': [0.208450, 0.166760, 0.133408, 0.106727], 'p_i': 20, 'u_i': 2.9627},
        {'id': 5, 'e_m': 0.110349, 'e_o_k': [0.011214, 0.008971, 0.007177, 0.005742], 'p_i': 80, 'u_i': 1.9286},
        {'id': 6, 'e_m': 3.223708, 'e_o_k': [0.327613, 0.262090, 0.209672, 0.167738], 'p_i': 10, 'u_i': 3.5955},
        {'id': 7, 'e_m': 7.173276, 'e_o_k': [0.640166, 0.512133, 0.409706, 0.327765, 0.262212], 'p_i': 40, 'u_i': 1.8182},
    ]
    B_BUDGET = 95.680002
    return processors, tasks, B_BUDGET
