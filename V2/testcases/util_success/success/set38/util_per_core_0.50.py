"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599993, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599993, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.676488, 'e_o_k': [0.217643, 0.174115, 0.139292, 0.111433, 0.089147, 0.071317], 'p_i': 10, 'u_i': 1.2855},
        {'id': 1, 'e_m': 2.989805, 'e_o_k': [0.243121, 0.194497, 0.155597, 0.124478, 0.099582, 0.079666], 'p_i': 20, 'u_i': 4.6522},
        {'id': 2, 'e_m': 7.948135, 'e_o_k': [0.709317, 0.567454, 0.453963, 0.363170, 0.290536], 'p_i': 40, 'u_i': 4.9928},
        {'id': 3, 'e_m': 5.025623, 'e_o_k': [0.448503, 0.358802, 0.287042, 0.229633, 0.183707], 'p_i': 80, 'u_i': 3.9733},
        {'id': 4, 'e_m': 0.736268, 'e_o_k': [0.074824, 0.059859, 0.047887, 0.038310], 'p_i': 10, 'u_i': 1.2745},
        {'id': 5, 'e_m': 3.125212, 'e_o_k': [0.254132, 0.203305, 0.162644, 0.130116, 0.104092, 0.083274], 'p_i': 40, 'u_i': 2.7525},
        {'id': 6, 'e_m': 5.775942, 'e_o_k': [0.710157, 0.568125, 0.454500], 'p_i': 40, 'u_i': 3.5893},
        {'id': 7, 'e_m': 0.251816, 'e_o_k': [0.030961, 0.024769, 0.019815], 'p_i': 10, 'u_i': 2.8023},
    ]
    B_BUDGET = 119.599993
    return processors, tasks, B_BUDGET
