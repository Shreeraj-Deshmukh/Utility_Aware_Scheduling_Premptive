"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600007, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600007, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.226415, 'e_o_k': [0.037736, 0.030189], 'p_i': 10, 'u_i': 4.4075},
        {'id': 1, 'e_m': 0.161347, 'e_o_k': [0.026891, 0.021513], 'p_i': 20, 'u_i': 2.2030},
        {'id': 2, 'e_m': 5.438156, 'e_o_k': [0.668626, 0.534901, 0.427920], 'p_i': 40, 'u_i': 2.4770},
        {'id': 3, 'e_m': 2.530880, 'e_o_k': [0.205803, 0.164642, 0.131714, 0.105371, 0.084297, 0.067437], 'p_i': 80, 'u_i': 1.9604},
        {'id': 4, 'e_m': 3.205763, 'e_o_k': [0.325789, 0.260631, 0.208505, 0.166804], 'p_i': 10, 'u_i': 2.4961},
        {'id': 5, 'e_m': 2.760414, 'e_o_k': [0.339395, 0.271516, 0.217213], 'p_i': 40, 'u_i': 1.0730},
        {'id': 6, 'e_m': 7.289043, 'e_o_k': [0.896194, 0.716955, 0.573564], 'p_i': 20, 'u_i': 2.7749},
        {'id': 7, 'e_m': 0.953249, 'e_o_k': [0.077515, 0.062012, 0.049610, 0.039688, 0.031750, 0.025400], 'p_i': 20, 'u_i': 1.2098},
    ]
    B_BUDGET = 119.600007
    return processors, tasks, B_BUDGET
