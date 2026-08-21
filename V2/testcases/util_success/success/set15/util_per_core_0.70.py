"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440003, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440003, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.871130, 'e_o_k': [0.314787, 0.251830, 0.201464, 0.161171, 0.128937, 0.103150], 'p_i': 10, 'u_i': 4.6267},
        {'id': 1, 'e_m': 3.674384, 'e_o_k': [0.612397, 0.489918], 'p_i': 20, 'u_i': 4.4310},
        {'id': 2, 'e_m': 0.447128, 'e_o_k': [0.039903, 0.031923, 0.025538, 0.020430, 0.016344], 'p_i': 40, 'u_i': 4.5357},
        {'id': 3, 'e_m': 10.783872, 'e_o_k': [0.876909, 0.701527, 0.561222, 0.448977, 0.359182, 0.287345], 'p_i': 80, 'u_i': 2.3203},
        {'id': 4, 'e_m': 5.700196, 'e_o_k': [0.700844, 0.560675, 0.448540], 'p_i': 80, 'u_i': 3.8723},
        {'id': 5, 'e_m': 3.137225, 'e_o_k': [0.318824, 0.255059, 0.204047, 0.163238], 'p_i': 40, 'u_i': 1.1816},
        {'id': 6, 'e_m': 25.545470, 'e_o_k': [2.077273, 1.661818, 1.329455, 1.063564, 0.850851, 0.680681], 'p_i': 80, 'u_i': 4.5942},
        {'id': 7, 'e_m': 2.141897, 'e_o_k': [0.191150, 0.152920, 0.122336, 0.097869, 0.078295], 'p_i': 10, 'u_i': 3.3631},
    ]
    B_BUDGET = 167.440003
    return processors, tasks, B_BUDGET
