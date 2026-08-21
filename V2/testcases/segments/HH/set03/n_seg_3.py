"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.759727, 'e_o_k': [0.435909, 0.348727, 0.278982], 'p_i': 10, 'u_i': 3.3255},
        {'id': 1, 'e_m': 2.267234, 'e_o_k': [1.300872, 1.040698, 0.832558], 'p_i': 20, 'u_i': 3.5739},
        {'id': 2, 'e_m': 1.540180, 'e_o_k': [0.883710, 0.706968, 0.565574], 'p_i': 40, 'u_i': 2.2786},
        {'id': 3, 'e_m': 8.351708, 'e_o_k': [4.791964, 3.833571, 3.066857], 'p_i': 80, 'u_i': 1.5604},
        {'id': 4, 'e_m': 8.673789, 'e_o_k': [4.976764, 3.981411, 3.185129], 'p_i': 80, 'u_i': 1.1253},
        {'id': 5, 'e_m': 24.118641, 'e_o_k': [13.838565, 11.070852, 8.856681], 'p_i': 80, 'u_i': 3.7966},
        {'id': 6, 'e_m': 0.384822, 'e_o_k': [0.220799, 0.176640, 0.141312], 'p_i': 10, 'u_i': 1.2428},
        {'id': 7, 'e_m': 0.775086, 'e_o_k': [0.444721, 0.355777, 0.284622], 'p_i': 40, 'u_i': 4.6455},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET
