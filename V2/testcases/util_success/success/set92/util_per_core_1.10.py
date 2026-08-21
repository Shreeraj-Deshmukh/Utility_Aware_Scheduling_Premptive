"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120003, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120003, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.571970, 'e_o_k': [0.408017, 0.326414, 0.261131, 0.208905, 0.167124], 'p_i': 10, 'u_i': 2.3069},
        {'id': 1, 'e_m': 4.969666, 'e_o_k': [0.611025, 0.488820, 0.391056], 'p_i': 20, 'u_i': 2.1947},
        {'id': 2, 'e_m': 6.324985, 'e_o_k': [0.514327, 0.411461, 0.329169, 0.263335, 0.210668, 0.168535], 'p_i': 40, 'u_i': 1.8344},
        {'id': 3, 'e_m': 18.271229, 'e_o_k': [2.246463, 1.797170, 1.437736], 'p_i': 80, 'u_i': 1.0892},
        {'id': 4, 'e_m': 4.863071, 'e_o_k': [0.494214, 0.395372, 0.316297, 0.253038], 'p_i': 10, 'u_i': 2.9584},
        {'id': 5, 'e_m': 6.717632, 'e_o_k': [1.119605, 0.895684], 'p_i': 20, 'u_i': 2.1824},
        {'id': 6, 'e_m': 12.123120, 'e_o_k': [1.490547, 1.192438, 0.953950], 'p_i': 80, 'u_i': 3.4413},
        {'id': 7, 'e_m': 5.363082, 'e_o_k': [0.893847, 0.715078], 'p_i': 40, 'u_i': 4.6080},
    ]
    B_BUDGET = 263.120003
    return processors, tasks, B_BUDGET
