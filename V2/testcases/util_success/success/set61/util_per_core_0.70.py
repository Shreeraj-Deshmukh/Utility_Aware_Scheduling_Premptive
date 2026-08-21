"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439995, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439995, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.200347, 'e_o_k': [0.121986, 0.097589, 0.078071, 0.062457], 'p_i': 10, 'u_i': 3.1491},
        {'id': 1, 'e_m': 4.347716, 'e_o_k': [0.441841, 0.353473, 0.282778, 0.226223], 'p_i': 20, 'u_i': 2.2531},
        {'id': 2, 'e_m': 0.084124, 'e_o_k': [0.007507, 0.006006, 0.004805, 0.003844, 0.003075], 'p_i': 40, 'u_i': 4.0598},
        {'id': 3, 'e_m': 19.812357, 'e_o_k': [2.013451, 1.610761, 1.288609, 1.030887], 'p_i': 80, 'u_i': 4.5014},
        {'id': 4, 'e_m': 17.260214, 'e_o_k': [2.876702, 2.301362], 'p_i': 40, 'u_i': 4.8694},
        {'id': 5, 'e_m': 5.612535, 'e_o_k': [0.500881, 0.400705, 0.320564, 0.256451, 0.205161], 'p_i': 40, 'u_i': 3.6293},
        {'id': 6, 'e_m': 16.812344, 'e_o_k': [1.500388, 1.200310, 0.960248, 0.768198, 0.614559], 'p_i': 80, 'u_i': 4.0966},
        {'id': 7, 'e_m': 2.467914, 'e_o_k': [0.250804, 0.200643, 0.160515, 0.128412], 'p_i': 80, 'u_i': 3.0738},
    ]
    B_BUDGET = 167.439995
    return processors, tasks, B_BUDGET
