"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599998, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599998, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.167852, 'e_o_k': [0.017058, 0.013647, 0.010917, 0.008734], 'p_i': 10, 'u_i': 3.0491},
        {'id': 1, 'e_m': 1.993882, 'e_o_k': [0.177940, 0.142352, 0.113882, 0.091105, 0.072884], 'p_i': 20, 'u_i': 3.9469},
        {'id': 2, 'e_m': 5.108747, 'e_o_k': [0.628125, 0.502500, 0.402000], 'p_i': 40, 'u_i': 1.2331},
        {'id': 3, 'e_m': 12.640301, 'e_o_k': [1.554135, 1.243308, 0.994647], 'p_i': 80, 'u_i': 3.8857},
        {'id': 4, 'e_m': 2.394949, 'e_o_k': [0.399158, 0.319327], 'p_i': 20, 'u_i': 4.4773},
        {'id': 5, 'e_m': 1.256705, 'e_o_k': [0.209451, 0.167561], 'p_i': 10, 'u_i': 2.4546},
        {'id': 6, 'e_m': 1.366873, 'e_o_k': [0.138910, 0.111128, 0.088902, 0.071122], 'p_i': 80, 'u_i': 1.1544},
        {'id': 7, 'e_m': 26.823548, 'e_o_k': [3.297977, 2.638382, 2.110705], 'p_i': 80, 'u_i': 4.0204},
    ]
    B_BUDGET = 119.599998
    return processors, tasks, B_BUDGET
