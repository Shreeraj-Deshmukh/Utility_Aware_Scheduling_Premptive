"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599994, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599994, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.171534, 'e_o_k': [0.361922, 0.289538], 'p_i': 10, 'u_i': 1.8132},
        {'id': 1, 'e_m': 1.767580, 'e_o_k': [0.143734, 0.114987, 0.091990, 0.073592, 0.058873, 0.047099], 'p_i': 20, 'u_i': 1.3118},
        {'id': 2, 'e_m': 11.118702, 'e_o_k': [0.992269, 0.793815, 0.635052, 0.508042, 0.406433], 'p_i': 40, 'u_i': 1.6432},
        {'id': 3, 'e_m': 4.990401, 'e_o_k': [0.831733, 0.665387], 'p_i': 80, 'u_i': 3.2827},
        {'id': 4, 'e_m': 0.195027, 'e_o_k': [0.017405, 0.013924, 0.011139, 0.008911, 0.007129], 'p_i': 20, 'u_i': 1.0597},
        {'id': 5, 'e_m': 0.440222, 'e_o_k': [0.054126, 0.043301, 0.034640], 'p_i': 20, 'u_i': 4.4596},
        {'id': 6, 'e_m': 6.408860, 'e_o_k': [0.651307, 0.521046, 0.416836, 0.333469], 'p_i': 40, 'u_i': 4.8824},
        {'id': 7, 'e_m': 1.621360, 'e_o_k': [0.199348, 0.159478, 0.127582], 'p_i': 10, 'u_i': 1.5609},
    ]
    B_BUDGET = 119.599994
    return processors, tasks, B_BUDGET
