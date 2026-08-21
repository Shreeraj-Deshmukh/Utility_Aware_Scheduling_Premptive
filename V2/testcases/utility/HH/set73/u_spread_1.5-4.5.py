"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639984, "H": 80, "J": 29, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 176.639984, "H": 80, "J": 29, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.198341, 'e_o_k': [0.687573, 0.550058, 0.440046], 'p_i': 10, 'u_i': 3.7011},
        {'id': 1, 'e_m': 8.371318, 'e_o_k': [6.511025, 5.208820], 'p_i': 20, 'u_i': 2.4058},
        {'id': 2, 'e_m': 0.294500, 'e_o_k': [0.139668, 0.111734, 0.089387, 0.071510], 'p_i': 40, 'u_i': 1.9234},
        {'id': 3, 'e_m': 2.148895, 'e_o_k': [1.671363, 1.337090], 'p_i': 80, 'u_i': 4.0556},
        {'id': 4, 'e_m': 0.418546, 'e_o_k': [0.325535, 0.260428], 'p_i': 10, 'u_i': 2.4023},
        {'id': 5, 'e_m': 0.283932, 'e_o_k': [0.162912, 0.130329, 0.104264], 'p_i': 80, 'u_i': 2.6077},
        {'id': 6, 'e_m': 0.627393, 'e_o_k': [0.238082, 0.190465, 0.152372, 0.121898, 0.097518, 0.078015], 'p_i': 80, 'u_i': 2.2203},
        {'id': 7, 'e_m': 3.482604, 'e_o_k': [1.651641, 1.321313, 1.057050, 0.845640], 'p_i': 20, 'u_i': 2.6221},
    ]
    B_BUDGET = 176.639984
    return processors, tasks, B_BUDGET
