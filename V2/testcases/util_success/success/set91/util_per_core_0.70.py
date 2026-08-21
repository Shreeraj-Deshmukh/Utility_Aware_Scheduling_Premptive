"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440005, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440005, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.956465, 'e_o_k': [0.117598, 0.094079, 0.075263], 'p_i': 10, 'u_i': 1.0994},
        {'id': 1, 'e_m': 1.531405, 'e_o_k': [0.124529, 0.099623, 0.079698, 0.063759, 0.051007, 0.040806], 'p_i': 20, 'u_i': 4.8716},
        {'id': 2, 'e_m': 13.830963, 'e_o_k': [1.124688, 0.899750, 0.719800, 0.575840, 0.460672, 0.368538], 'p_i': 40, 'u_i': 3.1304},
        {'id': 3, 'e_m': 3.427408, 'e_o_k': [0.348314, 0.278651, 0.222921, 0.178337], 'p_i': 80, 'u_i': 4.2274},
        {'id': 4, 'e_m': 13.212122, 'e_o_k': [1.074366, 0.859493, 0.687594, 0.550075, 0.440060, 0.352048], 'p_i': 40, 'u_i': 1.7494},
        {'id': 5, 'e_m': 1.365799, 'e_o_k': [0.138801, 0.111041, 0.088832, 0.071066], 'p_i': 10, 'u_i': 4.2042},
        {'id': 6, 'e_m': 14.600428, 'e_o_k': [1.795135, 1.436108, 1.148886], 'p_i': 80, 'u_i': 1.0373},
        {'id': 7, 'e_m': 7.591130, 'e_o_k': [1.265188, 1.012151], 'p_i': 40, 'u_i': 1.4059},
    ]
    B_BUDGET = 167.440005
    return processors, tasks, B_BUDGET
