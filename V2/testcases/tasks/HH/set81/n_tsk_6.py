"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639992, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639992, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.107893, 'e_o_k': [0.635677, 0.508541, 0.406833], 'p_i': 10, 'u_i': 1.6802},
        {'id': 1, 'e_m': 3.595129, 'e_o_k': [2.796212, 2.236969], 'p_i': 20, 'u_i': 4.8914},
        {'id': 2, 'e_m': 4.190122, 'e_o_k': [1.590058, 1.272047, 1.017637, 0.814110, 0.651288, 0.521030], 'p_i': 40, 'u_i': 2.7135},
        {'id': 3, 'e_m': 24.008225, 'e_o_k': [9.110589, 7.288471, 5.830777, 4.664622, 3.731697, 2.985358], 'p_i': 80, 'u_i': 1.9259},
        {'id': 4, 'e_m': 3.350223, 'e_o_k': [1.588859, 1.271087, 1.016870, 0.813496], 'p_i': 40, 'u_i': 2.2208},
        {'id': 5, 'e_m': 0.833710, 'e_o_k': [0.347214, 0.277771, 0.222217, 0.177773, 0.142219], 'p_i': 40, 'u_i': 3.1305},
    ]
    B_BUDGET = 176.639992
    return processors, tasks, B_BUDGET
