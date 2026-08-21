"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.087909, 'e_o_k': [0.018014, 0.014411, 0.011529], 'p_i': 10, 'u_i': 3.9277},
        {'id': 1, 'e_m': 0.284882, 'e_o_k': [0.058377, 0.046702, 0.037362], 'p_i': 20, 'u_i': 1.1365},
        {'id': 2, 'e_m': 1.492482, 'e_o_k': [0.305836, 0.244669, 0.195735], 'p_i': 40, 'u_i': 1.9653},
        {'id': 3, 'e_m': 0.802400, 'e_o_k': [0.164426, 0.131541, 0.105233], 'p_i': 80, 'u_i': 1.4843},
        {'id': 4, 'e_m': 0.312685, 'e_o_k': [0.064075, 0.051260, 0.041008], 'p_i': 10, 'u_i': 4.5666},
        {'id': 5, 'e_m': 0.597481, 'e_o_k': [0.122435, 0.097948, 0.078358], 'p_i': 20, 'u_i': 2.1776},
        {'id': 6, 'e_m': 2.081442, 'e_o_k': [0.426525, 0.341220, 0.272976], 'p_i': 10, 'u_i': 3.5354},
        {'id': 7, 'e_m': 4.826900, 'e_o_k': [0.989119, 0.791295, 0.633036], 'p_i': 80, 'u_i': 3.2835},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
