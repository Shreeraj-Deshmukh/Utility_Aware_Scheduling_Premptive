"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760008, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760008, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.446094, 'e_o_k': [0.248587, 0.198869, 0.159096, 0.127276], 'p_i': 10, 'u_i': 2.1780},
        {'id': 1, 'e_m': 0.831669, 'e_o_k': [0.102254, 0.081804, 0.065443], 'p_i': 20, 'u_i': 3.8388},
        {'id': 2, 'e_m': 2.165892, 'e_o_k': [0.220111, 0.176089, 0.140871, 0.112697], 'p_i': 40, 'u_i': 1.0041},
        {'id': 3, 'e_m': 5.873951, 'e_o_k': [0.978992, 0.783194], 'p_i': 80, 'u_i': 4.1994},
        {'id': 4, 'e_m': 1.250505, 'e_o_k': [0.101687, 0.081350, 0.065080, 0.052064, 0.041651, 0.033321], 'p_i': 40, 'u_i': 2.8402},
        {'id': 5, 'e_m': 0.551236, 'e_o_k': [0.044825, 0.035860, 0.028688, 0.022950, 0.018360, 0.014688], 'p_i': 10, 'u_i': 1.6917},
        {'id': 6, 'e_m': 0.277880, 'e_o_k': [0.024799, 0.019839, 0.015871, 0.012697, 0.010158], 'p_i': 10, 'u_i': 1.6028},
        {'id': 7, 'e_m': 5.764900, 'e_o_k': [0.708799, 0.567039, 0.453632], 'p_i': 80, 'u_i': 2.5090},
    ]
    B_BUDGET = 71.760008
    return processors, tasks, B_BUDGET
