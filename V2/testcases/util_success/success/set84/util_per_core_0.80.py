"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359998, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359998, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.969117, 'e_o_k': [0.119154, 0.095323, 0.076258], 'p_i': 10, 'u_i': 4.3788},
        {'id': 1, 'e_m': 1.915960, 'e_o_k': [0.194711, 0.155769, 0.124615, 0.099692], 'p_i': 20, 'u_i': 3.2500},
        {'id': 2, 'e_m': 5.516791, 'e_o_k': [0.919465, 0.735572], 'p_i': 40, 'u_i': 3.9101},
        {'id': 3, 'e_m': 4.945663, 'e_o_k': [0.502608, 0.402086, 0.321669, 0.257335], 'p_i': 80, 'u_i': 2.7187},
        {'id': 4, 'e_m': 11.619216, 'e_o_k': [0.944836, 0.755869, 0.604695, 0.483756, 0.387005, 0.309604], 'p_i': 80, 'u_i': 3.8755},
        {'id': 5, 'e_m': 19.537569, 'e_o_k': [2.402160, 1.921728, 1.537382], 'p_i': 40, 'u_i': 3.4836},
        {'id': 6, 'e_m': 22.655263, 'e_o_k': [2.785483, 2.228387, 1.782709], 'p_i': 80, 'u_i': 4.1699},
        {'id': 7, 'e_m': 5.813591, 'e_o_k': [0.590812, 0.472650, 0.378120, 0.302496], 'p_i': 20, 'u_i': 3.6851},
    ]
    B_BUDGET = 191.359998
    return processors, tasks, B_BUDGET
