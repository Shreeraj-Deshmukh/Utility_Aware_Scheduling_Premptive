"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.44, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.44, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.084200, 'e_o_k': [0.008557, 0.006846, 0.005476, 0.004381], 'p_i': 10, 'u_i': 2.9445},
        {'id': 1, 'e_m': 3.257485, 'e_o_k': [0.400510, 0.320408, 0.256327], 'p_i': 20, 'u_i': 2.0531},
        {'id': 2, 'e_m': 7.298100, 'e_o_k': [0.741677, 0.593341, 0.474673, 0.379739], 'p_i': 40, 'u_i': 4.9994},
        {'id': 3, 'e_m': 5.375144, 'e_o_k': [0.660878, 0.528703, 0.422962], 'p_i': 80, 'u_i': 2.8114},
        {'id': 4, 'e_m': 1.295622, 'e_o_k': [0.131669, 0.105335, 0.084268, 0.067414], 'p_i': 20, 'u_i': 1.2657},
        {'id': 5, 'e_m': 15.954255, 'e_o_k': [1.297347, 1.037878, 0.830302, 0.664242, 0.531393, 0.425115], 'p_i': 40, 'u_i': 2.4168},
        {'id': 6, 'e_m': 7.175650, 'e_o_k': [0.729233, 0.583386, 0.466709, 0.373367], 'p_i': 80, 'u_i': 4.0307},
        {'id': 7, 'e_m': 34.058471, 'e_o_k': [5.676412, 4.541129], 'p_i': 80, 'u_i': 2.3502},
    ]
    B_BUDGET = 167.440000
    return processors, tasks, B_BUDGET
