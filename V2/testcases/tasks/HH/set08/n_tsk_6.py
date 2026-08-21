"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640005, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640005, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.981227, 'e_o_k': [0.372354, 0.297883, 0.238306, 0.190645, 0.152516, 0.122013], 'p_i': 10, 'u_i': 4.9438},
        {'id': 1, 'e_m': 0.148329, 'e_o_k': [0.056288, 0.045030, 0.036024, 0.028819, 0.023055, 0.018444], 'p_i': 20, 'u_i': 2.3791},
        {'id': 2, 'e_m': 8.384770, 'e_o_k': [6.521488, 5.217190], 'p_i': 40, 'u_i': 3.1569},
        {'id': 3, 'e_m': 6.146347, 'e_o_k': [2.914934, 2.331947, 1.865558, 1.492446], 'p_i': 80, 'u_i': 2.0315},
        {'id': 4, 'e_m': 0.305116, 'e_o_k': [0.127071, 0.101657, 0.081326, 0.065060, 0.052048], 'p_i': 10, 'u_i': 1.5871},
        {'id': 5, 'e_m': 7.550015, 'e_o_k': [5.872234, 4.697787], 'p_i': 20, 'u_i': 1.8711},
    ]
    B_BUDGET = 176.640005
    return processors, tasks, B_BUDGET
