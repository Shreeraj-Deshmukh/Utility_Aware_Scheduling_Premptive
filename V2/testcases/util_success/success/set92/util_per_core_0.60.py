"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520008, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520008, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.838608, 'e_o_k': [0.074840, 0.059872, 0.047898, 0.038318, 0.030654], 'p_i': 10, 'u_i': 3.7403},
        {'id': 1, 'e_m': 2.422472, 'e_o_k': [0.196987, 0.157590, 0.126072, 0.100858, 0.080686, 0.064549], 'p_i': 20, 'u_i': 1.1622},
        {'id': 2, 'e_m': 9.537068, 'e_o_k': [1.172590, 0.938072, 0.750458], 'p_i': 40, 'u_i': 4.1752},
        {'id': 3, 'e_m': 23.325591, 'e_o_k': [2.370487, 1.896390, 1.517112, 1.213689], 'p_i': 80, 'u_i': 1.9420},
        {'id': 4, 'e_m': 0.005496, 'e_o_k': [0.000916, 0.000733], 'p_i': 10, 'u_i': 2.5093},
        {'id': 5, 'e_m': 5.812941, 'e_o_k': [0.714706, 0.571765, 0.457412], 'p_i': 80, 'u_i': 3.6510},
        {'id': 6, 'e_m': 1.083959, 'e_o_k': [0.110158, 0.088127, 0.070501, 0.056401], 'p_i': 10, 'u_i': 3.1983},
        {'id': 7, 'e_m': 11.336474, 'e_o_k': [1.152081, 0.921665, 0.737332, 0.589865], 'p_i': 40, 'u_i': 4.3627},
    ]
    B_BUDGET = 143.520008
    return processors, tasks, B_BUDGET
