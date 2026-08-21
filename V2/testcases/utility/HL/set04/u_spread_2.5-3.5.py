"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400005, "H": 80, "J": 33, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 110.400005, "H": 80, "J": 33, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.929756, 'e_o_k': [0.126008, 0.100806, 0.080645, 0.064516, 0.051613, 0.041290], 'p_i': 10, 'u_i': 2.8696},
        {'id': 1, 'e_m': 0.056878, 'e_o_k': [0.007709, 0.006167, 0.004933, 0.003947, 0.003157, 0.002526], 'p_i': 20, 'u_i': 2.7359},
        {'id': 2, 'e_m': 2.623994, 'e_o_k': [0.728887, 0.583110], 'p_i': 40, 'u_i': 2.6432},
        {'id': 3, 'e_m': 4.474673, 'e_o_k': [1.242965, 0.994372], 'p_i': 80, 'u_i': 2.6277},
        {'id': 4, 'e_m': 2.349668, 'e_o_k': [0.652686, 0.522149], 'p_i': 20, 'u_i': 3.3363},
        {'id': 5, 'e_m': 10.542988, 'e_o_k': [1.785737, 1.428589, 1.142871, 0.914297], 'p_i': 40, 'u_i': 2.9313},
        {'id': 6, 'e_m': 0.342456, 'e_o_k': [0.095127, 0.076101], 'p_i': 10, 'u_i': 2.6179},
        {'id': 7, 'e_m': 3.346871, 'e_o_k': [0.929686, 0.743749], 'p_i': 20, 'u_i': 2.9790},
    ]
    B_BUDGET = 110.400005
    return processors, tasks, B_BUDGET
