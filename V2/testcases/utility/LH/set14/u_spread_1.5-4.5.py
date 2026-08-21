"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320001, "H": 80, "J": 20, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 88.320001, "H": 80, "J": 20, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.361229, 'e_o_k': [0.280956, 0.224765], 'p_i': 10, 'u_i': 1.5162},
        {'id': 1, 'e_m': 1.543444, 'e_o_k': [0.885583, 0.708466, 0.566773], 'p_i': 20, 'u_i': 3.7564},
        {'id': 2, 'e_m': 5.606336, 'e_o_k': [3.216750, 2.573400, 2.058720], 'p_i': 40, 'u_i': 2.2448},
        {'id': 3, 'e_m': 2.233033, 'e_o_k': [1.281248, 1.024999, 0.819999], 'p_i': 80, 'u_i': 2.6080},
        {'id': 4, 'e_m': 0.084420, 'e_o_k': [0.040036, 0.032029, 0.025623, 0.020499], 'p_i': 80, 'u_i': 3.0767},
        {'id': 5, 'e_m': 0.994040, 'e_o_k': [0.377216, 0.301773, 0.241418, 0.193135, 0.154508, 0.123606], 'p_i': 40, 'u_i': 2.2366},
        {'id': 6, 'e_m': 3.955611, 'e_o_k': [2.269613, 1.815690, 1.452552], 'p_i': 80, 'u_i': 1.6643},
        {'id': 7, 'e_m': 3.462576, 'e_o_k': [1.642143, 1.313714, 1.050971, 0.840777], 'p_i': 80, 'u_i': 2.8867},
    ]
    B_BUDGET = 88.320001
    return processors, tasks, B_BUDGET
