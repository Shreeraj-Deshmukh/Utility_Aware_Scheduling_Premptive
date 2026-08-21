"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279994, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279994, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.977167, 'e_o_k': [0.404727, 0.323781, 0.259025, 0.207220, 0.165776, 0.132621], 'p_i': 10, 'u_i': 4.6267},
        {'id': 1, 'e_m': 4.724209, 'e_o_k': [0.787368, 0.629894], 'p_i': 20, 'u_i': 4.4310},
        {'id': 2, 'e_m': 0.574879, 'e_o_k': [0.051304, 0.041043, 0.032835, 0.026268, 0.021014], 'p_i': 40, 'u_i': 4.5357},
        {'id': 3, 'e_m': 13.864979, 'e_o_k': [1.127454, 0.901963, 0.721571, 0.577256, 0.461805, 0.369444], 'p_i': 80, 'u_i': 2.3203},
        {'id': 4, 'e_m': 7.328824, 'e_o_k': [0.901085, 0.720868, 0.576694], 'p_i': 80, 'u_i': 3.8723},
        {'id': 5, 'e_m': 4.033575, 'e_o_k': [0.409916, 0.327933, 0.262346, 0.209877], 'p_i': 40, 'u_i': 1.1816},
        {'id': 6, 'e_m': 32.844176, 'e_o_k': [2.670779, 2.136623, 1.709299, 1.367439, 1.093951, 0.875161], 'p_i': 80, 'u_i': 4.5942},
        {'id': 7, 'e_m': 2.753868, 'e_o_k': [0.245764, 0.196611, 0.157289, 0.125831, 0.100665], 'p_i': 10, 'u_i': 3.3631},
    ]
    B_BUDGET = 215.279994
    return processors, tasks, B_BUDGET
