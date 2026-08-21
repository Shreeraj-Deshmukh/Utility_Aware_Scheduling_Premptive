"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440006, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440006, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.062081, 'e_o_k': [0.253535, 0.202828, 0.162262], 'p_i': 10, 'u_i': 2.4893},
        {'id': 1, 'e_m': 5.293869, 'e_o_k': [0.650885, 0.520708, 0.416567], 'p_i': 20, 'u_i': 4.7173},
        {'id': 2, 'e_m': 11.844932, 'e_o_k': [1.974155, 1.579324], 'p_i': 40, 'u_i': 2.7558},
        {'id': 3, 'e_m': 27.900728, 'e_o_k': [2.489951, 1.991961, 1.593568, 1.274855, 1.019884], 'p_i': 80, 'u_i': 2.1995},
        {'id': 4, 'e_m': 5.419731, 'e_o_k': [0.666360, 0.533088, 0.426471], 'p_i': 40, 'u_i': 2.7585},
        {'id': 5, 'e_m': 1.008784, 'e_o_k': [0.090027, 0.072022, 0.057617, 0.046094, 0.036875], 'p_i': 10, 'u_i': 4.0797},
        {'id': 6, 'e_m': 0.368395, 'e_o_k': [0.037438, 0.029951, 0.023961, 0.019169], 'p_i': 10, 'u_i': 3.6908},
        {'id': 7, 'e_m': 0.220098, 'e_o_k': [0.022368, 0.017894, 0.014315, 0.011452], 'p_i': 20, 'u_i': 3.3068},
    ]
    B_BUDGET = 167.440006
    return processors, tasks, B_BUDGET
