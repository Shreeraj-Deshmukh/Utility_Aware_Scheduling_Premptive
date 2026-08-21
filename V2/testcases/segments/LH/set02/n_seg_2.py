"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.355801, 'e_o_k': [0.276734, 0.221387], 'p_i': 10, 'u_i': 2.6844},
        {'id': 1, 'e_m': 0.978019, 'e_o_k': [0.760682, 0.608545], 'p_i': 20, 'u_i': 4.0273},
        {'id': 2, 'e_m': 3.289454, 'e_o_k': [2.558464, 2.046771], 'p_i': 40, 'u_i': 2.2476},
        {'id': 3, 'e_m': 7.449156, 'e_o_k': [5.793788, 4.635030], 'p_i': 80, 'u_i': 1.3199},
        {'id': 4, 'e_m': 2.409551, 'e_o_k': [1.874095, 1.499276], 'p_i': 80, 'u_i': 3.4892},
        {'id': 5, 'e_m': 0.229718, 'e_o_k': [0.178670, 0.142936], 'p_i': 10, 'u_i': 1.4050},
        {'id': 6, 'e_m': 0.659831, 'e_o_k': [0.513202, 0.410562], 'p_i': 20, 'u_i': 3.5798},
        {'id': 7, 'e_m': 1.081708, 'e_o_k': [0.841328, 0.673063], 'p_i': 20, 'u_i': 2.2529},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET
