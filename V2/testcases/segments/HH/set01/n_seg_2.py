"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640007, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640007, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.255642, 'e_o_k': [0.198833, 0.159066], 'p_i': 10, 'u_i': 1.1226},
        {'id': 1, 'e_m': 5.834936, 'e_o_k': [4.538283, 3.630627], 'p_i': 20, 'u_i': 3.8598},
        {'id': 2, 'e_m': 1.030030, 'e_o_k': [0.801134, 0.640907], 'p_i': 40, 'u_i': 4.6365},
        {'id': 3, 'e_m': 1.325038, 'e_o_k': [1.030585, 0.824468], 'p_i': 80, 'u_i': 1.0760},
        {'id': 4, 'e_m': 19.367876, 'e_o_k': [15.063903, 12.051123], 'p_i': 80, 'u_i': 3.5452},
        {'id': 5, 'e_m': 0.396585, 'e_o_k': [0.308455, 0.246764], 'p_i': 40, 'u_i': 3.7479},
        {'id': 6, 'e_m': 3.226328, 'e_o_k': [2.509366, 2.007493], 'p_i': 80, 'u_i': 4.4508},
        {'id': 7, 'e_m': 2.960663, 'e_o_k': [2.302738, 1.842190], 'p_i': 20, 'u_i': 2.7382},
    ]
    B_BUDGET = 176.640007
    return processors, tasks, B_BUDGET
