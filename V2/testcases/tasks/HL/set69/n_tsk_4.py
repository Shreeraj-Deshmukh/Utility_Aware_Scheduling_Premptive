"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.281523, 'e_o_k': [0.173682, 0.138946, 0.111156, 0.088925, 0.071140, 0.056912], 'p_i': 10, 'u_i': 1.7448},
        {'id': 1, 'e_m': 4.014414, 'e_o_k': [0.597099, 0.477679, 0.382143, 0.305715, 0.244572], 'p_i': 20, 'u_i': 2.9486},
        {'id': 2, 'e_m': 17.639969, 'e_o_k': [2.623746, 2.098997, 1.679197, 1.343358, 1.074686], 'p_i': 40, 'u_i': 1.5908},
        {'id': 3, 'e_m': 2.410225, 'e_o_k': [0.358494, 0.286795, 0.229436, 0.183549, 0.146839], 'p_i': 80, 'u_i': 1.2188},
    ]
    B_BUDGET = 110.400005
    return processors, tasks, B_BUDGET
