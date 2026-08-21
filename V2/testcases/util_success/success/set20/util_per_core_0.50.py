"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600016, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600016, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.679170, 'e_o_k': [0.239098, 0.191278, 0.153023, 0.122418, 0.097934], 'p_i': 10, 'u_i': 1.5090},
        {'id': 1, 'e_m': 1.767443, 'e_o_k': [0.143723, 0.114978, 0.091982, 0.073586, 0.058869, 0.047095], 'p_i': 20, 'u_i': 3.9781},
        {'id': 2, 'e_m': 4.253588, 'e_o_k': [0.522982, 0.418386, 0.334709], 'p_i': 40, 'u_i': 2.6834},
        {'id': 3, 'e_m': 15.001642, 'e_o_k': [2.500274, 2.000219], 'p_i': 80, 'u_i': 1.3712},
        {'id': 4, 'e_m': 1.110187, 'e_o_k': [0.099077, 0.079261, 0.063409, 0.050727, 0.040582], 'p_i': 40, 'u_i': 4.1249},
        {'id': 5, 'e_m': 2.893388, 'e_o_k': [0.235281, 0.188225, 0.150580, 0.120464, 0.096371, 0.077097], 'p_i': 40, 'u_i': 1.3639},
        {'id': 6, 'e_m': 12.696002, 'e_o_k': [1.133032, 0.906426, 0.725141, 0.580112, 0.464090], 'p_i': 80, 'u_i': 1.0001},
        {'id': 7, 'e_m': 0.910613, 'e_o_k': [0.081266, 0.065013, 0.052010, 0.041608, 0.033287], 'p_i': 10, 'u_i': 1.8994},
    ]
    B_BUDGET = 119.600016
    return processors, tasks, B_BUDGET
