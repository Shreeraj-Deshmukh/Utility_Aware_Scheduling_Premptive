"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400009, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400009, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.799476, 'e_o_k': [0.777632, 0.622106], 'p_i': 10, 'u_i': 4.3165},
        {'id': 1, 'e_m': 2.384351, 'e_o_k': [0.662320, 0.529856], 'p_i': 20, 'u_i': 4.1600},
        {'id': 2, 'e_m': 1.700493, 'e_o_k': [0.252929, 0.202343, 0.161875, 0.129500, 0.103600], 'p_i': 40, 'u_i': 2.4258},
        {'id': 3, 'e_m': 2.594088, 'e_o_k': [0.439378, 0.351503, 0.281202, 0.224962], 'p_i': 80, 'u_i': 2.6711},
        {'id': 4, 'e_m': 25.043045, 'e_o_k': [3.394029, 2.715223, 2.172178, 1.737743, 1.390194, 1.112155], 'p_i': 80, 'u_i': 3.0914},
        {'id': 5, 'e_m': 0.128584, 'e_o_k': [0.021779, 0.017423, 0.013939, 0.011151], 'p_i': 10, 'u_i': 2.6989},
    ]
    B_BUDGET = 110.400009
    return processors, tasks, B_BUDGET
