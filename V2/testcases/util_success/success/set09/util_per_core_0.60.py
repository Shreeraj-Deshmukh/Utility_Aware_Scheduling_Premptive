"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.52001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.52001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.605841, 'e_o_k': [0.434307, 0.347446], 'p_i': 10, 'u_i': 1.8132},
        {'id': 1, 'e_m': 2.121096, 'e_o_k': [0.172480, 0.137984, 0.110388, 0.088310, 0.070648, 0.056518], 'p_i': 20, 'u_i': 1.3118},
        {'id': 2, 'e_m': 13.342442, 'e_o_k': [1.190722, 0.952578, 0.762062, 0.609650, 0.487720], 'p_i': 40, 'u_i': 1.6432},
        {'id': 3, 'e_m': 5.988481, 'e_o_k': [0.998080, 0.798464], 'p_i': 80, 'u_i': 3.2827},
        {'id': 4, 'e_m': 0.234033, 'e_o_k': [0.020886, 0.016709, 0.013367, 0.010694, 0.008555], 'p_i': 20, 'u_i': 1.0597},
        {'id': 5, 'e_m': 0.528266, 'e_o_k': [0.064951, 0.051961, 0.041568], 'p_i': 20, 'u_i': 4.4596},
        {'id': 6, 'e_m': 7.690632, 'e_o_k': [0.781568, 0.625255, 0.500204, 0.400163], 'p_i': 40, 'u_i': 4.8824},
        {'id': 7, 'e_m': 1.945633, 'e_o_k': [0.239217, 0.191374, 0.153099], 'p_i': 10, 'u_i': 1.5609},
    ]
    B_BUDGET = 143.520010
    return processors, tasks, B_BUDGET
