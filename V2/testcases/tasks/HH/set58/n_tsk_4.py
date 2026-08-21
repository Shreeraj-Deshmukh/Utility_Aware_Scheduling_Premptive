"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.635145, 'e_o_k': [0.999979, 0.799983, 0.639987, 0.511989, 0.409591, 0.327673], 'p_i': 10, 'u_i': 3.8653},
        {'id': 1, 'e_m': 6.890535, 'e_o_k': [3.953586, 3.162869, 2.530295], 'p_i': 20, 'u_i': 1.8068},
        {'id': 2, 'e_m': 1.050998, 'e_o_k': [0.817443, 0.653954], 'p_i': 40, 'u_i': 1.4573},
        {'id': 3, 'e_m': 13.254707, 'e_o_k': [5.520166, 4.416133, 3.532906, 2.826325, 2.261060], 'p_i': 80, 'u_i': 1.2598},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
