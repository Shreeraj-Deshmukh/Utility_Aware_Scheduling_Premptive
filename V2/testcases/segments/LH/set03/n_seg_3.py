"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32002, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.32002, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.379864, 'e_o_k': [0.217955, 0.174364, 0.139491], 'p_i': 10, 'u_i': 3.3255},
        {'id': 1, 'e_m': 1.133617, 'e_o_k': [0.650436, 0.520349, 0.416279], 'p_i': 20, 'u_i': 3.5739},
        {'id': 2, 'e_m': 0.770090, 'e_o_k': [0.441855, 0.353484, 0.282787], 'p_i': 40, 'u_i': 2.2786},
        {'id': 3, 'e_m': 4.175854, 'e_o_k': [2.395982, 1.916785, 1.533428], 'p_i': 80, 'u_i': 1.5604},
        {'id': 4, 'e_m': 4.336894, 'e_o_k': [2.488382, 1.990706, 1.592564], 'p_i': 80, 'u_i': 1.1253},
        {'id': 5, 'e_m': 12.059321, 'e_o_k': [6.919282, 5.535426, 4.428341], 'p_i': 80, 'u_i': 3.7966},
        {'id': 6, 'e_m': 0.192411, 'e_o_k': [0.110400, 0.088320, 0.070656], 'p_i': 10, 'u_i': 1.2428},
        {'id': 7, 'e_m': 0.387543, 'e_o_k': [0.222361, 0.177889, 0.142311], 'p_i': 40, 'u_i': 4.6455},
    ]
    B_BUDGET = 88.320020
    return processors, tasks, B_BUDGET
