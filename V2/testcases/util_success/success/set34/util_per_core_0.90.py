"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279986, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279986, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.850371, 'e_o_k': [0.641728, 0.513383], 'p_i': 10, 'u_i': 4.9296},
        {'id': 1, 'e_m': 4.821488, 'e_o_k': [0.392067, 0.313654, 0.250923, 0.200739, 0.160591, 0.128473], 'p_i': 20, 'u_i': 4.5772},
        {'id': 2, 'e_m': 14.492579, 'e_o_k': [1.293364, 1.034692, 0.827753, 0.662203, 0.529762], 'p_i': 40, 'u_i': 4.4816},
        {'id': 3, 'e_m': 17.502620, 'e_o_k': [1.778722, 1.422977, 1.138382, 0.910705], 'p_i': 80, 'u_i': 1.1432},
        {'id': 4, 'e_m': 2.719328, 'e_o_k': [0.276354, 0.221084, 0.176867, 0.141493], 'p_i': 20, 'u_i': 4.4630},
        {'id': 5, 'e_m': 2.369732, 'e_o_k': [0.240826, 0.192661, 0.154129, 0.123303], 'p_i': 10, 'u_i': 3.8428},
        {'id': 6, 'e_m': 2.358765, 'e_o_k': [0.210504, 0.168403, 0.134722, 0.107778, 0.086222], 'p_i': 20, 'u_i': 4.3035},
        {'id': 7, 'e_m': 2.038268, 'e_o_k': [0.165745, 0.132596, 0.106077, 0.084862, 0.067889, 0.054311], 'p_i': 20, 'u_i': 1.7239},
    ]
    B_BUDGET = 215.279986
    return processors, tasks, B_BUDGET
