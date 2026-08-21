"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.030044, 'e_o_k': [0.286123, 0.228899], 'p_i': 10, 'u_i': 3.7892},
        {'id': 1, 'e_m': 0.169513, 'e_o_k': [0.047087, 0.037670], 'p_i': 20, 'u_i': 2.5683},
        {'id': 2, 'e_m': 7.923597, 'e_o_k': [2.200999, 1.760799], 'p_i': 40, 'u_i': 1.2577},
        {'id': 3, 'e_m': 0.881446, 'e_o_k': [0.244846, 0.195877], 'p_i': 80, 'u_i': 3.4086},
        {'id': 4, 'e_m': 0.392495, 'e_o_k': [0.109026, 0.087221], 'p_i': 40, 'u_i': 3.2935},
        {'id': 5, 'e_m': 0.407213, 'e_o_k': [0.113115, 0.090492], 'p_i': 10, 'u_i': 4.9988},
        {'id': 6, 'e_m': 0.082726, 'e_o_k': [0.022980, 0.018384], 'p_i': 20, 'u_i': 2.8879},
        {'id': 7, 'e_m': 0.494838, 'e_o_k': [0.137455, 0.109964], 'p_i': 20, 'u_i': 4.7528},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
