"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199978, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199978, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.147701, 'e_o_k': [0.255961, 0.204768, 0.163815, 0.131052, 0.104841, 0.083873], 'p_i': 10, 'u_i': 4.1820},
        {'id': 1, 'e_m': 9.776630, 'e_o_k': [1.629438, 1.303551], 'p_i': 20, 'u_i': 2.8729},
        {'id': 2, 'e_m': 1.388336, 'e_o_k': [0.170697, 0.136558, 0.109246], 'p_i': 40, 'u_i': 4.4646},
        {'id': 3, 'e_m': 12.793403, 'e_o_k': [2.132234, 1.705787], 'p_i': 80, 'u_i': 2.8456},
        {'id': 4, 'e_m': 2.077431, 'e_o_k': [0.211121, 0.168897, 0.135117, 0.108094], 'p_i': 10, 'u_i': 4.6357},
        {'id': 5, 'e_m': 34.993710, 'e_o_k': [5.832285, 4.665828], 'p_i': 80, 'u_i': 3.1275},
        {'id': 6, 'e_m': 3.317714, 'e_o_k': [0.337166, 0.269733, 0.215786, 0.172629], 'p_i': 10, 'u_i': 2.7677},
        {'id': 7, 'e_m': 0.248365, 'e_o_k': [0.025240, 0.020192, 0.016154, 0.012923], 'p_i': 10, 'u_i': 2.2237},
    ]
    B_BUDGET = 239.199978
    return processors, tasks, B_BUDGET
