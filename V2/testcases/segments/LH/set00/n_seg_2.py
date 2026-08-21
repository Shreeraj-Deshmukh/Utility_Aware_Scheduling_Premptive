"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319991, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319991, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.141359, 'e_o_k': [0.109946, 0.087957], 'p_i': 10, 'u_i': 4.9222},
        {'id': 1, 'e_m': 0.498599, 'e_o_k': [0.387799, 0.310239], 'p_i': 20, 'u_i': 1.9107},
        {'id': 2, 'e_m': 5.343733, 'e_o_k': [4.156237, 3.324989], 'p_i': 40, 'u_i': 1.7322},
        {'id': 3, 'e_m': 4.168750, 'e_o_k': [3.242361, 2.593889], 'p_i': 80, 'u_i': 1.5709},
        {'id': 4, 'e_m': 0.783836, 'e_o_k': [0.609650, 0.487720], 'p_i': 20, 'u_i': 3.7661},
        {'id': 5, 'e_m': 0.731293, 'e_o_k': [0.568783, 0.455027], 'p_i': 20, 'u_i': 1.0932},
        {'id': 6, 'e_m': 0.043154, 'e_o_k': [0.033564, 0.026851], 'p_i': 20, 'u_i': 3.8665},
        {'id': 7, 'e_m': 3.892691, 'e_o_k': [3.027649, 2.422119], 'p_i': 40, 'u_i': 4.9324},
    ]
    B_BUDGET = 88.319991
    return processors, tasks, B_BUDGET
