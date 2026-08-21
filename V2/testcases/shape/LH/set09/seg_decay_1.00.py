"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320009, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.320009, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.868614, 'e_o_k': [0.608030, 0.608030], 'p_i': 10, 'u_i': 1.8132},
        {'id': 1, 'e_m': 0.707032, 'e_o_k': [0.164974, 0.164974, 0.164974, 0.164974, 0.164974, 0.164974], 'p_i': 20, 'u_i': 1.3118},
        {'id': 2, 'e_m': 4.447481, 'e_o_k': [1.245295, 1.245295, 1.245295, 1.245295, 1.245295], 'p_i': 40, 'u_i': 1.6432},
        {'id': 3, 'e_m': 1.996160, 'e_o_k': [1.397312, 1.397312], 'p_i': 80, 'u_i': 3.2827},
        {'id': 4, 'e_m': 0.078011, 'e_o_k': [0.021843, 0.021843, 0.021843, 0.021843, 0.021843], 'p_i': 20, 'u_i': 1.0597},
        {'id': 5, 'e_m': 0.176089, 'e_o_k': [0.082175, 0.082175, 0.082175], 'p_i': 20, 'u_i': 4.4596},
        {'id': 6, 'e_m': 2.563544, 'e_o_k': [0.897240, 0.897240, 0.897240, 0.897240], 'p_i': 40, 'u_i': 4.8824},
        {'id': 7, 'e_m': 0.648544, 'e_o_k': [0.302654, 0.302654, 0.302654], 'p_i': 10, 'u_i': 1.5609},
    ]
    B_BUDGET = 88.320009
    return processors, tasks, B_BUDGET
