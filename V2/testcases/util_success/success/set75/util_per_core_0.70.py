"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439991, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439991, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.779299, 'e_o_k': [0.282449, 0.225959, 0.180767, 0.144614], 'p_i': 10, 'u_i': 1.3807},
        {'id': 1, 'e_m': 9.653893, 'e_o_k': [1.186954, 0.949563, 0.759651], 'p_i': 20, 'u_i': 1.8392},
        {'id': 2, 'e_m': 4.951288, 'e_o_k': [0.608765, 0.487012, 0.389610], 'p_i': 40, 'u_i': 3.5091},
        {'id': 3, 'e_m': 3.591500, 'e_o_k': [0.598583, 0.478867], 'p_i': 80, 'u_i': 3.6327},
        {'id': 4, 'e_m': 4.204562, 'e_o_k': [0.427293, 0.341834, 0.273467, 0.218774], 'p_i': 80, 'u_i': 2.4382},
        {'id': 5, 'e_m': 8.316809, 'e_o_k': [0.676295, 0.541036, 0.432829, 0.346263, 0.277011, 0.221608], 'p_i': 40, 'u_i': 2.3485},
        {'id': 6, 'e_m': 1.766733, 'e_o_k': [0.294456, 0.235564], 'p_i': 20, 'u_i': 1.1590},
        {'id': 7, 'e_m': 2.437712, 'e_o_k': [0.406285, 0.325028], 'p_i': 20, 'u_i': 4.3960},
    ]
    B_BUDGET = 167.439991
    return processors, tasks, B_BUDGET
