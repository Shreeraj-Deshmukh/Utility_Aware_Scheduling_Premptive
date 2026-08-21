"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760003, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760003, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.533701, 'e_o_k': [0.088950, 0.071160], 'p_i': 10, 'u_i': 2.6844},
        {'id': 1, 'e_m': 1.467029, 'e_o_k': [0.119294, 0.095435, 0.076348, 0.061078, 0.048863, 0.039090], 'p_i': 20, 'u_i': 3.2251},
        {'id': 2, 'e_m': 4.934181, 'e_o_k': [0.606662, 0.485329, 0.388263], 'p_i': 40, 'u_i': 4.0273},
        {'id': 3, 'e_m': 11.173734, 'e_o_k': [1.373820, 1.099056, 0.879245], 'p_i': 80, 'u_i': 2.2476},
        {'id': 4, 'e_m': 3.614327, 'e_o_k': [0.367310, 0.293848, 0.235078, 0.188063], 'p_i': 80, 'u_i': 1.3199},
        {'id': 5, 'e_m': 0.344577, 'e_o_k': [0.028020, 0.022416, 0.017933, 0.014346, 0.011477, 0.009182], 'p_i': 10, 'u_i': 4.7520},
        {'id': 6, 'e_m': 0.989747, 'e_o_k': [0.088328, 0.070663, 0.056530, 0.045224, 0.036179], 'p_i': 20, 'u_i': 3.4892},
        {'id': 7, 'e_m': 1.622562, 'e_o_k': [0.270427, 0.216342], 'p_i': 20, 'u_i': 1.4050},
    ]
    B_BUDGET = 71.760003
    return processors, tasks, B_BUDGET
