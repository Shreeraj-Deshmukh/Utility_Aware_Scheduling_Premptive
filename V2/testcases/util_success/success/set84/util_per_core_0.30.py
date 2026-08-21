"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759993, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759993, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.363723, 'e_o_k': [0.032460, 0.025968, 0.020774, 0.016619, 0.013296], 'p_i': 10, 'u_i': 1.7042},
        {'id': 1, 'e_m': 0.552480, 'e_o_k': [0.067928, 0.054342, 0.043474], 'p_i': 20, 'u_i': 4.3788},
        {'id': 2, 'e_m': 3.425711, 'e_o_k': [0.348141, 0.278513, 0.222810, 0.178248], 'p_i': 40, 'u_i': 3.2500},
        {'id': 3, 'e_m': 1.942862, 'e_o_k': [0.323810, 0.259048], 'p_i': 80, 'u_i': 3.9101},
        {'id': 4, 'e_m': 0.897270, 'e_o_k': [0.091186, 0.072949, 0.058359, 0.046687], 'p_i': 80, 'u_i': 2.7187},
        {'id': 5, 'e_m': 4.233176, 'e_o_k': [0.344228, 0.275382, 0.220306, 0.176245, 0.140996, 0.112797], 'p_i': 40, 'u_i': 3.8755},
        {'id': 6, 'e_m': 19.496915, 'e_o_k': [2.397162, 1.917729, 1.534183], 'p_i': 80, 'u_i': 3.4836},
        {'id': 7, 'e_m': 2.612736, 'e_o_k': [0.321238, 0.256990, 0.205592], 'p_i': 40, 'u_i': 4.1699},
    ]
    B_BUDGET = 71.759993
    return processors, tasks, B_BUDGET
