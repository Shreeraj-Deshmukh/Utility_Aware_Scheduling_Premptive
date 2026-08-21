"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640013, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640013, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.617360, 'e_o_k': [0.257111, 0.205689, 0.164551, 0.131641, 0.105313], 'p_i': 10, 'u_i': 4.1247},
        {'id': 1, 'e_m': 5.349248, 'e_o_k': [3.069241, 2.455393, 1.964314], 'p_i': 20, 'u_i': 3.4312},
        {'id': 2, 'e_m': 11.779971, 'e_o_k': [9.162200, 7.329760], 'p_i': 40, 'u_i': 1.1226},
        {'id': 3, 'e_m': 14.104185, 'e_o_k': [5.873947, 4.699157, 3.759326, 3.007461, 2.405969], 'p_i': 80, 'u_i': 3.8598},
    ]
    B_BUDGET = 176.640013
    return processors, tasks, B_BUDGET
