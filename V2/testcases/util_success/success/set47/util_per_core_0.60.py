"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.51999, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.51999, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.650154, 'e_o_k': [0.325751, 0.260601, 0.208481, 0.166785, 0.133428], 'p_i': 10, 'u_i': 3.4259},
        {'id': 1, 'e_m': 2.517997, 'e_o_k': [0.255894, 0.204715, 0.163772, 0.131018], 'p_i': 20, 'u_i': 1.3819},
        {'id': 2, 'e_m': 4.046576, 'e_o_k': [0.674429, 0.539543], 'p_i': 40, 'u_i': 1.7445},
        {'id': 3, 'e_m': 8.375127, 'e_o_k': [0.681038, 0.544830, 0.435864, 0.348691, 0.278953, 0.223162], 'p_i': 80, 'u_i': 3.6642},
        {'id': 4, 'e_m': 1.439950, 'e_o_k': [0.146336, 0.117069, 0.093655, 0.074924], 'p_i': 10, 'u_i': 2.6174},
        {'id': 5, 'e_m': 1.800550, 'e_o_k': [0.160687, 0.128549, 0.102840, 0.082272, 0.065817], 'p_i': 10, 'u_i': 2.3254},
        {'id': 6, 'e_m': 0.292991, 'e_o_k': [0.048832, 0.039065], 'p_i': 10, 'u_i': 3.2626},
        {'id': 7, 'e_m': 5.995288, 'e_o_k': [0.535039, 0.428031, 0.342425, 0.273940, 0.219152], 'p_i': 40, 'u_i': 1.6837},
    ]
    B_BUDGET = 143.519990
    return processors, tasks, B_BUDGET
