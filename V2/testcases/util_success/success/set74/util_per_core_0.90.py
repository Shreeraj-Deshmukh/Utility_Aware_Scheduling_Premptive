"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.28, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.28, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.031804, 'e_o_k': [0.327853, 0.262282, 0.209826, 0.167861, 0.134289, 0.107431], 'p_i': 10, 'u_i': 2.8037},
        {'id': 1, 'e_m': 0.885752, 'e_o_k': [0.090015, 0.072012, 0.057610, 0.046088], 'p_i': 20, 'u_i': 4.7578},
        {'id': 2, 'e_m': 5.189370, 'e_o_k': [0.864895, 0.691916], 'p_i': 40, 'u_i': 1.7165},
        {'id': 3, 'e_m': 33.035371, 'e_o_k': [2.686327, 2.149061, 1.719249, 1.375399, 1.100319, 0.880256], 'p_i': 80, 'u_i': 2.0036},
        {'id': 4, 'e_m': 5.054967, 'e_o_k': [0.621512, 0.497210, 0.397768], 'p_i': 20, 'u_i': 1.4212},
        {'id': 5, 'e_m': 1.776308, 'e_o_k': [0.218399, 0.174719, 0.139775], 'p_i': 10, 'u_i': 3.1256},
        {'id': 6, 'e_m': 5.194000, 'e_o_k': [0.527846, 0.422276, 0.337821, 0.270257], 'p_i': 80, 'u_i': 1.0663},
        {'id': 7, 'e_m': 6.291028, 'e_o_k': [0.561432, 0.449145, 0.359316, 0.287453, 0.229962], 'p_i': 20, 'u_i': 3.8936},
    ]
    B_BUDGET = 215.280000
    return processors, tasks, B_BUDGET
