"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.328551, 'e_o_k': [1.386236, 1.108989, 0.887191, 0.709753, 0.567802], 'p_i': 10, 'u_i': 4.0082},
        {'id': 1, 'e_m': 0.075464, 'e_o_k': [0.028637, 0.022909, 0.018328, 0.014662, 0.011730, 0.009384], 'p_i': 20, 'u_i': 3.2625},
        {'id': 2, 'e_m': 8.498214, 'e_o_k': [4.876024, 3.900819, 3.120655], 'p_i': 40, 'u_i': 3.4071},
        {'id': 3, 'e_m': 20.073309, 'e_o_k': [8.359898, 6.687918, 5.350335, 4.280268, 3.424214], 'p_i': 80, 'u_i': 2.2919},
    ]
    B_BUDGET = 176.639998
    return processors, tasks, B_BUDGET
