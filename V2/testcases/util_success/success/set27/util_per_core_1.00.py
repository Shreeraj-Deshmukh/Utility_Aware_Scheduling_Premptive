"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199974, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199974, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.545920, 'e_o_k': [0.125709, 0.100567, 0.080454, 0.064363, 0.051490, 0.041192], 'p_i': 10, 'u_i': 1.3112},
        {'id': 1, 'e_m': 3.221267, 'e_o_k': [0.261943, 0.209554, 0.167643, 0.134115, 0.107292, 0.085833], 'p_i': 20, 'u_i': 2.1246},
        {'id': 2, 'e_m': 3.057897, 'e_o_k': [0.248658, 0.198926, 0.159141, 0.127313, 0.101850, 0.081480], 'p_i': 40, 'u_i': 2.2214},
        {'id': 3, 'e_m': 12.674924, 'e_o_k': [1.131151, 0.904921, 0.723937, 0.579149, 0.463319], 'p_i': 80, 'u_i': 3.1164},
        {'id': 4, 'e_m': 4.154157, 'e_o_k': [0.370730, 0.296584, 0.237267, 0.189814, 0.151851], 'p_i': 10, 'u_i': 2.9383},
        {'id': 5, 'e_m': 39.366136, 'e_o_k': [3.513161, 2.810529, 2.248423, 1.798738, 1.438991], 'p_i': 80, 'u_i': 2.8468},
        {'id': 6, 'e_m': 2.814039, 'e_o_k': [0.469006, 0.375205], 'p_i': 10, 'u_i': 4.6487},
        {'id': 7, 'e_m': 2.605644, 'e_o_k': [0.434274, 0.347419], 'p_i': 10, 'u_i': 3.0837},
    ]
    B_BUDGET = 239.199974
    return processors, tasks, B_BUDGET
