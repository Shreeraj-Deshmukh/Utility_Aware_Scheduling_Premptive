"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639983, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 176.639983, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.737228, 'e_o_k': [1.216059, 1.216059], 'p_i': 10, 'u_i': 1.8132},
        {'id': 1, 'e_m': 1.414064, 'e_o_k': [0.329948, 0.329948, 0.329948, 0.329948, 0.329948, 0.329948], 'p_i': 20, 'u_i': 1.3118},
        {'id': 2, 'e_m': 8.894962, 'e_o_k': [2.490589, 2.490589, 2.490589, 2.490589, 2.490589], 'p_i': 40, 'u_i': 1.6432},
        {'id': 3, 'e_m': 3.992321, 'e_o_k': [2.794625, 2.794625], 'p_i': 80, 'u_i': 3.2827},
        {'id': 4, 'e_m': 0.156022, 'e_o_k': [0.043686, 0.043686, 0.043686, 0.043686, 0.043686], 'p_i': 20, 'u_i': 1.0597},
        {'id': 5, 'e_m': 0.352177, 'e_o_k': [0.164349, 0.164349, 0.164349], 'p_i': 20, 'u_i': 4.4596},
        {'id': 6, 'e_m': 5.127088, 'e_o_k': [1.794481, 1.794481, 1.794481, 1.794481], 'p_i': 40, 'u_i': 4.8824},
        {'id': 7, 'e_m': 1.297088, 'e_o_k': [0.605308, 0.605308, 0.605308], 'p_i': 10, 'u_i': 1.5609},
    ]
    B_BUDGET = 176.639983
    return processors, tasks, B_BUDGET
