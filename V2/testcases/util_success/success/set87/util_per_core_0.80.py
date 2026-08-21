"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360011, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360011, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.288114, 'e_o_k': [0.293442, 0.234754, 0.187803, 0.150242, 0.120194], 'p_i': 10, 'u_i': 2.9699},
        {'id': 1, 'e_m': 0.634426, 'e_o_k': [0.078003, 0.062403, 0.049922], 'p_i': 20, 'u_i': 1.6736},
        {'id': 2, 'e_m': 2.338830, 'e_o_k': [0.208725, 0.166980, 0.133584, 0.106867, 0.085494], 'p_i': 40, 'u_i': 2.6796},
        {'id': 3, 'e_m': 24.607810, 'e_o_k': [3.025550, 2.420440, 1.936352], 'p_i': 80, 'u_i': 2.5270},
        {'id': 4, 'e_m': 4.835389, 'e_o_k': [0.491401, 0.393121, 0.314497, 0.251597], 'p_i': 20, 'u_i': 1.9244},
        {'id': 5, 'e_m': 3.523567, 'e_o_k': [0.587261, 0.469809], 'p_i': 10, 'u_i': 4.2011},
        {'id': 6, 'e_m': 2.073525, 'e_o_k': [0.185048, 0.148038, 0.118431, 0.094745, 0.075796], 'p_i': 40, 'u_i': 3.3831},
        {'id': 7, 'e_m': 4.548694, 'e_o_k': [0.405940, 0.324752, 0.259802, 0.207841, 0.166273], 'p_i': 20, 'u_i': 4.9669},
    ]
    B_BUDGET = 191.360011
    return processors, tasks, B_BUDGET
