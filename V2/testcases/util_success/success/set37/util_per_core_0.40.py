"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680003, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680003, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.381593, 'e_o_k': [0.396932, 0.317546], 'p_i': 10, 'u_i': 3.1340},
        {'id': 1, 'e_m': 0.718285, 'e_o_k': [0.072996, 0.058397, 0.046718, 0.037374], 'p_i': 20, 'u_i': 4.7064},
        {'id': 2, 'e_m': 1.663706, 'e_o_k': [0.148475, 0.118780, 0.095024, 0.076019, 0.060815], 'p_i': 40, 'u_i': 3.9461},
        {'id': 3, 'e_m': 20.841520, 'e_o_k': [2.118041, 1.694433, 1.355546, 1.084437], 'p_i': 80, 'u_i': 2.2173},
        {'id': 4, 'e_m': 1.314253, 'e_o_k': [0.219042, 0.175234], 'p_i': 20, 'u_i': 4.4667},
        {'id': 5, 'e_m': 0.736106, 'e_o_k': [0.065693, 0.052554, 0.042043, 0.033635, 0.026908], 'p_i': 10, 'u_i': 3.9626},
        {'id': 6, 'e_m': 1.268397, 'e_o_k': [0.155950, 0.124760, 0.099808], 'p_i': 20, 'u_i': 1.6271},
        {'id': 7, 'e_m': 0.842866, 'e_o_k': [0.075220, 0.060176, 0.048141, 0.038513, 0.030810], 'p_i': 40, 'u_i': 2.4987},
    ]
    B_BUDGET = 95.680003
    return processors, tasks, B_BUDGET
