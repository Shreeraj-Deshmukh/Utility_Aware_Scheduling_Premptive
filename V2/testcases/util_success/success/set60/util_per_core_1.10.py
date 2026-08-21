"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120016, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120016, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.504551, 'e_o_k': [0.457780, 0.366224, 0.292979, 0.234383], 'p_i': 10, 'u_i': 1.8920},
        {'id': 1, 'e_m': 2.897249, 'e_o_k': [0.258560, 0.206848, 0.165478, 0.132383, 0.105906], 'p_i': 20, 'u_i': 4.6661},
        {'id': 2, 'e_m': 14.553134, 'e_o_k': [1.183413, 0.946730, 0.757384, 0.605907, 0.484726, 0.387781], 'p_i': 40, 'u_i': 3.8800},
        {'id': 3, 'e_m': 28.665372, 'e_o_k': [4.777562, 3.822050], 'p_i': 80, 'u_i': 3.7867},
        {'id': 4, 'e_m': 7.014903, 'e_o_k': [1.169150, 0.935320], 'p_i': 80, 'u_i': 2.4838},
        {'id': 5, 'e_m': 17.611466, 'e_o_k': [2.165344, 1.732275, 1.385820], 'p_i': 80, 'u_i': 2.1780},
        {'id': 6, 'e_m': 4.456961, 'e_o_k': [0.547987, 0.438390, 0.350712], 'p_i': 20, 'u_i': 4.2374},
        {'id': 7, 'e_m': 14.074372, 'e_o_k': [1.730456, 1.384365, 1.107492], 'p_i': 40, 'u_i': 3.3065},
    ]
    B_BUDGET = 263.120016
    return processors, tasks, B_BUDGET
