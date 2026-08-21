"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639995, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.639995, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.711602, 'e_o_k': [0.553468, 0.442774], 'p_i': 10, 'u_i': 2.6844},
        {'id': 1, 'e_m': 1.956038, 'e_o_k': [1.521363, 1.217091], 'p_i': 20, 'u_i': 4.0273},
        {'id': 2, 'e_m': 6.578908, 'e_o_k': [5.116928, 4.093543], 'p_i': 40, 'u_i': 2.2476},
        {'id': 3, 'e_m': 14.898312, 'e_o_k': [11.587576, 9.270061], 'p_i': 80, 'u_i': 1.3199},
        {'id': 4, 'e_m': 4.819102, 'e_o_k': [3.748191, 2.998552], 'p_i': 80, 'u_i': 3.4892},
        {'id': 5, 'e_m': 0.459436, 'e_o_k': [0.357339, 0.285872], 'p_i': 10, 'u_i': 1.4050},
        {'id': 6, 'e_m': 1.319662, 'e_o_k': [1.026404, 0.821123], 'p_i': 20, 'u_i': 3.5798},
        {'id': 7, 'e_m': 2.163416, 'e_o_k': [1.682657, 1.346125], 'p_i': 20, 'u_i': 2.2529},
    ]
    B_BUDGET = 176.639995
    return processors, tasks, B_BUDGET
