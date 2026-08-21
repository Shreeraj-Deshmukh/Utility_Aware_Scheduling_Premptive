"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680017, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680017, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.505787, 'e_o_k': [0.084298, 0.067438], 'p_i': 10, 'u_i': 2.8589},
        {'id': 1, 'e_m': 0.195219, 'e_o_k': [0.024002, 0.019202, 0.015361], 'p_i': 20, 'u_i': 2.7598},
        {'id': 2, 'e_m': 10.184228, 'e_o_k': [1.697371, 1.357897], 'p_i': 40, 'u_i': 2.0735},
        {'id': 3, 'e_m': 6.561179, 'e_o_k': [0.533533, 0.426827, 0.341461, 0.273169, 0.218535, 0.174828], 'p_i': 80, 'u_i': 3.6242},
        {'id': 4, 'e_m': 4.539403, 'e_o_k': [0.756567, 0.605254], 'p_i': 20, 'u_i': 2.1240},
        {'id': 5, 'e_m': 6.765491, 'e_o_k': [0.687550, 0.550040, 0.440032, 0.352026], 'p_i': 80, 'u_i': 2.2796},
        {'id': 6, 'e_m': 1.084629, 'e_o_k': [0.096796, 0.077437, 0.061949, 0.049559, 0.039648], 'p_i': 20, 'u_i': 4.8637},
        {'id': 7, 'e_m': 0.372698, 'e_o_k': [0.045824, 0.036659, 0.029327], 'p_i': 10, 'u_i': 2.9768},
    ]
    B_BUDGET = 95.680017
    return processors, tasks, B_BUDGET
