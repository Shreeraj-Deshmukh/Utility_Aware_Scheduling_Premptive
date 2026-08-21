"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360008, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360008, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.808775, 'e_o_k': [0.099440, 0.079552, 0.063641], 'p_i': 10, 'u_i': 3.3502},
        {'id': 1, 'e_m': 0.001579, 'e_o_k': [0.000128, 0.000103, 0.000082, 0.000066, 0.000053, 0.000042], 'p_i': 20, 'u_i': 1.2795},
        {'id': 2, 'e_m': 2.887027, 'e_o_k': [0.354962, 0.283970, 0.227176], 'p_i': 40, 'u_i': 4.0968},
        {'id': 3, 'e_m': 19.809800, 'e_o_k': [3.301633, 2.641307], 'p_i': 80, 'u_i': 1.8773},
        {'id': 4, 'e_m': 15.403355, 'e_o_k': [1.565382, 1.252305, 1.001844, 0.801475], 'p_i': 40, 'u_i': 4.5380},
        {'id': 5, 'e_m': 2.803037, 'e_o_k': [0.227934, 0.182347, 0.145878, 0.116702, 0.093362, 0.074689], 'p_i': 80, 'u_i': 2.5931},
        {'id': 6, 'e_m': 17.320885, 'e_o_k': [2.886814, 2.309451], 'p_i': 40, 'u_i': 2.1006},
        {'id': 7, 'e_m': 27.688115, 'e_o_k': [2.251506, 1.801204, 1.440964, 1.152771, 0.922217, 0.737773], 'p_i': 80, 'u_i': 1.6702},
    ]
    B_BUDGET = 191.360008
    return processors, tasks, B_BUDGET
