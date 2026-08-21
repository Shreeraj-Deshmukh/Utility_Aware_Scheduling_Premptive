"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200006, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200006, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.110143, 'e_o_k': [0.366802, 0.293442, 0.234754, 0.187803, 0.150242], 'p_i': 10, 'u_i': 2.9699},
        {'id': 1, 'e_m': 0.793032, 'e_o_k': [0.097504, 0.078003, 0.062403], 'p_i': 20, 'u_i': 1.6736},
        {'id': 2, 'e_m': 2.923537, 'e_o_k': [0.260906, 0.208725, 0.166980, 0.133584, 0.106867], 'p_i': 40, 'u_i': 2.6796},
        {'id': 3, 'e_m': 30.759763, 'e_o_k': [3.781938, 3.025550, 2.420440], 'p_i': 80, 'u_i': 2.5270},
        {'id': 4, 'e_m': 6.044236, 'e_o_k': [0.614252, 0.491401, 0.393121, 0.314497], 'p_i': 20, 'u_i': 1.9244},
        {'id': 5, 'e_m': 4.404459, 'e_o_k': [0.734076, 0.587261], 'p_i': 10, 'u_i': 4.2011},
        {'id': 6, 'e_m': 2.591906, 'e_o_k': [0.231310, 0.185048, 0.148038, 0.118431, 0.094745], 'p_i': 40, 'u_i': 3.3831},
        {'id': 7, 'e_m': 5.685867, 'e_o_k': [0.507425, 0.405940, 0.324752, 0.259802, 0.207841], 'p_i': 20, 'u_i': 4.9669},
    ]
    B_BUDGET = 239.200006
    return processors, tasks, B_BUDGET
