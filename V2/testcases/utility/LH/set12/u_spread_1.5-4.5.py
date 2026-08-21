"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 25, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 25, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.573508, 'e_o_k': [0.446062, 0.356850], 'p_i': 10, 'u_i': 2.6985},
        {'id': 1, 'e_m': 1.886878, 'e_o_k': [1.467571, 1.174057], 'p_i': 20, 'u_i': 2.9312},
        {'id': 2, 'e_m': 2.675239, 'e_o_k': [1.534973, 1.227978, 0.982383], 'p_i': 40, 'u_i': 4.3706},
        {'id': 3, 'e_m': 8.484623, 'e_o_k': [3.533577, 2.826862, 2.261489, 1.809191, 1.447353], 'p_i': 80, 'u_i': 3.6618},
        {'id': 4, 'e_m': 0.549748, 'e_o_k': [0.315429, 0.252344, 0.201875], 'p_i': 20, 'u_i': 2.1250},
        {'id': 5, 'e_m': 0.074482, 'e_o_k': [0.031019, 0.024816, 0.019852, 0.015882, 0.012706], 'p_i': 20, 'u_i': 4.1526},
        {'id': 6, 'e_m': 1.648956, 'e_o_k': [0.625742, 0.500594, 0.400475, 0.320380, 0.256304, 0.205043], 'p_i': 80, 'u_i': 4.2287},
        {'id': 7, 'e_m': 1.883445, 'e_o_k': [0.784395, 0.627516, 0.502013, 0.401610, 0.321288], 'p_i': 80, 'u_i': 3.4136},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET
