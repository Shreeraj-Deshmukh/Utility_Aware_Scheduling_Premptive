"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520008, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520008, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.631496, 'e_o_k': [0.271916, 0.217533], 'p_i': 10, 'u_i': 2.8418},
        {'id': 1, 'e_m': 0.587897, 'e_o_k': [0.059746, 0.047797, 0.038237, 0.030590], 'p_i': 20, 'u_i': 1.5566},
        {'id': 2, 'e_m': 19.644216, 'e_o_k': [1.996363, 1.597091, 1.277673, 1.022138], 'p_i': 40, 'u_i': 3.2695},
        {'id': 3, 'e_m': 11.482665, 'e_o_k': [1.913778, 1.531022], 'p_i': 80, 'u_i': 3.8342},
        {'id': 4, 'e_m': 0.455735, 'e_o_k': [0.037059, 0.029647, 0.023718, 0.018974, 0.015179, 0.012143], 'p_i': 20, 'u_i': 4.3734},
        {'id': 5, 'e_m': 1.132075, 'e_o_k': [0.115048, 0.092039, 0.073631, 0.058905], 'p_i': 20, 'u_i': 3.3497},
        {'id': 6, 'e_m': 7.549726, 'e_o_k': [0.767249, 0.613799, 0.491039, 0.392831], 'p_i': 40, 'u_i': 4.2042},
        {'id': 7, 'e_m': 4.187328, 'e_o_k': [0.514835, 0.411868, 0.329495], 'p_i': 40, 'u_i': 1.0373},
    ]
    B_BUDGET = 143.520008
    return processors, tasks, B_BUDGET
