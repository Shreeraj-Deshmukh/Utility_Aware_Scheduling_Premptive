"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439988, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439988, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.494758, 'e_o_k': [0.044154, 0.035323, 0.028258, 0.022607, 0.018085], 'p_i': 10, 'u_i': 4.9222},
        {'id': 1, 'e_m': 1.745095, 'e_o_k': [0.177347, 0.141878, 0.113502, 0.090802], 'p_i': 20, 'u_i': 1.9107},
        {'id': 2, 'e_m': 18.703066, 'e_o_k': [1.669122, 1.335297, 1.068238, 0.854590, 0.683672], 'p_i': 40, 'u_i': 1.7322},
        {'id': 3, 'e_m': 14.590625, 'e_o_k': [1.302114, 1.041691, 0.833353, 0.666683, 0.533346], 'p_i': 80, 'u_i': 1.5709},
        {'id': 4, 'e_m': 2.743426, 'e_o_k': [0.244832, 0.195866, 0.156693, 0.125354, 0.100283], 'p_i': 20, 'u_i': 3.7661},
        {'id': 5, 'e_m': 2.559524, 'e_o_k': [0.314696, 0.251756, 0.201405], 'p_i': 20, 'u_i': 1.0932},
        {'id': 6, 'e_m': 0.151039, 'e_o_k': [0.012282, 0.009826, 0.007860, 0.006288, 0.005031, 0.004025], 'p_i': 20, 'u_i': 2.8740},
        {'id': 7, 'e_m': 13.624419, 'e_o_k': [1.675133, 1.340107, 1.072085], 'p_i': 40, 'u_i': 4.9324},
    ]
    B_BUDGET = 167.439988
    return processors, tasks, B_BUDGET
