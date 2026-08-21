"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.40001, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.40001, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.059421, 'e_o_k': [0.702992, 0.421795, 0.253077, 0.151846], 'p_i': 10, 'u_i': 1.9017},
        {'id': 1, 'e_m': 2.238024, 'e_o_k': [0.699383, 0.419630], 'p_i': 20, 'u_i': 4.1004},
        {'id': 2, 'e_m': 0.750637, 'e_o_k': [0.172481, 0.103489, 0.062093, 0.037256], 'p_i': 40, 'u_i': 2.6358},
        {'id': 3, 'e_m': 5.306501, 'e_o_k': [1.353699, 0.812220, 0.487332], 'p_i': 80, 'u_i': 4.3577},
        {'id': 4, 'e_m': 0.055926, 'e_o_k': [0.012851, 0.007710, 0.004626, 0.002776], 'p_i': 40, 'u_i': 4.2383},
        {'id': 5, 'e_m': 0.091009, 'e_o_k': [0.019737, 0.011842, 0.007105, 0.004263, 0.002558], 'p_i': 80, 'u_i': 1.1754},
        {'id': 6, 'e_m': 18.185686, 'e_o_k': [5.683027, 3.409816], 'p_i': 80, 'u_i': 2.9766},
        {'id': 7, 'e_m': 2.688109, 'e_o_k': [0.563933, 0.338360, 0.203016, 0.121809, 0.073086, 0.043851], 'p_i': 40, 'u_i': 4.8798},
    ]
    B_BUDGET = 110.400010
    return processors, tasks, B_BUDGET
