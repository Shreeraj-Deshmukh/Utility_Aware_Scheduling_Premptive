"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119993, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119993, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.498032, 'e_o_k': [0.133689, 0.106951, 0.085561, 0.068449, 0.054759], 'p_i': 10, 'u_i': 1.5498},
        {'id': 1, 'e_m': 0.666253, 'e_o_k': [0.081916, 0.065533, 0.052427], 'p_i': 20, 'u_i': 3.8477},
        {'id': 2, 'e_m': 16.524906, 'e_o_k': [1.343751, 1.075000, 0.860000, 0.688000, 0.550400, 0.440320], 'p_i': 40, 'u_i': 1.9913},
        {'id': 3, 'e_m': 13.815818, 'e_o_k': [1.404047, 1.123237, 0.898590, 0.718872], 'p_i': 80, 'u_i': 4.5336},
        {'id': 4, 'e_m': 35.108000, 'e_o_k': [3.133151, 2.506521, 2.005217, 1.604173, 1.283339], 'p_i': 80, 'u_i': 3.0445},
        {'id': 5, 'e_m': 1.974867, 'e_o_k': [0.329144, 0.263316], 'p_i': 10, 'u_i': 1.0573},
        {'id': 6, 'e_m': 4.414242, 'e_o_k': [0.735707, 0.588566], 'p_i': 10, 'u_i': 1.3900},
        {'id': 7, 'e_m': 28.264227, 'e_o_k': [3.475110, 2.780088, 2.224070], 'p_i': 80, 'u_i': 1.3591},
    ]
    B_BUDGET = 263.119993
    return processors, tasks, B_BUDGET
