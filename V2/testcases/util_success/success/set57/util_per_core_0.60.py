"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520006, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520006, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.302232, 'e_o_k': [0.026972, 0.021578, 0.017262, 0.013810, 0.011048], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 2.162744, 'e_o_k': [0.175867, 0.140694, 0.112555, 0.090044, 0.072035, 0.057628], 'p_i': 20, 'u_i': 3.3967},
        {'id': 2, 'e_m': 12.992836, 'e_o_k': [2.165473, 1.732378], 'p_i': 40, 'u_i': 1.9449},
        {'id': 3, 'e_m': 13.353259, 'e_o_k': [2.225543, 1.780434], 'p_i': 80, 'u_i': 4.6056},
        {'id': 4, 'e_m': 8.990438, 'e_o_k': [1.498406, 1.198725], 'p_i': 40, 'u_i': 2.0280},
        {'id': 5, 'e_m': 6.513619, 'e_o_k': [0.529666, 0.423733, 0.338986, 0.271189, 0.216951, 0.173561], 'p_i': 80, 'u_i': 1.2717},
        {'id': 6, 'e_m': 1.952031, 'e_o_k': [0.325338, 0.260271], 'p_i': 10, 'u_i': 1.1584},
        {'id': 7, 'e_m': 5.481498, 'e_o_k': [0.673955, 0.539164, 0.431331], 'p_i': 80, 'u_i': 3.8897},
    ]
    B_BUDGET = 143.520006
    return processors, tasks, B_BUDGET
