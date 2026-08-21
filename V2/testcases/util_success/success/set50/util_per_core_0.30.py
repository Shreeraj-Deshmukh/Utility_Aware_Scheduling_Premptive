"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759995, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759995, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.896733, 'e_o_k': [0.072919, 0.058335, 0.046668, 0.037335, 0.029868, 0.023894], 'p_i': 10, 'u_i': 2.5141},
        {'id': 1, 'e_m': 0.805992, 'e_o_k': [0.134332, 0.107466], 'p_i': 20, 'u_i': 3.5906},
        {'id': 2, 'e_m': 2.780652, 'e_o_k': [0.226113, 0.180891, 0.144713, 0.115770, 0.092616, 0.074093], 'p_i': 40, 'u_i': 2.8954},
        {'id': 3, 'e_m': 7.448026, 'e_o_k': [0.664686, 0.531749, 0.425399, 0.340319, 0.272255], 'p_i': 80, 'u_i': 2.6615},
        {'id': 4, 'e_m': 0.188786, 'e_o_k': [0.019186, 0.015348, 0.012279, 0.009823], 'p_i': 10, 'u_i': 4.2574},
        {'id': 5, 'e_m': 1.480480, 'e_o_k': [0.150455, 0.120364, 0.096291, 0.077033], 'p_i': 80, 'u_i': 4.9741},
        {'id': 6, 'e_m': 17.905579, 'e_o_k': [2.201506, 1.761204, 1.408964], 'p_i': 80, 'u_i': 2.2740},
        {'id': 7, 'e_m': 1.848245, 'e_o_k': [0.164943, 0.131955, 0.105564, 0.084451, 0.067561], 'p_i': 40, 'u_i': 2.9164},
    ]
    B_BUDGET = 71.759995
    return processors, tasks, B_BUDGET
