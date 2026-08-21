"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680005, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680005, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.143336, 'e_o_k': [0.191278, 0.153023, 0.122418, 0.097934, 0.078348], 'p_i': 10, 'u_i': 1.5090},
        {'id': 1, 'e_m': 1.413954, 'e_o_k': [0.114978, 0.091982, 0.073586, 0.058869, 0.047095, 0.037676], 'p_i': 20, 'u_i': 3.9781},
        {'id': 2, 'e_m': 3.402871, 'e_o_k': [0.418386, 0.334709, 0.267767], 'p_i': 40, 'u_i': 2.6834},
        {'id': 3, 'e_m': 12.001313, 'e_o_k': [2.000219, 1.600175], 'p_i': 80, 'u_i': 1.3712},
        {'id': 4, 'e_m': 0.888149, 'e_o_k': [0.079261, 0.063409, 0.050727, 0.040582, 0.032465], 'p_i': 40, 'u_i': 4.1249},
        {'id': 5, 'e_m': 2.314711, 'e_o_k': [0.188225, 0.150580, 0.120464, 0.096371, 0.077097, 0.061677], 'p_i': 40, 'u_i': 1.3639},
        {'id': 6, 'e_m': 10.156802, 'e_o_k': [0.906426, 0.725141, 0.580112, 0.464090, 0.371272], 'p_i': 80, 'u_i': 1.0001},
        {'id': 7, 'e_m': 0.728490, 'e_o_k': [0.065013, 0.052010, 0.041608, 0.033287, 0.026629], 'p_i': 10, 'u_i': 1.8994},
    ]
    B_BUDGET = 95.680005
    return processors, tasks, B_BUDGET
