"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359991, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359991, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.356664, 'e_o_k': [0.289754, 0.231803, 0.185442], 'p_i': 10, 'u_i': 2.4893},
        {'id': 1, 'e_m': 6.050136, 'e_o_k': [0.743869, 0.595095, 0.476076], 'p_i': 20, 'u_i': 4.7173},
        {'id': 2, 'e_m': 13.537065, 'e_o_k': [2.256177, 1.804942], 'p_i': 40, 'u_i': 2.7558},
        {'id': 3, 'e_m': 31.886546, 'e_o_k': [2.845658, 2.276526, 1.821221, 1.456977, 1.165582], 'p_i': 80, 'u_i': 2.1995},
        {'id': 4, 'e_m': 6.193979, 'e_o_k': [0.761555, 0.609244, 0.487395], 'p_i': 40, 'u_i': 2.7585},
        {'id': 5, 'e_m': 1.152896, 'e_o_k': [0.102888, 0.082311, 0.065848, 0.052679, 0.042143], 'p_i': 10, 'u_i': 4.0797},
        {'id': 6, 'e_m': 0.421022, 'e_o_k': [0.042787, 0.034229, 0.027384, 0.021907], 'p_i': 10, 'u_i': 3.6908},
        {'id': 7, 'e_m': 0.251541, 'e_o_k': [0.025563, 0.020450, 0.016360, 0.013088], 'p_i': 20, 'u_i': 3.3068},
    ]
    B_BUDGET = 191.359991
    return processors, tasks, B_BUDGET
