"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759995, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759995, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.944310, 'e_o_k': [0.076788, 0.061431, 0.049144, 0.039316, 0.031452, 0.025162], 'p_i': 10, 'u_i': 4.1820},
        {'id': 1, 'e_m': 2.932989, 'e_o_k': [0.488832, 0.391065], 'p_i': 20, 'u_i': 2.8729},
        {'id': 2, 'e_m': 0.416501, 'e_o_k': [0.051209, 0.040967, 0.032774], 'p_i': 40, 'u_i': 4.4646},
        {'id': 3, 'e_m': 3.838021, 'e_o_k': [0.639670, 0.511736], 'p_i': 80, 'u_i': 2.8456},
        {'id': 4, 'e_m': 0.623229, 'e_o_k': [0.063336, 0.050669, 0.040535, 0.032428], 'p_i': 10, 'u_i': 4.6357},
        {'id': 5, 'e_m': 10.498113, 'e_o_k': [1.749686, 1.399748], 'p_i': 80, 'u_i': 3.1275},
        {'id': 6, 'e_m': 0.995314, 'e_o_k': [0.101150, 0.080920, 0.064736, 0.051789], 'p_i': 10, 'u_i': 2.7677},
        {'id': 7, 'e_m': 0.074510, 'e_o_k': [0.007572, 0.006058, 0.004846, 0.003877], 'p_i': 10, 'u_i': 2.2237},
    ]
    B_BUDGET = 71.759995
    return processors, tasks, B_BUDGET
