"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280017, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280017, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.440025, 'e_o_k': [0.406671, 0.325337], 'p_i': 10, 'u_i': 2.4344},
        {'id': 1, 'e_m': 7.505637, 'e_o_k': [0.669827, 0.535862, 0.428689, 0.342952, 0.274361], 'p_i': 20, 'u_i': 4.3497},
        {'id': 2, 'e_m': 8.304479, 'e_o_k': [1.384080, 1.107264], 'p_i': 40, 'u_i': 1.9085},
        {'id': 3, 'e_m': 31.114151, 'e_o_k': [2.530099, 2.024080, 1.619264, 1.295411, 1.036329, 0.829063], 'p_i': 80, 'u_i': 4.5985},
        {'id': 4, 'e_m': 1.656726, 'e_o_k': [0.203696, 0.162957, 0.130365], 'p_i': 10, 'u_i': 1.1568},
        {'id': 5, 'e_m': 0.272084, 'e_o_k': [0.027651, 0.022121, 0.017697, 0.014157], 'p_i': 40, 'u_i': 3.3218},
        {'id': 6, 'e_m': 16.037370, 'e_o_k': [1.304106, 1.043285, 0.834628, 0.667702, 0.534162, 0.427329], 'p_i': 40, 'u_i': 3.9399},
        {'id': 7, 'e_m': 0.430715, 'e_o_k': [0.071786, 0.057429], 'p_i': 40, 'u_i': 2.8364},
    ]
    B_BUDGET = 215.280017
    return processors, tasks, B_BUDGET
