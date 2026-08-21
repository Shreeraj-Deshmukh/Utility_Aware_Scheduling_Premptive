"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 20, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 20, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.361229, 'e_o_k': [0.090307, 0.090307], 'p_i': 10, 'u_i': 1.0216},
        {'id': 1, 'e_m': 1.543444, 'e_o_k': [0.257241, 0.257241, 0.257241], 'p_i': 20, 'u_i': 4.0085},
        {'id': 2, 'e_m': 5.606336, 'e_o_k': [0.934389, 0.934389, 0.934389], 'p_i': 40, 'u_i': 1.9931},
        {'id': 3, 'e_m': 2.233033, 'e_o_k': [0.372172, 0.372172, 0.372172], 'p_i': 80, 'u_i': 2.4773},
        {'id': 4, 'e_m': 0.084420, 'e_o_k': [0.010552, 0.010552, 0.010552, 0.010552], 'p_i': 80, 'u_i': 3.1022},
        {'id': 5, 'e_m': 0.994040, 'e_o_k': [0.082837, 0.082837, 0.082837, 0.082837, 0.082837, 0.082837], 'p_i': 40, 'u_i': 1.9821},
        {'id': 6, 'e_m': 3.955611, 'e_o_k': [0.659268, 0.659268, 0.659268], 'p_i': 80, 'u_i': 1.2190},
        {'id': 7, 'e_m': 3.462576, 'e_o_k': [0.432822, 0.432822, 0.432822, 0.432822], 'p_i': 80, 'u_i': 2.8489},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
