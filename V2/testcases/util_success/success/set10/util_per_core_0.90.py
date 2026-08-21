"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280006, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280006, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.795244, 'e_o_k': [0.064667, 0.051733, 0.041387, 0.033109, 0.026487, 0.021190], 'p_i': 10, 'u_i': 1.3055},
        {'id': 1, 'e_m': 8.001815, 'e_o_k': [0.650681, 0.520545, 0.416436, 0.333149, 0.266519, 0.213215], 'p_i': 20, 'u_i': 3.0735},
        {'id': 2, 'e_m': 1.883540, 'e_o_k': [0.191417, 0.153133, 0.122507, 0.098005], 'p_i': 40, 'u_i': 3.9862},
        {'id': 3, 'e_m': 15.786357, 'e_o_k': [1.940946, 1.552756, 1.242205], 'p_i': 80, 'u_i': 1.5757},
        {'id': 4, 'e_m': 4.378156, 'e_o_k': [0.538298, 0.430638, 0.344511], 'p_i': 20, 'u_i': 4.9941},
        {'id': 5, 'e_m': 0.113816, 'e_o_k': [0.018969, 0.015175], 'p_i': 80, 'u_i': 1.7632},
        {'id': 6, 'e_m': 29.053913, 'e_o_k': [2.592865, 2.074292, 1.659433, 1.327547, 1.062037], 'p_i': 80, 'u_i': 1.4284},
        {'id': 7, 'e_m': 19.698501, 'e_o_k': [3.283083, 2.626467], 'p_i': 40, 'u_i': 4.8320},
    ]
    B_BUDGET = 215.280006
    return processors, tasks, B_BUDGET
