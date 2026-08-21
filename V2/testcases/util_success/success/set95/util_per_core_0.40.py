"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679993, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679993, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.583822, 'e_o_k': [0.160957, 0.128766, 0.103013, 0.082410], 'p_i': 10, 'u_i': 1.9313},
        {'id': 1, 'e_m': 2.910187, 'e_o_k': [0.485031, 0.388025], 'p_i': 20, 'u_i': 4.0147},
        {'id': 2, 'e_m': 6.823232, 'e_o_k': [0.554843, 0.443874, 0.355099, 0.284079, 0.227264, 0.181811], 'p_i': 40, 'u_i': 3.8759},
        {'id': 3, 'e_m': 3.019671, 'e_o_k': [0.371271, 0.297017, 0.237613], 'p_i': 80, 'u_i': 4.3076},
        {'id': 4, 'e_m': 3.916411, 'e_o_k': [0.318470, 0.254776, 0.203820, 0.163056, 0.130445, 0.104356], 'p_i': 80, 'u_i': 1.9116},
        {'id': 5, 'e_m': 2.706466, 'e_o_k': [0.332762, 0.266210, 0.212968], 'p_i': 40, 'u_i': 2.7475},
        {'id': 6, 'e_m': 8.231295, 'e_o_k': [0.734587, 0.587670, 0.470136, 0.376109, 0.300887], 'p_i': 80, 'u_i': 2.9584},
        {'id': 7, 'e_m': 1.365476, 'e_o_k': [0.138768, 0.111014, 0.088811, 0.071049], 'p_i': 20, 'u_i': 3.8181},
    ]
    B_BUDGET = 95.679993
    return processors, tasks, B_BUDGET
