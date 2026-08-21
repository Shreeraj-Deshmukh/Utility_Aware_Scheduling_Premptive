"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.380368, 'e_o_k': [0.903297, 0.722638, 0.578110, 0.462488, 0.369990, 0.295992], 'p_i': 10, 'u_i': 2.2901},
        {'id': 1, 'e_m': 5.865049, 'e_o_k': [4.561705, 3.649364], 'p_i': 20, 'u_i': 4.0645},
        {'id': 2, 'e_m': 10.615229, 'e_o_k': [4.028244, 3.222595, 2.578076, 2.062461, 1.649969, 1.319975], 'p_i': 40, 'u_i': 4.5754},
        {'id': 3, 'e_m': 0.266399, 'e_o_k': [0.126341, 0.101073, 0.080858, 0.064687], 'p_i': 80, 'u_i': 3.5388},
    ]
    B_BUDGET = 176.639991
    return processors, tasks, B_BUDGET
