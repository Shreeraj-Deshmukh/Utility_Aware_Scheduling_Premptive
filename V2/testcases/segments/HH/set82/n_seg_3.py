"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640005, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640005, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.689807, 'e_o_k': [0.969561, 0.775649, 0.620519], 'p_i': 10, 'u_i': 3.8434},
        {'id': 1, 'e_m': 0.355169, 'e_o_k': [0.203786, 0.163029, 0.130423], 'p_i': 20, 'u_i': 3.7460},
        {'id': 2, 'e_m': 2.867086, 'e_o_k': [1.645050, 1.316040, 1.052832], 'p_i': 40, 'u_i': 2.3844},
        {'id': 3, 'e_m': 3.497724, 'e_o_k': [2.006891, 1.605513, 1.284410], 'p_i': 80, 'u_i': 3.6397},
        {'id': 4, 'e_m': 13.830064, 'e_o_k': [7.935283, 6.348226, 5.078581], 'p_i': 80, 'u_i': 2.3882},
        {'id': 5, 'e_m': 3.101531, 'e_o_k': [1.779567, 1.423653, 1.138923], 'p_i': 20, 'u_i': 4.1284},
        {'id': 6, 'e_m': 0.222281, 'e_o_k': [0.127538, 0.102031, 0.081625], 'p_i': 10, 'u_i': 3.5880},
        {'id': 7, 'e_m': 2.953634, 'e_o_k': [1.694708, 1.355766, 1.084613], 'p_i': 20, 'u_i': 3.2846},
    ]
    B_BUDGET = 176.640005
    return processors, tasks, B_BUDGET
