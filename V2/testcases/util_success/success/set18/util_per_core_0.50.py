"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600003, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600003, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.245940, 'e_o_k': [0.111192, 0.088953, 0.071163, 0.056930, 0.045544], 'p_i': 10, 'u_i': 4.1058},
        {'id': 1, 'e_m': 0.742524, 'e_o_k': [0.091294, 0.073035, 0.058428], 'p_i': 20, 'u_i': 1.5782},
        {'id': 2, 'e_m': 2.228183, 'e_o_k': [0.198850, 0.159080, 0.127264, 0.101811, 0.081449], 'p_i': 40, 'u_i': 1.2072},
        {'id': 3, 'e_m': 5.823775, 'e_o_k': [0.519732, 0.415786, 0.332629, 0.266103, 0.212882], 'p_i': 80, 'u_i': 4.8515},
        {'id': 4, 'e_m': 1.092784, 'e_o_k': [0.088862, 0.071089, 0.056871, 0.045497, 0.036398, 0.029118], 'p_i': 20, 'u_i': 3.3809},
        {'id': 5, 'e_m': 22.906537, 'e_o_k': [2.327900, 1.862320, 1.489856, 1.191885], 'p_i': 80, 'u_i': 4.9290},
        {'id': 6, 'e_m': 1.941518, 'e_o_k': [0.323586, 0.258869], 'p_i': 20, 'u_i': 1.8035},
        {'id': 7, 'e_m': 2.717312, 'e_o_k': [0.276150, 0.220920, 0.176736, 0.141389], 'p_i': 10, 'u_i': 3.4846},
    ]
    B_BUDGET = 119.600003
    return processors, tasks, B_BUDGET
