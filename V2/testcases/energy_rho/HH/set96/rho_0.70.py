"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 145.72802, "H": 80, "J": 32, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.7, "seed": 1096, "set": 96, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.70"}
"""

_SPEC = '{"B": 145.72802, "H": 80, "J": 32, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.7, "seed": 1096, "set": 96, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.505787, 'e_o_k': [0.393390, 0.314712], 'p_i': 10, 'u_i': 2.8589},
        {'id': 1, 'e_m': 0.195219, 'e_o_k': [0.112011, 0.089609, 0.071687], 'p_i': 20, 'u_i': 2.7598},
        {'id': 2, 'e_m': 10.184228, 'e_o_k': [7.921066, 6.336853], 'p_i': 40, 'u_i': 2.0735},
        {'id': 3, 'e_m': 6.561179, 'e_o_k': [2.489822, 1.991857, 1.593486, 1.274789, 1.019831, 0.815865], 'p_i': 80, 'u_i': 3.6242},
        {'id': 4, 'e_m': 4.539403, 'e_o_k': [3.530646, 2.824517], 'p_i': 20, 'u_i': 2.1240},
        {'id': 5, 'e_m': 6.765491, 'e_o_k': [3.208566, 2.566853, 2.053482, 1.642786], 'p_i': 80, 'u_i': 2.2796},
        {'id': 6, 'e_m': 1.084629, 'e_o_k': [0.451714, 0.361371, 0.289097, 0.231277, 0.185022], 'p_i': 20, 'u_i': 4.8637},
        {'id': 7, 'e_m': 0.372698, 'e_o_k': [0.213843, 0.171074, 0.136860], 'p_i': 10, 'u_i': 2.9768},
    ]
    B_BUDGET = 145.728020
    return processors, tasks, B_BUDGET
