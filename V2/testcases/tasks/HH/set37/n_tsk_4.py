"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.492663, 'e_o_k': [3.494294, 2.795435], 'p_i': 10, 'u_i': 1.0738},
        {'id': 1, 'e_m': 1.261030, 'e_o_k': [0.598050, 0.478440, 0.382752, 0.306201], 'p_i': 20, 'u_i': 3.3187},
        {'id': 2, 'e_m': 3.885238, 'e_o_k': [2.229235, 1.783388, 1.426710], 'p_i': 40, 'u_i': 4.5515},
        {'id': 3, 'e_m': 15.244097, 'e_o_k': [11.856520, 9.485216], 'p_i': 80, 'u_i': 3.0521},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
