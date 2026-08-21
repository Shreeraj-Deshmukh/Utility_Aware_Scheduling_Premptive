"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.401182, 'e_o_k': [1.416485, 1.133188, 0.906550, 0.725240, 0.580192], 'p_i': 10, 'u_i': 2.1126},
        {'id': 1, 'e_m': 0.754885, 'e_o_k': [0.358008, 0.286406, 0.229125, 0.183300], 'p_i': 20, 'u_i': 1.1880},
        {'id': 2, 'e_m': 7.815327, 'e_o_k': [6.078588, 4.862870], 'p_i': 40, 'u_i': 4.0095},
        {'id': 3, 'e_m': 18.140351, 'e_o_k': [7.554882, 6.043906, 4.835124, 3.868100, 3.094480], 'p_i': 80, 'u_i': 4.5444},
    ]
    B_BUDGET = 176.640006
    return processors, tasks, B_BUDGET
