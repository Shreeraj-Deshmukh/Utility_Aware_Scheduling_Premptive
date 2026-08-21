"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639998, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639998, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.206954, 'e_o_k': [0.919127, 0.735301, 0.588241, 0.470593, 0.376474], 'p_i': 10, 'u_i': 2.2919},
        {'id': 1, 'e_m': 0.046886, 'e_o_k': [0.017792, 0.014234, 0.011387, 0.009110, 0.007288, 0.005830], 'p_i': 20, 'u_i': 3.9772},
        {'id': 2, 'e_m': 4.267678, 'e_o_k': [2.023966, 1.619173, 1.295338, 1.036271], 'p_i': 40, 'u_i': 1.4627},
        {'id': 3, 'e_m': 2.726716, 'e_o_k': [2.120779, 1.696623], 'p_i': 80, 'u_i': 4.5040},
        {'id': 4, 'e_m': 2.163074, 'e_o_k': [1.241108, 0.992886, 0.794309], 'p_i': 20, 'u_i': 4.7123},
        {'id': 5, 'e_m': 13.121227, 'e_o_k': [5.464576, 4.371661, 3.497329, 2.797863, 2.238290], 'p_i': 40, 'u_i': 4.3702},
    ]
    B_BUDGET = 176.639998
    return processors, tasks, B_BUDGET
