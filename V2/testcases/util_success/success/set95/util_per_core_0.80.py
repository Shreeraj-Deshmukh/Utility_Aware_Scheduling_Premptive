"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360005, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360005, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.167644, 'e_o_k': [0.321915, 0.257532, 0.206026, 0.164820], 'p_i': 10, 'u_i': 1.9313},
        {'id': 1, 'e_m': 5.820375, 'e_o_k': [0.970062, 0.776050], 'p_i': 20, 'u_i': 4.0147},
        {'id': 2, 'e_m': 13.646463, 'e_o_k': [1.109685, 0.887748, 0.710198, 0.568159, 0.454527, 0.363622], 'p_i': 40, 'u_i': 3.8759},
        {'id': 3, 'e_m': 6.039342, 'e_o_k': [0.742542, 0.594034, 0.475227], 'p_i': 80, 'u_i': 4.3076},
        {'id': 4, 'e_m': 7.832822, 'e_o_k': [0.636939, 0.509551, 0.407641, 0.326113, 0.260890, 0.208712], 'p_i': 80, 'u_i': 1.9116},
        {'id': 5, 'e_m': 5.412931, 'e_o_k': [0.665524, 0.532419, 0.425936], 'p_i': 40, 'u_i': 2.7475},
        {'id': 6, 'e_m': 16.462590, 'e_o_k': [1.469174, 1.175340, 0.940272, 0.752217, 0.601774], 'p_i': 80, 'u_i': 2.9584},
        {'id': 7, 'e_m': 2.730953, 'e_o_k': [0.277536, 0.222029, 0.177623, 0.142098], 'p_i': 20, 'u_i': 3.8181},
    ]
    B_BUDGET = 191.360005
    return processors, tasks, B_BUDGET
