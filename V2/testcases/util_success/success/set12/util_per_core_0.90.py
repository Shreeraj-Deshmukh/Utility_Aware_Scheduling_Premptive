"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279999, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279999, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.580787, 'e_o_k': [0.430131, 0.344105], 'p_i': 10, 'u_i': 2.5980},
        {'id': 1, 'e_m': 8.490949, 'e_o_k': [1.415158, 1.132127], 'p_i': 20, 'u_i': 2.9083},
        {'id': 2, 'e_m': 12.038574, 'e_o_k': [1.480153, 1.184122, 0.947298], 'p_i': 40, 'u_i': 4.8275},
        {'id': 3, 'e_m': 38.180805, 'e_o_k': [3.407378, 2.725902, 2.180722, 1.744577, 1.395662], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 2.473868, 'e_o_k': [0.304164, 0.243331, 0.194665], 'p_i': 20, 'u_i': 1.8333},
        {'id': 5, 'e_m': 0.335170, 'e_o_k': [0.029912, 0.023929, 0.019143, 0.015315, 0.012252], 'p_i': 20, 'u_i': 4.5368},
        {'id': 6, 'e_m': 7.420301, 'e_o_k': [0.603394, 0.482715, 0.386172, 0.308938, 0.247150, 0.197720], 'p_i': 80, 'u_i': 4.6383},
        {'id': 7, 'e_m': 8.475502, 'e_o_k': [0.756381, 0.605105, 0.484084, 0.387267, 0.309814], 'p_i': 80, 'u_i': 3.5515},
    ]
    B_BUDGET = 215.279999
    return processors, tasks, B_BUDGET
