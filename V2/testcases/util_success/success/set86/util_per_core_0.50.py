"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599993, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599993, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.777270, 'e_o_k': [0.095566, 0.076453, 0.061162], 'p_i': 10, 'u_i': 2.6742},
        {'id': 1, 'e_m': 0.353876, 'e_o_k': [0.028776, 0.023021, 0.018417, 0.014733, 0.011787, 0.009429], 'p_i': 20, 'u_i': 1.0126},
        {'id': 2, 'e_m': 0.818458, 'e_o_k': [0.073042, 0.058433, 0.046747, 0.037397, 0.029918], 'p_i': 40, 'u_i': 1.6645},
        {'id': 3, 'e_m': 18.241956, 'e_o_k': [1.627971, 1.302377, 1.041901, 0.833521, 0.666817], 'p_i': 80, 'u_i': 1.3774},
        {'id': 4, 'e_m': 4.604106, 'e_o_k': [0.767351, 0.613881], 'p_i': 40, 'u_i': 1.9412},
        {'id': 5, 'e_m': 1.071261, 'e_o_k': [0.178544, 0.142835], 'p_i': 10, 'u_i': 2.2237},
        {'id': 6, 'e_m': 2.381525, 'e_o_k': [0.292810, 0.234248, 0.187399], 'p_i': 10, 'u_i': 2.4269},
        {'id': 7, 'e_m': 15.656958, 'e_o_k': [1.591154, 1.272923, 1.018339, 0.814671], 'p_i': 80, 'u_i': 4.8879},
    ]
    B_BUDGET = 119.599993
    return processors, tasks, B_BUDGET
