"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360002, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360002, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.764066, 'e_o_k': [0.127344, 0.101876], 'p_i': 10, 'u_i': 4.7638},
        {'id': 1, 'e_m': 9.536026, 'e_o_k': [1.172462, 0.937970, 0.750376], 'p_i': 20, 'u_i': 2.7803},
        {'id': 2, 'e_m': 5.742435, 'e_o_k': [0.466956, 0.373565, 0.298852, 0.239081, 0.191265, 0.153012], 'p_i': 40, 'u_i': 3.4160},
        {'id': 3, 'e_m': 24.892448, 'e_o_k': [3.060547, 2.448438, 1.958750], 'p_i': 80, 'u_i': 3.4712},
        {'id': 4, 'e_m': 0.080920, 'e_o_k': [0.007222, 0.005777, 0.004622, 0.003697, 0.002958], 'p_i': 80, 'u_i': 4.3322},
        {'id': 5, 'e_m': 4.633982, 'e_o_k': [0.376820, 0.301456, 0.241165, 0.192932, 0.154345, 0.123476], 'p_i': 40, 'u_i': 1.9854},
        {'id': 6, 'e_m': 0.524868, 'e_o_k': [0.046841, 0.037473, 0.029978, 0.023983, 0.019186], 'p_i': 80, 'u_i': 1.7012},
        {'id': 7, 'e_m': 18.746148, 'e_o_k': [1.672967, 1.338373, 1.070699, 0.856559, 0.685247], 'p_i': 40, 'u_i': 3.3792},
    ]
    B_BUDGET = 191.360002
    return processors, tasks, B_BUDGET
