"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200001, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200001, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.085592, 'e_o_k': [0.347599, 0.278079], 'p_i': 10, 'u_i': 4.4926},
        {'id': 1, 'e_m': 5.157373, 'e_o_k': [0.634103, 0.507283, 0.405826], 'p_i': 20, 'u_i': 3.2922},
        {'id': 2, 'e_m': 5.423196, 'e_o_k': [0.903866, 0.723093], 'p_i': 40, 'u_i': 3.7450},
        {'id': 3, 'e_m': 32.567464, 'e_o_k': [3.309702, 2.647761, 2.118209, 1.694567], 'p_i': 80, 'u_i': 4.8771},
        {'id': 4, 'e_m': 0.703765, 'e_o_k': [0.117294, 0.093835], 'p_i': 20, 'u_i': 4.0203},
        {'id': 5, 'e_m': 3.029295, 'e_o_k': [0.307855, 0.246284, 0.197027, 0.157622], 'p_i': 10, 'u_i': 3.4418},
        {'id': 6, 'e_m': 2.962369, 'e_o_k': [0.364226, 0.291381, 0.233104], 'p_i': 10, 'u_i': 4.8003},
        {'id': 7, 'e_m': 3.565444, 'e_o_k': [0.438374, 0.350699, 0.280559], 'p_i': 10, 'u_i': 3.9154},
    ]
    B_BUDGET = 239.200001
    return processors, tasks, B_BUDGET
