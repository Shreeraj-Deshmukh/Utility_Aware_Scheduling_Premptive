"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760009, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760009, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.612475, 'e_o_k': [0.131121, 0.104897, 0.083918, 0.067134, 0.053707, 0.042966], 'p_i': 10, 'u_i': 3.5232},
        {'id': 1, 'e_m': 0.311846, 'e_o_k': [0.051974, 0.041579], 'p_i': 20, 'u_i': 1.0606},
        {'id': 2, 'e_m': 0.758741, 'e_o_k': [0.077108, 0.061686, 0.049349, 0.039479], 'p_i': 40, 'u_i': 3.4010},
        {'id': 3, 'e_m': 17.971898, 'e_o_k': [1.461415, 1.169132, 0.935306, 0.748245, 0.598596, 0.478876], 'p_i': 80, 'u_i': 4.8241},
        {'id': 4, 'e_m': 0.941732, 'e_o_k': [0.095704, 0.076564, 0.061251, 0.049001], 'p_i': 40, 'u_i': 1.6455},
        {'id': 5, 'e_m': 4.794736, 'e_o_k': [0.487270, 0.389816, 0.311853, 0.249482], 'p_i': 40, 'u_i': 1.3745},
        {'id': 6, 'e_m': 1.284234, 'e_o_k': [0.157898, 0.126318, 0.101054], 'p_i': 40, 'u_i': 1.5038},
        {'id': 7, 'e_m': 0.080509, 'e_o_k': [0.009899, 0.007919, 0.006335], 'p_i': 20, 'u_i': 4.4242},
    ]
    B_BUDGET = 71.760009
    return processors, tasks, B_BUDGET
