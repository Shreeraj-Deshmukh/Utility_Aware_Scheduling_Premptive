"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760007, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760007, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.525985, 'e_o_k': [0.046941, 0.037552, 0.030042, 0.024034, 0.019227], 'p_i': 10, 'u_i': 4.4298},
        {'id': 1, 'e_m': 5.145668, 'e_o_k': [0.632664, 0.506131, 0.404905], 'p_i': 20, 'u_i': 1.5050},
        {'id': 2, 'e_m': 0.310949, 'e_o_k': [0.051825, 0.041460], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 2.572263, 'e_o_k': [0.209168, 0.167334, 0.133867, 0.107094, 0.085675, 0.068540], 'p_i': 80, 'u_i': 4.0993},
        {'id': 4, 'e_m': 1.049143, 'e_o_k': [0.174857, 0.139886], 'p_i': 20, 'u_i': 2.5958},
        {'id': 5, 'e_m': 4.121008, 'e_o_k': [0.506681, 0.405345, 0.324276], 'p_i': 80, 'u_i': 1.3643},
        {'id': 6, 'e_m': 3.826944, 'e_o_k': [0.311194, 0.248956, 0.199164, 0.159332, 0.127465, 0.101972], 'p_i': 40, 'u_i': 1.6218},
        {'id': 7, 'e_m': 4.043822, 'e_o_k': [0.410958, 0.328766, 0.263013, 0.210410], 'p_i': 80, 'u_i': 1.2955},
    ]
    B_BUDGET = 71.760007
    return processors, tasks, B_BUDGET
