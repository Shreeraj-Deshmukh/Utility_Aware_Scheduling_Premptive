"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600006, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600006, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.097602, 'e_o_k': [0.134951, 0.107961, 0.086369], 'p_i': 10, 'u_i': 1.3531},
        {'id': 1, 'e_m': 2.200486, 'e_o_k': [0.178936, 0.143149, 0.114519, 0.091615, 0.073292, 0.058634], 'p_i': 20, 'u_i': 3.7145},
        {'id': 2, 'e_m': 19.017007, 'e_o_k': [3.169501, 2.535601], 'p_i': 40, 'u_i': 2.6488},
        {'id': 3, 'e_m': 1.526769, 'e_o_k': [0.124152, 0.099321, 0.079457, 0.063566, 0.050853, 0.040682], 'p_i': 80, 'u_i': 4.3024},
        {'id': 4, 'e_m': 2.334588, 'e_o_k': [0.287039, 0.229632, 0.183705], 'p_i': 20, 'u_i': 4.8206},
        {'id': 5, 'e_m': 2.438930, 'e_o_k': [0.198326, 0.158661, 0.126928, 0.101543, 0.081234, 0.064987], 'p_i': 20, 'u_i': 3.2508},
        {'id': 6, 'e_m': 2.302760, 'e_o_k': [0.283126, 0.226501, 0.181201], 'p_i': 80, 'u_i': 3.3334},
        {'id': 7, 'e_m': 1.459630, 'e_o_k': [0.243272, 0.194617], 'p_i': 80, 'u_i': 2.1081},
    ]
    B_BUDGET = 119.600006
    return processors, tasks, B_BUDGET
