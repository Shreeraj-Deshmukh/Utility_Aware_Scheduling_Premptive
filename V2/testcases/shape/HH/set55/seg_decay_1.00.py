"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640017, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 176.640017, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.362417, 'e_o_k': [0.551231, 0.551231, 0.551231, 0.551231, 0.551231, 0.551231], 'p_i': 10, 'u_i': 4.5134},
        {'id': 1, 'e_m': 1.818372, 'e_o_k': [0.848573, 0.848573, 0.848573], 'p_i': 20, 'u_i': 4.5874},
        {'id': 2, 'e_m': 2.018400, 'e_o_k': [0.941920, 0.941920, 0.941920], 'p_i': 40, 'u_i': 2.7347},
        {'id': 3, 'e_m': 10.977605, 'e_o_k': [5.122882, 5.122882, 5.122882], 'p_i': 80, 'u_i': 4.9671},
        {'id': 4, 'e_m': 5.439997, 'e_o_k': [1.523199, 1.523199, 1.523199, 1.523199, 1.523199], 'p_i': 80, 'u_i': 4.8761},
        {'id': 5, 'e_m': 0.284101, 'e_o_k': [0.099436, 0.099436, 0.099436, 0.099436], 'p_i': 10, 'u_i': 2.5248},
        {'id': 6, 'e_m': 1.455737, 'e_o_k': [1.019016, 1.019016], 'p_i': 40, 'u_i': 4.9532},
        {'id': 7, 'e_m': 6.094243, 'e_o_k': [2.132985, 2.132985, 2.132985, 2.132985], 'p_i': 40, 'u_i': 2.2979},
    ]
    B_BUDGET = 176.640017
    return processors, tasks, B_BUDGET
