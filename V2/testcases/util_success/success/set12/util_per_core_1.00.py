"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.2, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.2, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.126339, 'e_o_k': [0.507337, 0.405869, 0.324696], 'p_i': 10, 'u_i': 3.4529},
        {'id': 1, 'e_m': 8.532709, 'e_o_k': [0.693852, 0.555081, 0.444065, 0.355252, 0.284202, 0.227361], 'p_i': 20, 'u_i': 4.6383},
        {'id': 2, 'e_m': 7.480266, 'e_o_k': [0.667563, 0.534050, 0.427240, 0.341792, 0.273434], 'p_i': 40, 'u_i': 3.5515},
        {'id': 3, 'e_m': 15.967809, 'e_o_k': [1.298449, 1.038759, 0.831008, 0.664806, 0.531845, 0.425476], 'p_i': 80, 'u_i': 2.1438},
        {'id': 4, 'e_m': 1.694903, 'e_o_k': [0.282484, 0.225987], 'p_i': 80, 'u_i': 3.9145},
        {'id': 5, 'e_m': 18.630296, 'e_o_k': [3.105049, 2.484039], 'p_i': 80, 'u_i': 4.3793},
        {'id': 6, 'e_m': 2.259233, 'e_o_k': [0.229597, 0.183678, 0.146942, 0.117554], 'p_i': 40, 'u_i': 4.6043},
        {'id': 7, 'e_m': 9.271611, 'e_o_k': [1.545268, 1.236215], 'p_i': 20, 'u_i': 3.0442},
    ]
    B_BUDGET = 239.200000
    return processors, tasks, B_BUDGET
