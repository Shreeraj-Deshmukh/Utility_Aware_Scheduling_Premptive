"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640007, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640007, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.727022, 'e_o_k': [1.135718, 0.908575, 0.726860, 0.581488, 0.465190], 'p_i': 10, 'u_i': 4.2653},
        {'id': 1, 'e_m': 0.448204, 'e_o_k': [0.170083, 0.136067, 0.108853, 0.087083, 0.069666, 0.055733], 'p_i': 20, 'u_i': 3.8195},
        {'id': 2, 'e_m': 17.274833, 'e_o_k': [6.555416, 5.244333, 4.195467, 3.356373, 2.685099, 2.148079], 'p_i': 40, 'u_i': 1.2105},
        {'id': 3, 'e_m': 1.336713, 'e_o_k': [0.766967, 0.613573, 0.490859], 'p_i': 80, 'u_i': 1.7971},
        {'id': 4, 'e_m': 0.367997, 'e_o_k': [0.211146, 0.168917, 0.135133], 'p_i': 20, 'u_i': 3.9776},
        {'id': 5, 'e_m': 1.516321, 'e_o_k': [0.631500, 0.505200, 0.404160, 0.323328, 0.258662], 'p_i': 40, 'u_i': 2.5595},
    ]
    B_BUDGET = 176.640007
    return processors, tasks, B_BUDGET
