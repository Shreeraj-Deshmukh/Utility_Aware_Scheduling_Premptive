"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32001, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.32001, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.087909, 'e_o_k': [0.068373, 0.054699], 'p_i': 10, 'u_i': 3.9277},
        {'id': 1, 'e_m': 0.284882, 'e_o_k': [0.221575, 0.177260], 'p_i': 20, 'u_i': 1.1365},
        {'id': 2, 'e_m': 1.492482, 'e_o_k': [1.160819, 0.928655], 'p_i': 40, 'u_i': 1.9653},
        {'id': 3, 'e_m': 0.802400, 'e_o_k': [0.624089, 0.499271], 'p_i': 80, 'u_i': 1.4843},
        {'id': 4, 'e_m': 0.312685, 'e_o_k': [0.243200, 0.194560], 'p_i': 10, 'u_i': 4.5666},
        {'id': 5, 'e_m': 0.597481, 'e_o_k': [0.464708, 0.371766], 'p_i': 20, 'u_i': 2.1776},
        {'id': 6, 'e_m': 2.081442, 'e_o_k': [1.618899, 1.295119], 'p_i': 10, 'u_i': 3.5354},
        {'id': 7, 'e_m': 4.826900, 'e_o_k': [3.754256, 3.003405], 'p_i': 80, 'u_i': 3.2835},
    ]
    B_BUDGET = 88.320010
    return processors, tasks, B_BUDGET
