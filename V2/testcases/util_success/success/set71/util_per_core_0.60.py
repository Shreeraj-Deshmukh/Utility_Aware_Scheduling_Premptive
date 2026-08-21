"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520001, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520001, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.224950, 'e_o_k': [0.262242, 0.209794, 0.167835, 0.134268, 0.107414, 0.085932], 'p_i': 10, 'u_i': 3.5232},
        {'id': 1, 'e_m': 0.623692, 'e_o_k': [0.103949, 0.083159], 'p_i': 20, 'u_i': 1.0606},
        {'id': 2, 'e_m': 1.517481, 'e_o_k': [0.154216, 0.123372, 0.098698, 0.078958], 'p_i': 40, 'u_i': 3.4010},
        {'id': 3, 'e_m': 35.943797, 'e_o_k': [2.922830, 2.338264, 1.870611, 1.496489, 1.197191, 0.957753], 'p_i': 80, 'u_i': 4.8241},
        {'id': 4, 'e_m': 1.883464, 'e_o_k': [0.191409, 0.153127, 0.122502, 0.098001], 'p_i': 40, 'u_i': 1.6455},
        {'id': 5, 'e_m': 9.589471, 'e_o_k': [0.974540, 0.779632, 0.623705, 0.498964], 'p_i': 40, 'u_i': 1.3745},
        {'id': 6, 'e_m': 2.568467, 'e_o_k': [0.315795, 0.252636, 0.202109], 'p_i': 40, 'u_i': 1.5038},
        {'id': 7, 'e_m': 0.161018, 'e_o_k': [0.019797, 0.015838, 0.012670], 'p_i': 20, 'u_i': 4.4242},
    ]
    B_BUDGET = 143.520001
    return processors, tasks, B_BUDGET
