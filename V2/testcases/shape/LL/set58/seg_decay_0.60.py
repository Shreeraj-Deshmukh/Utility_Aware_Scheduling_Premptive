"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199985, "H": 80, "J": 40, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.199985, "H": 80, "J": 40, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.629540, 'e_o_k': [0.132070, 0.079242, 0.047545, 0.028527, 0.017116, 0.010270], 'p_i': 10, 'u_i': 4.1820},
        {'id': 1, 'e_m': 1.955326, 'e_o_k': [0.611039, 0.366624], 'p_i': 20, 'u_i': 2.8729},
        {'id': 2, 'e_m': 0.277667, 'e_o_k': [0.070833, 0.042500, 0.025500], 'p_i': 40, 'u_i': 4.4646},
        {'id': 3, 'e_m': 2.558681, 'e_o_k': [0.799588, 0.479753], 'p_i': 80, 'u_i': 2.8456},
        {'id': 4, 'e_m': 0.415486, 'e_o_k': [0.095470, 0.057282, 0.034369, 0.020622], 'p_i': 10, 'u_i': 4.6357},
        {'id': 5, 'e_m': 6.998742, 'e_o_k': [2.187107, 1.312264], 'p_i': 80, 'u_i': 3.1275},
        {'id': 6, 'e_m': 0.663543, 'e_o_k': [0.152468, 0.091481, 0.054889, 0.032933], 'p_i': 10, 'u_i': 2.7677},
        {'id': 7, 'e_m': 0.049673, 'e_o_k': [0.011414, 0.006848, 0.004109, 0.002465], 'p_i': 10, 'u_i': 2.2237},
    ]
    B_BUDGET = 55.199985
    return processors, tasks, B_BUDGET
