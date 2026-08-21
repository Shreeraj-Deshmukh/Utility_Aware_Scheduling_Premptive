"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.40001, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.40001, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.060089, 'e_o_k': [0.422149, 0.337719, 0.270176], 'p_i': 10, 'u_i': 3.7892},
        {'id': 1, 'e_m': 0.339026, 'e_o_k': [0.069473, 0.055578, 0.044462], 'p_i': 20, 'u_i': 2.5683},
        {'id': 2, 'e_m': 15.847193, 'e_o_k': [3.247376, 2.597901, 2.078320], 'p_i': 40, 'u_i': 1.2577},
        {'id': 3, 'e_m': 1.762893, 'e_o_k': [0.361248, 0.288999, 0.231199], 'p_i': 80, 'u_i': 3.4086},
        {'id': 4, 'e_m': 0.784991, 'e_o_k': [0.160859, 0.128687, 0.102950], 'p_i': 40, 'u_i': 3.2935},
        {'id': 5, 'e_m': 0.814426, 'e_o_k': [0.166891, 0.133513, 0.106810], 'p_i': 10, 'u_i': 4.9988},
        {'id': 6, 'e_m': 0.165452, 'e_o_k': [0.033904, 0.027123, 0.021699], 'p_i': 20, 'u_i': 2.8879},
        {'id': 7, 'e_m': 0.989677, 'e_o_k': [0.202803, 0.162242, 0.129794], 'p_i': 20, 'u_i': 4.7528},
    ]
    B_BUDGET = 110.400010
    return processors, tasks, B_BUDGET
