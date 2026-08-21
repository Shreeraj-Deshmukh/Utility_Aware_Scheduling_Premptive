"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.68001, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.68001, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.396008, 'e_o_k': [0.035341, 0.028273, 0.022618, 0.018095, 0.014476], 'p_i': 10, 'u_i': 2.2582},
        {'id': 1, 'e_m': 1.438192, 'e_o_k': [0.239699, 0.191759], 'p_i': 20, 'u_i': 2.9332},
        {'id': 2, 'e_m': 0.174158, 'e_o_k': [0.021413, 0.017130, 0.013704], 'p_i': 40, 'u_i': 1.0372},
        {'id': 3, 'e_m': 2.213172, 'e_o_k': [0.272111, 0.217689, 0.174151], 'p_i': 80, 'u_i': 1.7921},
        {'id': 4, 'e_m': 8.410664, 'e_o_k': [0.683927, 0.547142, 0.437713, 0.350171, 0.280137, 0.224109], 'p_i': 40, 'u_i': 1.1296},
        {'id': 5, 'e_m': 14.019005, 'e_o_k': [1.723648, 1.378918, 1.103135], 'p_i': 40, 'u_i': 3.7636},
        {'id': 6, 'e_m': 1.468623, 'e_o_k': [0.119424, 0.095539, 0.076431, 0.061145, 0.048916, 0.039133], 'p_i': 80, 'u_i': 2.3342},
        {'id': 7, 'e_m': 6.189722, 'e_o_k': [0.552391, 0.441913, 0.353530, 0.282824, 0.226259], 'p_i': 80, 'u_i': 1.6627},
    ]
    B_BUDGET = 95.680010
    return processors, tasks, B_BUDGET
