"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520003, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520003, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.401886, 'e_o_k': [0.040842, 0.032674, 0.026139, 0.020911], 'p_i': 10, 'u_i': 2.0521},
        {'id': 1, 'e_m': 3.564516, 'e_o_k': [0.318109, 0.254487, 0.203590, 0.162872, 0.130297], 'p_i': 20, 'u_i': 4.1261},
        {'id': 2, 'e_m': 6.336196, 'e_o_k': [0.643922, 0.515138, 0.412110, 0.329688], 'p_i': 40, 'u_i': 2.8820},
        {'id': 3, 'e_m': 32.439253, 'e_o_k': [2.637852, 2.110282, 1.688225, 1.350580, 1.080464, 0.864371], 'p_i': 80, 'u_i': 1.8301},
        {'id': 4, 'e_m': 0.007411, 'e_o_k': [0.001235, 0.000988], 'p_i': 20, 'u_i': 2.8656},
        {'id': 5, 'e_m': 4.037729, 'e_o_k': [0.328335, 0.262668, 0.210134, 0.168107, 0.134486, 0.107589], 'p_i': 20, 'u_i': 4.7863},
        {'id': 6, 'e_m': 0.200051, 'e_o_k': [0.016267, 0.013014, 0.010411, 0.008329, 0.006663, 0.005331], 'p_i': 20, 'u_i': 3.1132},
        {'id': 7, 'e_m': 2.054305, 'e_o_k': [0.208771, 0.167017, 0.133613, 0.106891], 'p_i': 10, 'u_i': 2.8421},
    ]
    B_BUDGET = 143.520003
    return processors, tasks, B_BUDGET
