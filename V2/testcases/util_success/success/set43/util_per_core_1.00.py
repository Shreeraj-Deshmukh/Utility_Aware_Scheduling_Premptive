"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199993, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199993, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.686108, 'e_o_k': [0.476230, 0.380984, 0.304788, 0.243830], 'p_i': 10, 'u_i': 1.5329},
        {'id': 1, 'e_m': 5.163803, 'e_o_k': [0.460834, 0.368668, 0.294934, 0.235947, 0.188758], 'p_i': 20, 'u_i': 2.8452},
        {'id': 2, 'e_m': 9.125118, 'e_o_k': [0.742024, 0.593619, 0.474896, 0.379916, 0.303933, 0.243147], 'p_i': 40, 'u_i': 4.8964},
        {'id': 3, 'e_m': 8.862661, 'e_o_k': [0.790932, 0.632746, 0.506197, 0.404957, 0.323966], 'p_i': 80, 'u_i': 4.1648},
        {'id': 4, 'e_m': 9.757157, 'e_o_k': [0.870760, 0.696608, 0.557286, 0.445829, 0.356663], 'p_i': 20, 'u_i': 1.8911},
        {'id': 5, 'e_m': 33.206277, 'e_o_k': [5.534380, 4.427504], 'p_i': 80, 'u_i': 2.2726},
        {'id': 6, 'e_m': 1.036604, 'e_o_k': [0.084293, 0.067435, 0.053948, 0.043158, 0.034527, 0.027621], 'p_i': 40, 'u_i': 2.2097},
        {'id': 7, 'e_m': 0.108728, 'e_o_k': [0.011050, 0.008840, 0.007072, 0.005657], 'p_i': 20, 'u_i': 4.6698},
    ]
    B_BUDGET = 239.199993
    return processors, tasks, B_BUDGET
