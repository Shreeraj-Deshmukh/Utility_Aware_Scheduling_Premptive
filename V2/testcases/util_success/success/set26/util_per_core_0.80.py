"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359999, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359999, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.403037, 'e_o_k': [0.195407, 0.156326, 0.125060, 0.100048, 0.080039, 0.064031], 'p_i': 10, 'u_i': 2.8402},
        {'id': 1, 'e_m': 2.656810, 'e_o_k': [0.216043, 0.172834, 0.138268, 0.110614, 0.088491, 0.070793], 'p_i': 20, 'u_i': 1.6917},
        {'id': 2, 'e_m': 5.933180, 'e_o_k': [0.529496, 0.423597, 0.338878, 0.271102, 0.216882], 'p_i': 40, 'u_i': 1.6028},
        {'id': 3, 'e_m': 37.757813, 'e_o_k': [4.642354, 3.713883, 2.971107], 'p_i': 80, 'u_i': 2.5090},
        {'id': 4, 'e_m': 3.496294, 'e_o_k': [0.429872, 0.343898, 0.275118], 'p_i': 40, 'u_i': 2.5667},
        {'id': 5, 'e_m': 9.496503, 'e_o_k': [0.965092, 0.772073, 0.617659, 0.494127], 'p_i': 40, 'u_i': 2.7205},
        {'id': 6, 'e_m': 0.270126, 'e_o_k': [0.027452, 0.021961, 0.017569, 0.014055], 'p_i': 10, 'u_i': 1.7673},
        {'id': 7, 'e_m': 2.547212, 'e_o_k': [0.313182, 0.250545, 0.200436], 'p_i': 10, 'u_i': 2.9380},
    ]
    B_BUDGET = 191.359999
    return processors, tasks, B_BUDGET
