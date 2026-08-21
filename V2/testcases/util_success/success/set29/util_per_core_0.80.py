"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360008, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360008, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.278645, 'e_o_k': [0.024867, 0.019894, 0.015915, 0.012732, 0.010186], 'p_i': 10, 'u_i': 1.7922},
        {'id': 1, 'e_m': 6.365211, 'e_o_k': [0.646871, 0.517497, 0.413997, 0.331198], 'p_i': 20, 'u_i': 4.9529},
        {'id': 2, 'e_m': 8.880289, 'e_o_k': [1.480048, 1.184039], 'p_i': 40, 'u_i': 2.3587},
        {'id': 3, 'e_m': 3.508011, 'e_o_k': [0.584669, 0.467735], 'p_i': 80, 'u_i': 4.5300},
        {'id': 4, 'e_m': 1.558331, 'e_o_k': [0.126718, 0.101375, 0.081100, 0.064880, 0.051904, 0.041523], 'p_i': 80, 'u_i': 3.1308},
        {'id': 5, 'e_m': 18.460747, 'e_o_k': [1.501167, 1.200933, 0.960747, 0.768597, 0.614878, 0.491902], 'p_i': 40, 'u_i': 2.3635},
        {'id': 6, 'e_m': 29.487756, 'e_o_k': [3.625544, 2.900435, 2.320348], 'p_i': 80, 'u_i': 1.8340},
        {'id': 7, 'e_m': 1.384228, 'e_o_k': [0.112561, 0.090049, 0.072039, 0.057631, 0.046105, 0.036884], 'p_i': 10, 'u_i': 2.0052},
    ]
    B_BUDGET = 191.360008
    return processors, tasks, B_BUDGET
