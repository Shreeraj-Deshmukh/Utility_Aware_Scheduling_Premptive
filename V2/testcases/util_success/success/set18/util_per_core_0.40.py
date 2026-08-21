"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680006, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680006, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.996752, 'e_o_k': [0.088953, 0.071163, 0.056930, 0.045544, 0.036435], 'p_i': 10, 'u_i': 4.1058},
        {'id': 1, 'e_m': 0.594019, 'e_o_k': [0.073035, 0.058428, 0.046743], 'p_i': 20, 'u_i': 1.5782},
        {'id': 2, 'e_m': 1.782547, 'e_o_k': [0.159080, 0.127264, 0.101811, 0.081449, 0.065159], 'p_i': 40, 'u_i': 1.2072},
        {'id': 3, 'e_m': 4.659020, 'e_o_k': [0.415786, 0.332629, 0.266103, 0.212882, 0.170306], 'p_i': 80, 'u_i': 4.8515},
        {'id': 4, 'e_m': 0.874227, 'e_o_k': [0.071089, 0.056871, 0.045497, 0.036398, 0.029118, 0.023295], 'p_i': 20, 'u_i': 3.3809},
        {'id': 5, 'e_m': 18.325230, 'e_o_k': [1.862320, 1.489856, 1.191885, 0.953508], 'p_i': 80, 'u_i': 4.9290},
        {'id': 6, 'e_m': 1.553215, 'e_o_k': [0.258869, 0.207095], 'p_i': 20, 'u_i': 1.8035},
        {'id': 7, 'e_m': 2.173850, 'e_o_k': [0.220920, 0.176736, 0.141389, 0.113111], 'p_i': 10, 'u_i': 3.4846},
    ]
    B_BUDGET = 95.680006
    return processors, tasks, B_BUDGET
