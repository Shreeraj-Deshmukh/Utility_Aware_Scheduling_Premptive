"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119994, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119994, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.775727, 'e_o_k': [0.587180, 0.469744, 0.375795], 'p_i': 10, 'u_i': 1.8133},
        {'id': 1, 'e_m': 2.929652, 'e_o_k': [0.297729, 0.238183, 0.190546, 0.152437], 'p_i': 20, 'u_i': 3.3241},
        {'id': 2, 'e_m': 12.685208, 'e_o_k': [1.289147, 1.031318, 0.825054, 0.660043], 'p_i': 40, 'u_i': 2.4878},
        {'id': 3, 'e_m': 22.615322, 'e_o_k': [1.839003, 1.471202, 1.176962, 0.941569, 0.753256, 0.602604], 'p_i': 80, 'u_i': 1.5486},
        {'id': 4, 'e_m': 1.632672, 'e_o_k': [0.165922, 0.132738, 0.106190, 0.084952], 'p_i': 40, 'u_i': 2.4086},
        {'id': 5, 'e_m': 15.845028, 'e_o_k': [1.414061, 1.131249, 0.904999, 0.723999, 0.579199], 'p_i': 40, 'u_i': 1.3599},
        {'id': 6, 'e_m': 3.815480, 'e_o_k': [0.469116, 0.375293, 0.300235], 'p_i': 10, 'u_i': 3.1633},
        {'id': 7, 'e_m': 12.610593, 'e_o_k': [1.125410, 0.900328, 0.720262, 0.576210, 0.460968], 'p_i': 80, 'u_i': 3.3362},
    ]
    B_BUDGET = 263.119994
    return processors, tasks, B_BUDGET
