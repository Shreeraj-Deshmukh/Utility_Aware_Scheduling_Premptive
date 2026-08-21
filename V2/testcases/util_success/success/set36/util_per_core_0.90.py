"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279994, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279994, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.297977, 'e_o_k': [0.036637, 0.029309, 0.023447], 'p_i': 10, 'u_i': 3.6720},
        {'id': 1, 'e_m': 8.961220, 'e_o_k': [0.910693, 0.728554, 0.582844, 0.466275], 'p_i': 20, 'u_i': 3.1242},
        {'id': 2, 'e_m': 10.027746, 'e_o_k': [0.894908, 0.715927, 0.572741, 0.458193, 0.366554], 'p_i': 40, 'u_i': 4.4132},
        {'id': 3, 'e_m': 6.373149, 'e_o_k': [0.568760, 0.455008, 0.364007, 0.291205, 0.232964], 'p_i': 80, 'u_i': 1.8696},
        {'id': 4, 'e_m': 3.091648, 'e_o_k': [0.314192, 0.251354, 0.201083, 0.160866], 'p_i': 20, 'u_i': 4.5901},
        {'id': 5, 'e_m': 16.764213, 'e_o_k': [1.496092, 1.196874, 0.957499, 0.765999, 0.612799], 'p_i': 40, 'u_i': 2.7327},
        {'id': 6, 'e_m': 0.701888, 'e_o_k': [0.116981, 0.093585], 'p_i': 10, 'u_i': 2.2872},
        {'id': 7, 'e_m': 3.479068, 'e_o_k': [0.427754, 0.342203, 0.273763], 'p_i': 10, 'u_i': 3.8626},
    ]
    B_BUDGET = 215.279994
    return processors, tasks, B_BUDGET
