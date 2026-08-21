"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640005, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640005, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.789693, 'e_o_k': [0.453103, 0.362482, 0.289986], 'p_i': 10, 'u_i': 4.2289},
        {'id': 1, 'e_m': 0.245294, 'e_o_k': [0.140743, 0.112594, 0.090075], 'p_i': 20, 'u_i': 3.6434},
        {'id': 2, 'e_m': 3.310794, 'e_o_k': [1.899636, 1.519709, 1.215767], 'p_i': 40, 'u_i': 2.1879},
        {'id': 3, 'e_m': 1.628519, 'e_o_k': [0.934396, 0.747517, 0.598014], 'p_i': 80, 'u_i': 2.3607},
        {'id': 4, 'e_m': 2.051152, 'e_o_k': [1.176890, 0.941512, 0.753210], 'p_i': 20, 'u_i': 2.0600},
        {'id': 5, 'e_m': 0.110349, 'e_o_k': [0.063315, 0.050652, 0.040522], 'p_i': 80, 'u_i': 2.1803},
        {'id': 6, 'e_m': 3.223708, 'e_o_k': [1.849668, 1.479735, 1.183788], 'p_i': 10, 'u_i': 4.5157},
        {'id': 7, 'e_m': 7.173276, 'e_o_k': [4.115814, 3.292651, 2.634121], 'p_i': 40, 'u_i': 4.4957},
    ]
    B_BUDGET = 176.640005
    return processors, tasks, B_BUDGET
