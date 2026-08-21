"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120008, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120008, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.670016, 'e_o_k': [0.169717, 0.135774, 0.108619, 0.086895], 'p_i': 10, 'u_i': 1.7812},
        {'id': 1, 'e_m': 9.915946, 'e_o_k': [0.884931, 0.707945, 0.566356, 0.453085, 0.362468], 'p_i': 20, 'u_i': 3.4338},
        {'id': 2, 'e_m': 1.126597, 'e_o_k': [0.100541, 0.080433, 0.064346, 0.051477, 0.041182], 'p_i': 40, 'u_i': 1.4372},
        {'id': 3, 'e_m': 28.358627, 'e_o_k': [3.486716, 2.789373, 2.231499], 'p_i': 80, 'u_i': 1.0760},
        {'id': 4, 'e_m': 7.458496, 'e_o_k': [0.665620, 0.532496, 0.425997, 0.340798, 0.272638], 'p_i': 20, 'u_i': 3.9613},
        {'id': 5, 'e_m': 1.121172, 'e_o_k': [0.137849, 0.110279, 0.088223], 'p_i': 10, 'u_i': 4.3968},
        {'id': 6, 'e_m': 17.305112, 'e_o_k': [1.407194, 1.125755, 0.900604, 0.720483, 0.576387, 0.461109], 'p_i': 40, 'u_i': 1.2846},
        {'id': 7, 'e_m': 2.368836, 'e_o_k': [0.211403, 0.169122, 0.135298, 0.108238, 0.086590], 'p_i': 10, 'u_i': 3.8310},
    ]
    B_BUDGET = 263.120008
    return processors, tasks, B_BUDGET
