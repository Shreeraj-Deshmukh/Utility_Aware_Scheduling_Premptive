"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199987, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199987, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.597822, 'e_o_k': [0.166062, 0.132849], 'p_i': 10, 'u_i': 1.3138},
        {'id': 1, 'e_m': 0.537328, 'e_o_k': [0.149258, 0.119406], 'p_i': 20, 'u_i': 3.5906},
        {'id': 2, 'e_m': 1.853768, 'e_o_k': [0.514935, 0.411948], 'p_i': 40, 'u_i': 2.7107},
        {'id': 3, 'e_m': 4.965351, 'e_o_k': [1.379264, 1.103411], 'p_i': 80, 'u_i': 4.0673},
        {'id': 4, 'e_m': 0.125857, 'e_o_k': [0.034960, 0.027968], 'p_i': 10, 'u_i': 2.2713},
        {'id': 5, 'e_m': 0.986987, 'e_o_k': [0.274163, 0.219330], 'p_i': 80, 'u_i': 2.2740},
        {'id': 6, 'e_m': 11.937053, 'e_o_k': [3.315848, 2.652678], 'p_i': 80, 'u_i': 2.9164},
        {'id': 7, 'e_m': 1.232163, 'e_o_k': [0.342268, 0.273814], 'p_i': 40, 'u_i': 4.5766},
    ]
    B_BUDGET = 55.199987
    return processors, tasks, B_BUDGET
