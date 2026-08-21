"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760014, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760014, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.238546, 'e_o_k': [0.039758, 0.031806], 'p_i': 10, 'u_i': 1.8047},
        {'id': 1, 'e_m': 1.828239, 'e_o_k': [0.304706, 0.243765], 'p_i': 20, 'u_i': 1.0945},
        {'id': 2, 'e_m': 1.493688, 'e_o_k': [0.133302, 0.106641, 0.085313, 0.068250, 0.054600], 'p_i': 40, 'u_i': 2.4137},
        {'id': 3, 'e_m': 8.054795, 'e_o_k': [1.342466, 1.073973], 'p_i': 80, 'u_i': 1.6729},
        {'id': 4, 'e_m': 1.377733, 'e_o_k': [0.112033, 0.089626, 0.071701, 0.057361, 0.045889, 0.036711], 'p_i': 40, 'u_i': 2.8481},
        {'id': 5, 'e_m': 1.277194, 'e_o_k': [0.129796, 0.103837, 0.083070, 0.066456], 'p_i': 10, 'u_i': 3.6691},
        {'id': 6, 'e_m': 2.145328, 'e_o_k': [0.218021, 0.174417, 0.139534, 0.111627], 'p_i': 20, 'u_i': 3.0767},
        {'id': 7, 'e_m': 6.182177, 'e_o_k': [0.502714, 0.402171, 0.321737, 0.257390, 0.205912, 0.164729], 'p_i': 80, 'u_i': 1.7471},
    ]
    B_BUDGET = 71.760014
    return processors, tasks, B_BUDGET
