"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680001, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680001, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.318061, 'e_o_k': [0.053010, 0.042408], 'p_i': 10, 'u_i': 1.8047},
        {'id': 1, 'e_m': 2.437651, 'e_o_k': [0.406275, 0.325020], 'p_i': 20, 'u_i': 1.0945},
        {'id': 2, 'e_m': 1.991584, 'e_o_k': [0.177735, 0.142188, 0.113751, 0.091001, 0.072800], 'p_i': 40, 'u_i': 2.4137},
        {'id': 3, 'e_m': 10.739727, 'e_o_k': [1.789954, 1.431964], 'p_i': 80, 'u_i': 1.6729},
        {'id': 4, 'e_m': 1.836977, 'e_o_k': [0.149377, 0.119502, 0.095601, 0.076481, 0.061185, 0.048948], 'p_i': 40, 'u_i': 2.8481},
        {'id': 5, 'e_m': 1.702926, 'e_o_k': [0.173062, 0.138449, 0.110759, 0.088608], 'p_i': 10, 'u_i': 3.6691},
        {'id': 6, 'e_m': 2.860437, 'e_o_k': [0.290695, 0.232556, 0.186045, 0.148836], 'p_i': 20, 'u_i': 3.0767},
        {'id': 7, 'e_m': 8.242902, 'e_o_k': [0.670285, 0.536228, 0.428983, 0.343186, 0.274549, 0.219639], 'p_i': 80, 'u_i': 1.7471},
    ]
    B_BUDGET = 95.680001
    return processors, tasks, B_BUDGET
