"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.087909, 'e_o_k': [0.050439, 0.040351, 0.032281], 'p_i': 10, 'u_i': 3.9277},
        {'id': 1, 'e_m': 0.284882, 'e_o_k': [0.163457, 0.130765, 0.104612], 'p_i': 20, 'u_i': 1.1365},
        {'id': 2, 'e_m': 1.492482, 'e_o_k': [0.856342, 0.685074, 0.548059], 'p_i': 40, 'u_i': 1.9653},
        {'id': 3, 'e_m': 0.802400, 'e_o_k': [0.460394, 0.368315, 0.294652], 'p_i': 80, 'u_i': 1.4843},
        {'id': 4, 'e_m': 0.312685, 'e_o_k': [0.179409, 0.143528, 0.114822], 'p_i': 10, 'u_i': 4.5666},
        {'id': 5, 'e_m': 0.597481, 'e_o_k': [0.342817, 0.274254, 0.219403], 'p_i': 20, 'u_i': 2.1776},
        {'id': 6, 'e_m': 2.081442, 'e_o_k': [1.194270, 0.955416, 0.764333], 'p_i': 10, 'u_i': 3.5354},
        {'id': 7, 'e_m': 4.826900, 'e_o_k': [2.769533, 2.215626, 1.772501], 'p_i': 80, 'u_i': 3.2835},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
