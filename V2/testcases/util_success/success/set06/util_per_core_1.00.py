"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200002, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200002, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.605305, 'e_o_k': [0.321749, 0.257399, 0.205919, 0.164736, 0.131788], 'p_i': 10, 'u_i': 1.0447},
        {'id': 1, 'e_m': 5.754688, 'e_o_k': [0.584826, 0.467861, 0.374289, 0.299431], 'p_i': 20, 'u_i': 4.8543},
        {'id': 2, 'e_m': 8.886177, 'e_o_k': [0.722594, 0.578075, 0.462460, 0.369968, 0.295975, 0.236780], 'p_i': 40, 'u_i': 3.5208},
        {'id': 3, 'e_m': 32.154592, 'e_o_k': [3.953433, 3.162747, 2.530197], 'p_i': 80, 'u_i': 2.2132},
        {'id': 4, 'e_m': 1.968339, 'e_o_k': [0.242009, 0.193607, 0.154886], 'p_i': 10, 'u_i': 1.3402},
        {'id': 5, 'e_m': 5.463490, 'e_o_k': [0.910582, 0.728465], 'p_i': 80, 'u_i': 1.7290},
        {'id': 6, 'e_m': 3.596899, 'e_o_k': [0.599483, 0.479586], 'p_i': 10, 'u_i': 2.1135},
        {'id': 7, 'e_m': 4.113237, 'e_o_k': [0.685540, 0.548432], 'p_i': 40, 'u_i': 1.2097},
    ]
    B_BUDGET = 239.200002
    return processors, tasks, B_BUDGET
