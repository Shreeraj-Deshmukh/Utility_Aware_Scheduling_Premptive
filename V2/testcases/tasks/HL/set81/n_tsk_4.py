"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.759875, 'e_o_k': [0.488854, 0.391083], 'p_i': 10, 'u_i': 3.3070},
        {'id': 1, 'e_m': 5.661111, 'e_o_k': [0.842026, 0.673621, 0.538897, 0.431117, 0.344894], 'p_i': 20, 'u_i': 4.6500},
        {'id': 2, 'e_m': 6.801565, 'e_o_k': [1.152027, 0.921621, 0.737297, 0.589838], 'p_i': 40, 'u_i': 2.3899},
        {'id': 3, 'e_m': 13.673430, 'e_o_k': [2.801932, 2.241546, 1.793237], 'p_i': 80, 'u_i': 1.6802},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
