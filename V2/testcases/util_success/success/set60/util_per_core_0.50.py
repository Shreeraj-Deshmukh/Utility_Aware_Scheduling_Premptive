"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600012, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600012, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.820777, 'e_o_k': [0.185038, 0.148031, 0.118425, 0.094740], 'p_i': 10, 'u_i': 4.9967},
        {'id': 1, 'e_m': 8.091228, 'e_o_k': [0.994823, 0.795859, 0.636687], 'p_i': 20, 'u_i': 3.1686},
        {'id': 2, 'e_m': 1.337538, 'e_o_k': [0.164451, 0.131561, 0.105249], 'p_i': 40, 'u_i': 1.4833},
        {'id': 3, 'e_m': 11.876220, 'e_o_k': [0.965735, 0.772588, 0.618070, 0.494456, 0.395565, 0.316452], 'p_i': 80, 'u_i': 1.9048},
        {'id': 4, 'e_m': 0.456794, 'e_o_k': [0.076132, 0.060906], 'p_i': 40, 'u_i': 4.4078},
        {'id': 5, 'e_m': 0.230055, 'e_o_k': [0.028285, 0.022628, 0.018103], 'p_i': 10, 'u_i': 3.6020},
        {'id': 6, 'e_m': 6.603334, 'e_o_k': [0.671070, 0.536856, 0.429485, 0.343588], 'p_i': 40, 'u_i': 4.8789},
        {'id': 7, 'e_m': 0.319610, 'e_o_k': [0.032481, 0.025985, 0.020788, 0.016630], 'p_i': 10, 'u_i': 3.0372},
    ]
    B_BUDGET = 119.600012
    return processors, tasks, B_BUDGET
