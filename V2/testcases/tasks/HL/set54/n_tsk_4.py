"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.006381, 'e_o_k': [0.542976, 0.434381, 0.347505, 0.278004, 0.222403, 0.177922], 'p_i': 10, 'u_i': 3.2200},
        {'id': 1, 'e_m': 0.664489, 'e_o_k': [0.136166, 0.108933, 0.087146], 'p_i': 20, 'u_i': 1.6886},
        {'id': 2, 'e_m': 14.601198, 'e_o_k': [2.171763, 1.737411, 1.389928, 1.111943, 0.889554], 'p_i': 40, 'u_i': 4.2653},
        {'id': 3, 'e_m': 0.088597, 'e_o_k': [0.012007, 0.009606, 0.007685, 0.006148, 0.004918, 0.003935], 'p_i': 80, 'u_i': 3.8195},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET
