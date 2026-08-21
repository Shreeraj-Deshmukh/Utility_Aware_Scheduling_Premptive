"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359992, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359992, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.916471, 'e_o_k': [0.081789, 0.065431, 0.052345, 0.041876, 0.033501], 'p_i': 10, 'u_i': 1.3802},
        {'id': 1, 'e_m': 3.397234, 'e_o_k': [0.417693, 0.334154, 0.267323], 'p_i': 20, 'u_i': 1.3476},
        {'id': 2, 'e_m': 5.648853, 'e_o_k': [0.941476, 0.753180], 'p_i': 40, 'u_i': 4.5157},
        {'id': 3, 'e_m': 23.524675, 'e_o_k': [2.892378, 2.313902, 1.851122], 'p_i': 80, 'u_i': 4.4957},
        {'id': 4, 'e_m': 0.622240, 'e_o_k': [0.050598, 0.040479, 0.032383, 0.025906, 0.020725, 0.016580], 'p_i': 10, 'u_i': 4.5672},
        {'id': 5, 'e_m': 3.387648, 'e_o_k': [0.344273, 0.275419, 0.220335, 0.176268], 'p_i': 40, 'u_i': 4.7861},
        {'id': 6, 'e_m': 2.564960, 'e_o_k': [0.208574, 0.166859, 0.133487, 0.106790, 0.085432, 0.068346], 'p_i': 10, 'u_i': 1.1886},
        {'id': 7, 'e_m': 19.992008, 'e_o_k': [2.031708, 1.625366, 1.300293, 1.040235], 'p_i': 40, 'u_i': 4.3925},
    ]
    B_BUDGET = 191.359992
    return processors, tasks, B_BUDGET
