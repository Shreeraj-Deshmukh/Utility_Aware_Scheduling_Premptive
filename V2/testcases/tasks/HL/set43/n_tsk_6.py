"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.072203, 'e_o_k': [0.014796, 0.011837, 0.009469], 'p_i': 10, 'u_i': 4.0506},
        {'id': 1, 'e_m': 3.542872, 'e_o_k': [0.725998, 0.580799, 0.464639], 'p_i': 20, 'u_i': 2.8657},
        {'id': 2, 'e_m': 5.455722, 'e_o_k': [0.924072, 0.739258, 0.591406, 0.473125], 'p_i': 40, 'u_i': 2.1758},
        {'id': 3, 'e_m': 6.580644, 'e_o_k': [1.827957, 1.462365], 'p_i': 80, 'u_i': 2.5351},
        {'id': 4, 'e_m': 1.686436, 'e_o_k': [0.285643, 0.228514, 0.182812, 0.146249], 'p_i': 40, 'u_i': 3.6072},
        {'id': 5, 'e_m': 14.192964, 'e_o_k': [1.923541, 1.538833, 1.231066, 0.984853, 0.787882, 0.630306], 'p_i': 40, 'u_i': 4.5999},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET
