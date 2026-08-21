"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119985, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119985, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.426904, 'e_o_k': [0.034714, 0.027772, 0.022217, 0.017774, 0.014219, 0.011375], 'p_i': 10, 'u_i': 3.4968},
        {'id': 1, 'e_m': 3.377029, 'e_o_k': [0.343194, 0.274555, 0.219644, 0.175715], 'p_i': 20, 'u_i': 4.4050},
        {'id': 2, 'e_m': 18.635952, 'e_o_k': [1.893898, 1.515118, 1.212094, 0.969676], 'p_i': 40, 'u_i': 1.9931},
        {'id': 3, 'e_m': 20.883578, 'e_o_k': [1.863718, 1.490974, 1.192779, 0.954223, 0.763379], 'p_i': 80, 'u_i': 2.2077},
        {'id': 4, 'e_m': 3.118090, 'e_o_k': [0.519682, 0.415745], 'p_i': 10, 'u_i': 1.4923},
        {'id': 5, 'e_m': 28.721666, 'e_o_k': [3.531352, 2.825082, 2.260066], 'p_i': 80, 'u_i': 2.4692},
        {'id': 6, 'e_m': 10.356111, 'e_o_k': [1.726018, 1.380815], 'p_i': 40, 'u_i': 2.0347},
        {'id': 7, 'e_m': 13.271278, 'e_o_k': [1.631714, 1.305372, 1.044297], 'p_i': 40, 'u_i': 1.9937},
    ]
    B_BUDGET = 263.119985
    return processors, tasks, B_BUDGET
