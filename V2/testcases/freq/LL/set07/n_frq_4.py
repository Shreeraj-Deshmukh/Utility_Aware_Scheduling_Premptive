"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200009, "H": 80, "J": 36, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "freq", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200009, "H": 80, "J": 36, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "freq", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.087909, 'e_o_k': [0.011914, 0.009531, 0.007625, 0.006100, 0.004880, 0.003904], 'p_i': 10, 'u_i': 2.1335},
        {'id': 1, 'e_m': 0.284882, 'e_o_k': [0.038609, 0.030888, 0.024710, 0.019768, 0.015814, 0.012652], 'p_i': 20, 'u_i': 1.1307},
        {'id': 2, 'e_m': 1.492482, 'e_o_k': [0.221990, 0.177592, 0.142073, 0.113659, 0.090927], 'p_i': 40, 'u_i': 4.3260},
        {'id': 3, 'e_m': 0.802400, 'e_o_k': [0.164426, 0.131541, 0.105233], 'p_i': 80, 'u_i': 4.7000},
        {'id': 4, 'e_m': 0.312685, 'e_o_k': [0.086857, 0.069486], 'p_i': 10, 'u_i': 1.4843},
        {'id': 5, 'e_m': 0.597481, 'e_o_k': [0.165967, 0.132774], 'p_i': 20, 'u_i': 4.5666},
        {'id': 6, 'e_m': 2.081442, 'e_o_k': [0.309591, 0.247673, 0.198138, 0.158511, 0.126808], 'p_i': 10, 'u_i': 2.1776},
        {'id': 7, 'e_m': 4.826900, 'e_o_k': [0.989119, 0.791295, 0.633036], 'p_i': 80, 'u_i': 3.5354},
    ]
    B_BUDGET = 55.200009
    return processors, tasks, B_BUDGET
