"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.52001, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.52001, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.758680, 'e_o_k': [0.126447, 0.101157], 'p_i': 10, 'u_i': 2.8589},
        {'id': 1, 'e_m': 0.292828, 'e_o_k': [0.036003, 0.028803, 0.023042], 'p_i': 20, 'u_i': 2.7598},
        {'id': 2, 'e_m': 15.276342, 'e_o_k': [2.546057, 2.036846], 'p_i': 40, 'u_i': 2.0735},
        {'id': 3, 'e_m': 9.841768, 'e_o_k': [0.800300, 0.640240, 0.512192, 0.409754, 0.327803, 0.262242], 'p_i': 80, 'u_i': 3.6242},
        {'id': 4, 'e_m': 6.809104, 'e_o_k': [1.134851, 0.907881], 'p_i': 20, 'u_i': 2.1240},
        {'id': 5, 'e_m': 10.148237, 'e_o_k': [1.031325, 0.825060, 0.660048, 0.528038], 'p_i': 80, 'u_i': 2.2796},
        {'id': 6, 'e_m': 1.626943, 'e_o_k': [0.145194, 0.116155, 0.092924, 0.074339, 0.059471], 'p_i': 20, 'u_i': 4.8637},
        {'id': 7, 'e_m': 0.559047, 'e_o_k': [0.068735, 0.054988, 0.043991], 'p_i': 10, 'u_i': 2.9768},
    ]
    B_BUDGET = 143.520010
    return processors, tasks, B_BUDGET
