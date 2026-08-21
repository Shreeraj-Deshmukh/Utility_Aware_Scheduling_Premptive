"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679995, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679995, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.255642, 'e_o_k': [0.020788, 0.016630, 0.013304, 0.010643, 0.008515, 0.006812], 'p_i': 10, 'u_i': 4.5169},
        {'id': 1, 'e_m': 5.834936, 'e_o_k': [0.972489, 0.777991], 'p_i': 20, 'u_i': 3.9484},
        {'id': 2, 'e_m': 1.030030, 'e_o_k': [0.091923, 0.073539, 0.058831, 0.047065, 0.037652], 'p_i': 40, 'u_i': 3.8598},
        {'id': 3, 'e_m': 1.325038, 'e_o_k': [0.107748, 0.086198, 0.068958, 0.055167, 0.044133, 0.035307], 'p_i': 80, 'u_i': 3.9484},
        {'id': 4, 'e_m': 19.367876, 'e_o_k': [2.381296, 1.905037, 1.524030], 'p_i': 80, 'u_i': 4.6365},
        {'id': 5, 'e_m': 0.396585, 'e_o_k': [0.032249, 0.025799, 0.020639, 0.016511, 0.013209, 0.010567], 'p_i': 40, 'u_i': 4.7054},
        {'id': 6, 'e_m': 3.226328, 'e_o_k': [0.537721, 0.430177], 'p_i': 80, 'u_i': 3.2554},
        {'id': 7, 'e_m': 2.960663, 'e_o_k': [0.493444, 0.394755], 'p_i': 20, 'u_i': 3.5452},
    ]
    B_BUDGET = 95.679995
    return processors, tasks, B_BUDGET
