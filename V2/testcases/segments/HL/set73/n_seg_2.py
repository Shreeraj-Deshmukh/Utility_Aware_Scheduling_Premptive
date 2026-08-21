"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.198341, 'e_o_k': [0.332872, 0.266298], 'p_i': 10, 'u_i': 3.9348},
        {'id': 1, 'e_m': 8.371318, 'e_o_k': [2.325366, 1.860293], 'p_i': 20, 'u_i': 2.2078},
        {'id': 2, 'e_m': 0.294500, 'e_o_k': [0.081805, 0.065444], 'p_i': 40, 'u_i': 1.5646},
        {'id': 3, 'e_m': 2.148895, 'e_o_k': [0.596915, 0.477532], 'p_i': 80, 'u_i': 4.4075},
        {'id': 4, 'e_m': 0.418546, 'e_o_k': [0.116263, 0.093010], 'p_i': 10, 'u_i': 2.2030},
        {'id': 5, 'e_m': 0.283932, 'e_o_k': [0.078870, 0.063096], 'p_i': 80, 'u_i': 2.4770},
        {'id': 6, 'e_m': 0.627393, 'e_o_k': [0.174276, 0.139421], 'p_i': 80, 'u_i': 4.3612},
        {'id': 7, 'e_m': 3.482604, 'e_o_k': [0.967390, 0.773912], 'p_i': 20, 'u_i': 4.6337},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
