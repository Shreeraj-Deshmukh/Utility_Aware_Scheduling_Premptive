"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520002, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520002, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.215004, 'e_o_k': [0.286917, 0.229534, 0.183627, 0.146902, 0.117521], 'p_i': 10, 'u_i': 1.5090},
        {'id': 1, 'e_m': 2.120931, 'e_o_k': [0.172467, 0.137974, 0.110379, 0.088303, 0.070643, 0.056514], 'p_i': 20, 'u_i': 3.9781},
        {'id': 2, 'e_m': 5.104306, 'e_o_k': [0.627579, 0.502063, 0.401650], 'p_i': 40, 'u_i': 2.6834},
        {'id': 3, 'e_m': 18.001970, 'e_o_k': [3.000328, 2.400263], 'p_i': 80, 'u_i': 1.3712},
        {'id': 4, 'e_m': 1.332224, 'e_o_k': [0.118892, 0.095114, 0.076091, 0.060873, 0.048698], 'p_i': 40, 'u_i': 4.1249},
        {'id': 5, 'e_m': 3.472066, 'e_o_k': [0.282337, 0.225870, 0.180696, 0.144556, 0.115645, 0.092516], 'p_i': 40, 'u_i': 1.3639},
        {'id': 6, 'e_m': 15.235203, 'e_o_k': [1.359639, 1.087711, 0.870169, 0.696135, 0.556908], 'p_i': 80, 'u_i': 1.0001},
        {'id': 7, 'e_m': 1.092735, 'e_o_k': [0.097519, 0.078015, 0.062412, 0.049930, 0.039944], 'p_i': 10, 'u_i': 1.8994},
    ]
    B_BUDGET = 143.520002
    return processors, tasks, B_BUDGET
