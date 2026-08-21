"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439998, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439998, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.525860, 'e_o_k': [0.225416, 0.180333, 0.144266, 0.115413, 0.092330], 'p_i': 10, 'u_i': 4.7302},
        {'id': 1, 'e_m': 8.736485, 'e_o_k': [1.456081, 1.164865], 'p_i': 20, 'u_i': 1.8342},
        {'id': 2, 'e_m': 3.102752, 'e_o_k': [0.381486, 0.305189, 0.244151], 'p_i': 40, 'u_i': 2.1428},
        {'id': 3, 'e_m': 8.436613, 'e_o_k': [0.857379, 0.685904, 0.548723, 0.438978], 'p_i': 80, 'u_i': 3.7337},
        {'id': 4, 'e_m': 10.319267, 'e_o_k': [0.920925, 0.736740, 0.589392, 0.471513, 0.377211], 'p_i': 40, 'u_i': 3.4112},
        {'id': 5, 'e_m': 16.089105, 'e_o_k': [2.681518, 2.145214], 'p_i': 80, 'u_i': 2.7179},
        {'id': 6, 'e_m': 0.016657, 'e_o_k': [0.001693, 0.001354, 0.001083, 0.000867], 'p_i': 40, 'u_i': 2.6898},
        {'id': 7, 'e_m': 1.361027, 'e_o_k': [0.167339, 0.133871, 0.107097], 'p_i': 20, 'u_i': 4.5690},
    ]
    B_BUDGET = 167.439998
    return processors, tasks, B_BUDGET
