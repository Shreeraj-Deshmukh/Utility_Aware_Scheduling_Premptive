"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319985, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319985, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.280173, 'e_o_k': [1.081383, 0.865106, 0.692085, 0.553668], 'p_i': 10, 'u_i': 1.8147},
        {'id': 1, 'e_m': 0.059600, 'e_o_k': [0.028265, 0.022612, 0.018090, 0.014472], 'p_i': 20, 'u_i': 2.7697},
        {'id': 2, 'e_m': 2.975935, 'e_o_k': [1.129301, 0.903441, 0.722753, 0.578202, 0.462562, 0.370050], 'p_i': 40, 'u_i': 2.4720},
        {'id': 3, 'e_m': 1.390599, 'e_o_k': [1.081577, 0.865262], 'p_i': 80, 'u_i': 3.3220},
        {'id': 4, 'e_m': 4.200429, 'e_o_k': [3.267000, 2.613600], 'p_i': 80, 'u_i': 2.5309},
        {'id': 5, 'e_m': 0.494329, 'e_o_k': [0.283631, 0.226905, 0.181524], 'p_i': 20, 'u_i': 3.7128},
    ]
    B_BUDGET = 88.319985
    return processors, tasks, B_BUDGET
