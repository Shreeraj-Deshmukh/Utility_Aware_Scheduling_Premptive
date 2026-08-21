"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440007, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440007, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.014264, 'e_o_k': [0.103076, 0.082460, 0.065968, 0.052775], 'p_i': 10, 'u_i': 4.6704},
        {'id': 1, 'e_m': 0.131070, 'e_o_k': [0.021845, 0.017476], 'p_i': 20, 'u_i': 1.7142},
        {'id': 2, 'e_m': 12.970503, 'e_o_k': [1.594734, 1.275787, 1.020630], 'p_i': 40, 'u_i': 2.7421},
        {'id': 3, 'e_m': 15.998894, 'e_o_k': [1.300977, 1.040782, 0.832625, 0.666100, 0.532880, 0.426304], 'p_i': 80, 'u_i': 1.9194},
        {'id': 4, 'e_m': 6.628810, 'e_o_k': [1.104802, 0.883841], 'p_i': 20, 'u_i': 4.0448},
        {'id': 5, 'e_m': 5.437261, 'e_o_k': [0.668516, 0.534813, 0.427850], 'p_i': 20, 'u_i': 1.1256},
        {'id': 6, 'e_m': 0.179960, 'e_o_k': [0.018289, 0.014631, 0.011705, 0.009364], 'p_i': 10, 'u_i': 3.9028},
        {'id': 7, 'e_m': 2.929435, 'e_o_k': [0.261432, 0.209146, 0.167317, 0.133853, 0.107083], 'p_i': 20, 'u_i': 2.5194},
    ]
    B_BUDGET = 167.440007
    return processors, tasks, B_BUDGET
