"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600015, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600015, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.297217, 'e_o_k': [0.026525, 0.021220, 0.016976, 0.013581, 0.010864], 'p_i': 10, 'u_i': 4.9795},
        {'id': 1, 'e_m': 2.878995, 'e_o_k': [0.353975, 0.283180, 0.226544], 'p_i': 20, 'u_i': 4.9448},
        {'id': 2, 'e_m': 9.459297, 'e_o_k': [0.844178, 0.675342, 0.540274, 0.432219, 0.345775], 'p_i': 40, 'u_i': 4.4554},
        {'id': 3, 'e_m': 25.116295, 'e_o_k': [2.241459, 1.793167, 1.434534, 1.147627, 0.918102], 'p_i': 80, 'u_i': 2.2591},
        {'id': 4, 'e_m': 0.274465, 'e_o_k': [0.033746, 0.026997, 0.021597], 'p_i': 10, 'u_i': 2.7803},
        {'id': 5, 'e_m': 12.465646, 'e_o_k': [1.013665, 0.810932, 0.648746, 0.518996, 0.415197, 0.332158], 'p_i': 80, 'u_i': 3.4160},
        {'id': 6, 'e_m': 3.883756, 'e_o_k': [0.477511, 0.382009, 0.305607], 'p_i': 80, 'u_i': 3.4712},
        {'id': 7, 'e_m': 0.881569, 'e_o_k': [0.078674, 0.062939, 0.050351, 0.040281, 0.032225], 'p_i': 20, 'u_i': 4.3322},
    ]
    B_BUDGET = 119.600015
    return processors, tasks, B_BUDGET
