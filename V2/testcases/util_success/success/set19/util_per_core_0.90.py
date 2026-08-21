"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280005, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280005, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.590679, 'e_o_k': [0.060028, 0.048023, 0.038418, 0.030735], 'p_i': 10, 'u_i': 4.2383},
        {'id': 1, 'e_m': 6.414139, 'e_o_k': [0.572418, 0.457935, 0.366348, 0.293078, 0.234463], 'p_i': 20, 'u_i': 1.1754},
        {'id': 2, 'e_m': 10.085104, 'e_o_k': [1.680851, 1.344681], 'p_i': 40, 'u_i': 2.9766},
        {'id': 3, 'e_m': 25.066468, 'e_o_k': [2.038322, 1.630658, 1.304526, 1.043621, 0.834897, 0.667917], 'p_i': 80, 'u_i': 4.8798},
        {'id': 4, 'e_m': 26.764049, 'e_o_k': [2.176364, 1.741091, 1.392873, 1.114298, 0.891439, 0.713151], 'p_i': 80, 'u_i': 3.7063},
        {'id': 5, 'e_m': 3.523489, 'e_o_k': [0.314448, 0.251558, 0.201246, 0.160997, 0.128798], 'p_i': 10, 'u_i': 2.9881},
        {'id': 6, 'e_m': 1.165786, 'e_o_k': [0.104039, 0.083231, 0.066585, 0.053268, 0.042614], 'p_i': 20, 'u_i': 3.8057},
        {'id': 7, 'e_m': 8.766223, 'e_o_k': [1.461037, 1.168830], 'p_i': 80, 'u_i': 1.4079},
    ]
    B_BUDGET = 215.280005
    return processors, tasks, B_BUDGET
