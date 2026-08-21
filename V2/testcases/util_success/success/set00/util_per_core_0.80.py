"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359997, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359997, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.041113, 'e_o_k': [0.496858, 0.397486, 0.317989], 'p_i': 10, 'u_i': 2.8465},
        {'id': 1, 'e_m': 1.537395, 'e_o_k': [0.137202, 0.109762, 0.087809, 0.070247, 0.056198], 'p_i': 20, 'u_i': 3.7661},
        {'id': 2, 'e_m': 8.186760, 'e_o_k': [1.006569, 0.805255, 0.644204], 'p_i': 40, 'u_i': 1.0932},
        {'id': 3, 'e_m': 11.984379, 'e_o_k': [0.974530, 0.779624, 0.623699, 0.498959, 0.399167, 0.319334], 'p_i': 80, 'u_i': 2.8740},
        {'id': 4, 'e_m': 25.216240, 'e_o_k': [3.100357, 2.480286, 1.984229], 'p_i': 80, 'u_i': 4.9324},
        {'id': 5, 'e_m': 1.651694, 'e_o_k': [0.203077, 0.162462, 0.129969], 'p_i': 20, 'u_i': 4.5939},
        {'id': 6, 'e_m': 2.832604, 'e_o_k': [0.472101, 0.377681], 'p_i': 10, 'u_i': 2.0087},
        {'id': 7, 'e_m': 6.679770, 'e_o_k': [0.678838, 0.543071, 0.434457, 0.347565], 'p_i': 80, 'u_i': 1.3714},
    ]
    B_BUDGET = 191.359997
    return processors, tasks, B_BUDGET
