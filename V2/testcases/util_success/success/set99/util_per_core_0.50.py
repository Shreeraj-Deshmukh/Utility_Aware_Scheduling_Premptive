"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600002, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600002, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.213286, 'e_o_k': [0.108278, 0.086622, 0.069298, 0.055438, 0.044350], 'p_i': 10, 'u_i': 1.8657},
        {'id': 1, 'e_m': 3.653764, 'e_o_k': [0.326074, 0.260859, 0.208687, 0.166950, 0.133560], 'p_i': 20, 'u_i': 1.6547},
        {'id': 2, 'e_m': 1.387379, 'e_o_k': [0.140994, 0.112795, 0.090236, 0.072189], 'p_i': 40, 'u_i': 3.2690},
        {'id': 3, 'e_m': 4.560766, 'e_o_k': [0.560750, 0.448600, 0.358880], 'p_i': 80, 'u_i': 2.0883},
        {'id': 4, 'e_m': 1.293894, 'e_o_k': [0.159085, 0.127268, 0.101815], 'p_i': 10, 'u_i': 2.4453},
        {'id': 5, 'e_m': 12.656523, 'e_o_k': [1.129509, 0.903607, 0.722886, 0.578309, 0.462647], 'p_i': 40, 'u_i': 4.4841},
        {'id': 6, 'e_m': 6.114852, 'e_o_k': [0.751826, 0.601461, 0.481169], 'p_i': 40, 'u_i': 2.2759},
        {'id': 7, 'e_m': 0.449226, 'e_o_k': [0.074871, 0.059897], 'p_i': 80, 'u_i': 4.2544},
    ]
    B_BUDGET = 119.600002
    return processors, tasks, B_BUDGET
