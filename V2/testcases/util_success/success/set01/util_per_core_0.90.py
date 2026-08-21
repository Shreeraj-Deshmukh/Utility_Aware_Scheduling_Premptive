"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.28002, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.28002, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.905292, 'e_o_k': [0.398882, 0.319106, 0.255285, 0.204228, 0.163382, 0.130706], 'p_i': 10, 'u_i': 4.4657},
        {'id': 1, 'e_m': 2.064359, 'e_o_k': [0.209793, 0.167834, 0.134267, 0.107414], 'p_i': 20, 'u_i': 3.8247},
        {'id': 2, 'e_m': 5.776462, 'e_o_k': [0.962744, 0.770195], 'p_i': 40, 'u_i': 4.6345},
        {'id': 3, 'e_m': 14.420968, 'e_o_k': [1.773070, 1.418456, 1.134765], 'p_i': 80, 'u_i': 3.0133},
        {'id': 4, 'e_m': 2.738241, 'e_o_k': [0.456374, 0.365099], 'p_i': 40, 'u_i': 4.0741},
        {'id': 5, 'e_m': 32.396954, 'e_o_k': [3.292373, 2.633899, 2.107119, 1.685695], 'p_i': 80, 'u_i': 3.2271},
        {'id': 6, 'e_m': 3.227535, 'e_o_k': [0.328002, 0.262401, 0.209921, 0.167937], 'p_i': 80, 'u_i': 1.2509},
        {'id': 7, 'e_m': 14.712683, 'e_o_k': [2.452114, 1.961691], 'p_i': 40, 'u_i': 4.6197},
    ]
    B_BUDGET = 215.280020
    return processors, tasks, B_BUDGET
