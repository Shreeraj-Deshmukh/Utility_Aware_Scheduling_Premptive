"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199985, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.199985, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.844903, 'e_o_k': [0.183229, 0.109937, 0.065962, 0.039577, 0.023746], 'p_i': 10, 'u_i': 3.8434},
        {'id': 1, 'e_m': 0.177585, 'e_o_k': [0.055495, 0.033297], 'p_i': 20, 'u_i': 3.7460},
        {'id': 2, 'e_m': 1.433543, 'e_o_k': [0.329399, 0.197639, 0.118584, 0.071150], 'p_i': 40, 'u_i': 2.3844},
        {'id': 3, 'e_m': 1.748862, 'e_o_k': [0.546519, 0.327912], 'p_i': 80, 'u_i': 3.6397},
        {'id': 4, 'e_m': 6.915032, 'e_o_k': [1.450690, 0.870414, 0.522248, 0.313349, 0.188009, 0.112806], 'p_i': 80, 'u_i': 2.0089},
        {'id': 5, 'e_m': 1.550765, 'e_o_k': [0.356334, 0.213800, 0.128280, 0.076968], 'p_i': 20, 'u_i': 4.2973},
        {'id': 6, 'e_m': 0.111141, 'e_o_k': [0.034731, 0.020839], 'p_i': 10, 'u_i': 3.5880},
        {'id': 7, 'e_m': 1.476817, 'e_o_k': [0.309818, 0.185891, 0.111535, 0.066921, 0.040152, 0.024091], 'p_i': 20, 'u_i': 4.0384},
    ]
    B_BUDGET = 55.199985
    return processors, tasks, B_BUDGET
