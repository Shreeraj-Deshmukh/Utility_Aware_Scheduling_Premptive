"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120022, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120022, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.294151, 'e_o_k': [0.382359, 0.305887], 'p_i': 10, 'u_i': 4.4926},
        {'id': 1, 'e_m': 5.673110, 'e_o_k': [0.697514, 0.558011, 0.446409], 'p_i': 20, 'u_i': 3.2922},
        {'id': 2, 'e_m': 5.965516, 'e_o_k': [0.994253, 0.795402], 'p_i': 40, 'u_i': 3.7450},
        {'id': 3, 'e_m': 35.824210, 'e_o_k': [3.640672, 2.912537, 2.330030, 1.864024], 'p_i': 80, 'u_i': 4.8771},
        {'id': 4, 'e_m': 0.774142, 'e_o_k': [0.129024, 0.103219], 'p_i': 20, 'u_i': 4.0203},
        {'id': 5, 'e_m': 3.332224, 'e_o_k': [0.338641, 0.270913, 0.216730, 0.173384], 'p_i': 10, 'u_i': 3.4418},
        {'id': 6, 'e_m': 3.258606, 'e_o_k': [0.400648, 0.320519, 0.256415], 'p_i': 10, 'u_i': 4.8003},
        {'id': 7, 'e_m': 3.921988, 'e_o_k': [0.482212, 0.385769, 0.308615], 'p_i': 10, 'u_i': 3.9154},
    ]
    B_BUDGET = 263.120022
    return processors, tasks, B_BUDGET
