"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760006, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760006, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.727972, 'e_o_k': [0.064967, 0.051973, 0.041579, 0.033263, 0.026610], 'p_i': 10, 'u_i': 1.8657},
        {'id': 1, 'e_m': 2.192258, 'e_o_k': [0.195644, 0.156515, 0.125212, 0.100170, 0.080136], 'p_i': 20, 'u_i': 1.6547},
        {'id': 2, 'e_m': 0.832428, 'e_o_k': [0.084596, 0.067677, 0.054142, 0.043313], 'p_i': 40, 'u_i': 3.2690},
        {'id': 3, 'e_m': 2.736459, 'e_o_k': [0.336450, 0.269160, 0.215328], 'p_i': 80, 'u_i': 2.0883},
        {'id': 4, 'e_m': 0.776337, 'e_o_k': [0.095451, 0.076361, 0.061089], 'p_i': 10, 'u_i': 2.4453},
        {'id': 5, 'e_m': 7.593914, 'e_o_k': [0.677705, 0.542164, 0.433731, 0.346985, 0.277588], 'p_i': 40, 'u_i': 4.4841},
        {'id': 6, 'e_m': 3.668911, 'e_o_k': [0.451096, 0.360877, 0.288701], 'p_i': 40, 'u_i': 2.2759},
        {'id': 7, 'e_m': 0.269535, 'e_o_k': [0.044923, 0.035938], 'p_i': 80, 'u_i': 4.2544},
    ]
    B_BUDGET = 71.760006
    return processors, tasks, B_BUDGET
