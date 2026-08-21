"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119999, "H": 80, "J": 47, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119999, "H": 80, "J": 47, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.893537, 'e_o_k': [0.315589, 0.252472], 'p_i': 10, 'u_i': 4.6424},
        {'id': 1, 'e_m': 6.951313, 'e_o_k': [0.565258, 0.452206, 0.361765, 0.289412, 0.231530, 0.185224], 'p_i': 20, 'u_i': 1.5808},
        {'id': 2, 'e_m': 13.845135, 'e_o_k': [1.407026, 1.125621, 0.900497, 0.720397], 'p_i': 40, 'u_i': 4.8715},
        {'id': 3, 'e_m': 36.042504, 'e_o_k': [6.007084, 4.805667], 'p_i': 80, 'u_i': 1.1976},
        {'id': 4, 'e_m': 3.152407, 'e_o_k': [0.387591, 0.310073, 0.248058], 'p_i': 10, 'u_i': 4.9704},
        {'id': 5, 'e_m': 1.622000, 'e_o_k': [0.270333, 0.216267], 'p_i': 10, 'u_i': 2.1180},
        {'id': 6, 'e_m': 3.853543, 'e_o_k': [0.391620, 0.313296, 0.250637, 0.200510], 'p_i': 10, 'u_i': 3.9329},
        {'id': 7, 'e_m': 0.036259, 'e_o_k': [0.002948, 0.002359, 0.001887, 0.001510, 0.001208, 0.000966], 'p_i': 10, 'u_i': 3.7608},
    ]
    B_BUDGET = 263.119999
    return processors, tasks, B_BUDGET
