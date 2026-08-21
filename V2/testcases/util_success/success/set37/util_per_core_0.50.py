"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600003, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600003, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.976991, 'e_o_k': [0.496165, 0.396932], 'p_i': 10, 'u_i': 3.1340},
        {'id': 1, 'e_m': 0.897856, 'e_o_k': [0.091246, 0.072996, 0.058397, 0.046718], 'p_i': 20, 'u_i': 4.7064},
        {'id': 2, 'e_m': 2.079633, 'e_o_k': [0.185593, 0.148475, 0.118780, 0.095024, 0.076019], 'p_i': 40, 'u_i': 3.9461},
        {'id': 3, 'e_m': 26.051900, 'e_o_k': [2.647551, 2.118041, 1.694433, 1.355546], 'p_i': 80, 'u_i': 2.2173},
        {'id': 4, 'e_m': 1.642816, 'e_o_k': [0.273803, 0.219042], 'p_i': 20, 'u_i': 4.4667},
        {'id': 5, 'e_m': 0.920133, 'e_o_k': [0.082116, 0.065693, 0.052554, 0.042043, 0.033635], 'p_i': 10, 'u_i': 3.9626},
        {'id': 6, 'e_m': 1.585496, 'e_o_k': [0.194938, 0.155950, 0.124760], 'p_i': 20, 'u_i': 1.6271},
        {'id': 7, 'e_m': 1.053583, 'e_o_k': [0.094025, 0.075220, 0.060176, 0.048141, 0.038513], 'p_i': 40, 'u_i': 2.4987},
    ]
    B_BUDGET = 119.600003
    return processors, tasks, B_BUDGET
