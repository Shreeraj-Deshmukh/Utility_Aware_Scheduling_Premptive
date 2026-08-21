"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.059421, 'e_o_k': [0.849839, 0.679871], 'p_i': 10, 'u_i': 1.9017},
        {'id': 1, 'e_m': 2.238024, 'e_o_k': [0.621673, 0.497339], 'p_i': 20, 'u_i': 4.1004},
        {'id': 2, 'e_m': 0.750637, 'e_o_k': [0.208510, 0.166808], 'p_i': 40, 'u_i': 2.6358},
        {'id': 3, 'e_m': 5.306501, 'e_o_k': [1.474028, 1.179223], 'p_i': 80, 'u_i': 4.3577},
        {'id': 4, 'e_m': 0.055926, 'e_o_k': [0.015535, 0.012428], 'p_i': 40, 'u_i': 4.2383},
        {'id': 5, 'e_m': 0.091009, 'e_o_k': [0.025280, 0.020224], 'p_i': 80, 'u_i': 1.1754},
        {'id': 6, 'e_m': 18.185686, 'e_o_k': [5.051579, 4.041264], 'p_i': 80, 'u_i': 2.9766},
        {'id': 7, 'e_m': 2.688109, 'e_o_k': [0.746697, 0.597357], 'p_i': 40, 'u_i': 4.2232},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
