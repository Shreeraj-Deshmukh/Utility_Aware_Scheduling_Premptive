"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280008, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280008, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.658615, 'e_o_k': [0.203928, 0.163142, 0.130514], 'p_i': 10, 'u_i': 4.0215},
        {'id': 1, 'e_m': 8.771917, 'e_o_k': [0.782834, 0.626267, 0.501014, 0.400811, 0.320649], 'p_i': 20, 'u_i': 1.4911},
        {'id': 2, 'e_m': 9.201259, 'e_o_k': [0.935087, 0.748070, 0.598456, 0.478765], 'p_i': 40, 'u_i': 3.6858},
        {'id': 3, 'e_m': 12.332613, 'e_o_k': [1.516305, 1.213044, 0.970435], 'p_i': 80, 'u_i': 3.5601},
        {'id': 4, 'e_m': 17.514394, 'e_o_k': [1.424212, 1.139370, 0.911496, 0.729197, 0.583357, 0.466686], 'p_i': 80, 'u_i': 2.9573},
        {'id': 5, 'e_m': 4.170826, 'e_o_k': [0.695138, 0.556110], 'p_i': 40, 'u_i': 4.1230},
        {'id': 6, 'e_m': 10.029134, 'e_o_k': [0.895032, 0.716026, 0.572821, 0.458256, 0.366605], 'p_i': 40, 'u_i': 4.3496},
        {'id': 7, 'e_m': 2.374246, 'e_o_k': [0.193066, 0.154453, 0.123562, 0.098850, 0.079080, 0.063264], 'p_i': 10, 'u_i': 3.3614},
    ]
    B_BUDGET = 215.280008
    return processors, tasks, B_BUDGET
