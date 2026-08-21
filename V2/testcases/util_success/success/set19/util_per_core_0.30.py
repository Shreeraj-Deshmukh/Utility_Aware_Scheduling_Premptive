"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759994, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759994, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.294565, 'e_o_k': [0.233188, 0.186550, 0.149240, 0.119392], 'p_i': 10, 'u_i': 1.9017},
        {'id': 1, 'e_m': 1.678518, 'e_o_k': [0.279753, 0.223802], 'p_i': 20, 'u_i': 4.1004},
        {'id': 2, 'e_m': 0.562978, 'e_o_k': [0.057213, 0.045771, 0.036616, 0.029293], 'p_i': 40, 'u_i': 2.6358},
        {'id': 3, 'e_m': 3.979876, 'e_o_k': [0.489329, 0.391463, 0.313171], 'p_i': 80, 'u_i': 4.3577},
        {'id': 4, 'e_m': 0.041944, 'e_o_k': [0.004263, 0.003410, 0.002728, 0.002182], 'p_i': 40, 'u_i': 4.2383},
        {'id': 5, 'e_m': 0.068257, 'e_o_k': [0.006091, 0.004873, 0.003899, 0.003119, 0.002495], 'p_i': 80, 'u_i': 1.1754},
        {'id': 6, 'e_m': 13.639264, 'e_o_k': [2.273211, 1.818569], 'p_i': 80, 'u_i': 2.9766},
        {'id': 7, 'e_m': 2.016081, 'e_o_k': [0.163941, 0.131153, 0.104922, 0.083938, 0.067150, 0.053720], 'p_i': 40, 'u_i': 4.8798},
    ]
    B_BUDGET = 71.759994
    return processors, tasks, B_BUDGET
