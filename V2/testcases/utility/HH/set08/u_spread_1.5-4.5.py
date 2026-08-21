"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 37, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 37, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.713852, 'e_o_k': [0.270891, 0.216713, 0.173370, 0.138696, 0.110957, 0.088766], 'p_i': 10, 'u_i': 3.8729},
        {'id': 1, 'e_m': 0.102835, 'e_o_k': [0.048770, 0.039016, 0.031213, 0.024970], 'p_i': 20, 'u_i': 2.2736},
        {'id': 2, 'e_m': 5.612205, 'e_o_k': [2.337306, 1.869845, 1.495876, 1.196701, 0.957360], 'p_i': 40, 'u_i': 1.9403},
        {'id': 3, 'e_m': 3.855748, 'e_o_k': [2.998915, 2.399132], 'p_i': 80, 'u_i': 2.1533},
        {'id': 4, 'e_m': 0.273644, 'e_o_k': [0.212834, 0.170267], 'p_i': 20, 'u_i': 4.4654},
        {'id': 5, 'e_m': 4.043450, 'e_o_k': [1.683969, 1.347175, 1.077740, 0.862192, 0.689754], 'p_i': 10, 'u_i': 2.5496},
        {'id': 6, 'e_m': 1.584227, 'e_o_k': [1.232177, 0.985741], 'p_i': 40, 'u_i': 1.9428},
        {'id': 7, 'e_m': 0.773382, 'e_o_k': [0.443744, 0.354995, 0.283996], 'p_i': 10, 'u_i': 2.6170},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
