"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.28, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.28, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.847666, 'e_o_k': [0.227172, 0.181738, 0.145390], 'p_i': 10, 'u_i': 4.1932},
        {'id': 1, 'e_m': 2.514710, 'e_o_k': [0.419118, 0.335295], 'p_i': 20, 'u_i': 2.7154},
        {'id': 2, 'e_m': 1.426415, 'e_o_k': [0.175379, 0.140303, 0.112243], 'p_i': 40, 'u_i': 4.3253},
        {'id': 3, 'e_m': 30.636015, 'e_o_k': [3.113416, 2.490733, 1.992586, 1.594069], 'p_i': 80, 'u_i': 1.0005},
        {'id': 4, 'e_m': 7.320213, 'e_o_k': [0.653279, 0.522624, 0.418099, 0.334479, 0.267583], 'p_i': 80, 'u_i': 1.9051},
        {'id': 5, 'e_m': 5.493430, 'e_o_k': [0.490251, 0.392201, 0.313761, 0.251009, 0.200807], 'p_i': 20, 'u_i': 2.2450},
        {'id': 6, 'e_m': 15.859748, 'e_o_k': [2.643291, 2.114633], 'p_i': 40, 'u_i': 3.5907},
        {'id': 7, 'e_m': 12.328779, 'e_o_k': [1.515833, 1.212667, 0.970133], 'p_i': 40, 'u_i': 4.3441},
    ]
    B_BUDGET = 215.280000
    return processors, tasks, B_BUDGET
