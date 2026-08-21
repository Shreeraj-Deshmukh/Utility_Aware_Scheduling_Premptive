"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599991, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599991, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.274300, 'e_o_k': [0.033725, 0.026980, 0.021584], 'p_i': 10, 'u_i': 1.2368},
        {'id': 1, 'e_m': 1.431697, 'e_o_k': [0.116421, 0.093137, 0.074509, 0.059607, 0.047686, 0.038149], 'p_i': 20, 'u_i': 2.8306},
        {'id': 2, 'e_m': 14.077157, 'e_o_k': [1.730798, 1.384638, 1.107711], 'p_i': 40, 'u_i': 2.9234},
        {'id': 3, 'e_m': 9.288103, 'e_o_k': [1.141980, 0.913584, 0.730867], 'p_i': 80, 'u_i': 3.7707},
        {'id': 4, 'e_m': 3.328903, 'e_o_k': [0.409291, 0.327433, 0.261946], 'p_i': 20, 'u_i': 1.9627},
        {'id': 5, 'e_m': 4.089226, 'e_o_k': [0.681538, 0.545230], 'p_i': 40, 'u_i': 4.9296},
        {'id': 6, 'e_m': 0.035472, 'e_o_k': [0.002884, 0.002308, 0.001846, 0.001477, 0.001181, 0.000945], 'p_i': 40, 'u_i': 4.5772},
        {'id': 7, 'e_m': 1.633924, 'e_o_k': [0.145817, 0.116653, 0.093323, 0.074658, 0.059726], 'p_i': 10, 'u_i': 4.4816},
    ]
    B_BUDGET = 119.599991
    return processors, tasks, B_BUDGET
