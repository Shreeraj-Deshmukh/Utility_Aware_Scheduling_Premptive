"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199987, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199987, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.252893, 'e_o_k': [0.051822, 0.041458, 0.033166], 'p_i': 10, 'u_i': 2.8589},
        {'id': 1, 'e_m': 0.097609, 'e_o_k': [0.020002, 0.016002, 0.012801], 'p_i': 20, 'u_i': 2.7598},
        {'id': 2, 'e_m': 5.092114, 'e_o_k': [1.043466, 0.834773, 0.667818], 'p_i': 40, 'u_i': 2.0735},
        {'id': 3, 'e_m': 3.280589, 'e_o_k': [0.672252, 0.537802, 0.430241], 'p_i': 80, 'u_i': 1.1592},
        {'id': 4, 'e_m': 2.269701, 'e_o_k': [0.465103, 0.372082, 0.297666], 'p_i': 20, 'u_i': 2.2796},
        {'id': 5, 'e_m': 3.382746, 'e_o_k': [0.693186, 0.554548, 0.443639], 'p_i': 80, 'u_i': 4.8637},
        {'id': 6, 'e_m': 0.542314, 'e_o_k': [0.111130, 0.088904, 0.071123], 'p_i': 20, 'u_i': 2.9768},
        {'id': 7, 'e_m': 0.186349, 'e_o_k': [0.038186, 0.030549, 0.024439], 'p_i': 10, 'u_i': 1.8410},
    ]
    B_BUDGET = 55.199987
    return processors, tasks, B_BUDGET
