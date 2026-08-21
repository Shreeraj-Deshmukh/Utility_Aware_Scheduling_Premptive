"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.385802, 'e_o_k': [0.057384, 0.045907, 0.036726, 0.029380, 0.023504], 'p_i': 10, 'u_i': 4.5167},
        {'id': 1, 'e_m': 1.144116, 'e_o_k': [0.317810, 0.254248], 'p_i': 20, 'u_i': 2.0571},
        {'id': 2, 'e_m': 4.460307, 'e_o_k': [0.663420, 0.530736, 0.424589, 0.339671, 0.271737], 'p_i': 40, 'u_i': 3.7403},
        {'id': 3, 'e_m': 9.592694, 'e_o_k': [1.300077, 1.040061, 0.832049, 0.665639, 0.532511, 0.426009], 'p_i': 80, 'u_i': 1.1622},
        {'id': 4, 'e_m': 0.010312, 'e_o_k': [0.002113, 0.001690, 0.001352], 'p_i': 40, 'u_i': 4.1752},
        {'id': 5, 'e_m': 0.725399, 'e_o_k': [0.122866, 0.098293, 0.078634, 0.062907], 'p_i': 10, 'u_i': 1.9420},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
