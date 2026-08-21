"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519999, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519999, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.429660, 'e_o_k': [0.348543, 0.278834, 0.223067, 0.178454], 'p_i': 10, 'u_i': 1.7025},
        {'id': 1, 'e_m': 2.164861, 'e_o_k': [0.193199, 0.154559, 0.123647, 0.098918, 0.079134], 'p_i': 20, 'u_i': 2.0058},
        {'id': 2, 'e_m': 1.683645, 'e_o_k': [0.280608, 0.224486], 'p_i': 40, 'u_i': 3.5722},
        {'id': 3, 'e_m': 29.721415, 'e_o_k': [3.020469, 2.416375, 1.933100, 1.546480], 'p_i': 80, 'u_i': 1.2384},
        {'id': 4, 'e_m': 2.774700, 'e_o_k': [0.462450, 0.369960], 'p_i': 40, 'u_i': 4.5379},
        {'id': 5, 'e_m': 3.934146, 'e_o_k': [0.655691, 0.524553], 'p_i': 20, 'u_i': 1.9982},
        {'id': 6, 'e_m': 0.458277, 'e_o_k': [0.076380, 0.061104], 'p_i': 20, 'u_i': 2.1252},
        {'id': 7, 'e_m': 3.695479, 'e_o_k': [0.375557, 0.300445, 0.240356, 0.192285], 'p_i': 80, 'u_i': 4.2384},
    ]
    B_BUDGET = 143.519999
    return processors, tasks, B_BUDGET
