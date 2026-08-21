"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280005, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280005, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.614575, 'e_o_k': [0.269096, 0.215277], 'p_i': 10, 'u_i': 2.0470},
        {'id': 1, 'e_m': 1.445813, 'e_o_k': [0.146932, 0.117546, 0.094037, 0.075229], 'p_i': 20, 'u_i': 4.9556},
        {'id': 2, 'e_m': 13.115851, 'e_o_k': [2.185975, 1.748780], 'p_i': 40, 'u_i': 1.3741},
        {'id': 3, 'e_m': 37.298972, 'e_o_k': [3.328680, 2.662944, 2.130355, 1.704284, 1.363427], 'p_i': 80, 'u_i': 4.6107},
        {'id': 4, 'e_m': 18.128572, 'e_o_k': [1.617852, 1.294282, 1.035425, 0.828340, 0.662672], 'p_i': 40, 'u_i': 2.5105},
        {'id': 5, 'e_m': 0.210220, 'e_o_k': [0.021364, 0.017091, 0.013673, 0.010938], 'p_i': 10, 'u_i': 2.2972},
        {'id': 6, 'e_m': 8.251357, 'e_o_k': [1.375226, 1.100181], 'p_i': 40, 'u_i': 3.0996},
        {'id': 7, 'e_m': 0.915982, 'e_o_k': [0.081745, 0.065396, 0.052317, 0.041854, 0.033483], 'p_i': 10, 'u_i': 4.5299},
    ]
    B_BUDGET = 215.280005
    return processors, tasks, B_BUDGET
