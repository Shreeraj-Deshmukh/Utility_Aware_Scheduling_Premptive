"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120021, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120021, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.393825, 'e_o_k': [0.032025, 0.025620, 0.020496, 0.016397, 0.013117, 0.010494], 'p_i': 10, 'u_i': 4.6948},
        {'id': 1, 'e_m': 7.397590, 'e_o_k': [0.601547, 0.481238, 0.384990, 0.307992, 0.246394, 0.197115], 'p_i': 20, 'u_i': 1.5554},
        {'id': 2, 'e_m': 7.947405, 'e_o_k': [1.324567, 1.059654], 'p_i': 40, 'u_i': 4.1277},
        {'id': 3, 'e_m': 13.999244, 'e_o_k': [1.249338, 0.999470, 0.799576, 0.639661, 0.511729], 'p_i': 80, 'u_i': 1.1747},
        {'id': 4, 'e_m': 14.591371, 'e_o_k': [1.794021, 1.435217, 1.148173], 'p_i': 40, 'u_i': 2.4278},
        {'id': 5, 'e_m': 1.790338, 'e_o_k': [0.220123, 0.176099, 0.140879], 'p_i': 10, 'u_i': 2.1744},
        {'id': 6, 'e_m': 4.888741, 'e_o_k': [0.436287, 0.349030, 0.279224, 0.223379, 0.178703], 'p_i': 10, 'u_i': 4.1867},
        {'id': 7, 'e_m': 7.687404, 'e_o_k': [0.686049, 0.548839, 0.439071, 0.351257, 0.281006], 'p_i': 20, 'u_i': 3.6278},
    ]
    B_BUDGET = 263.120021
    return processors, tasks, B_BUDGET
