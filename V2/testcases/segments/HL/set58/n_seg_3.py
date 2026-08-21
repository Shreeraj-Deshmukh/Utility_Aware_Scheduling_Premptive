"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.39999, "H": 80, "J": 40, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.39999, "H": 80, "J": 40, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.259080, 'e_o_k': [0.258008, 0.206407, 0.165125], 'p_i': 10, 'u_i': 2.8729},
        {'id': 1, 'e_m': 3.910652, 'e_o_k': [0.801363, 0.641091, 0.512872], 'p_i': 20, 'u_i': 4.4646},
        {'id': 2, 'e_m': 0.555334, 'e_o_k': [0.113798, 0.091038, 0.072831], 'p_i': 40, 'u_i': 2.8456},
        {'id': 3, 'e_m': 5.117361, 'e_o_k': [1.048640, 0.838912, 0.671129], 'p_i': 80, 'u_i': 4.6357},
        {'id': 4, 'e_m': 0.830972, 'e_o_k': [0.170281, 0.136225, 0.108980], 'p_i': 10, 'u_i': 3.1275},
        {'id': 5, 'e_m': 13.997484, 'e_o_k': [2.868337, 2.294670, 1.835736], 'p_i': 80, 'u_i': 2.7677},
        {'id': 6, 'e_m': 1.327086, 'e_o_k': [0.271944, 0.217555, 0.174044], 'p_i': 10, 'u_i': 2.2237},
        {'id': 7, 'e_m': 0.099346, 'e_o_k': [0.020358, 0.016286, 0.013029], 'p_i': 10, 'u_i': 3.7702},
    ]
    B_BUDGET = 110.399990
    return processors, tasks, B_BUDGET
