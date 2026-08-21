"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639994, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.639994, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.318061, 'e_o_k': [0.278303, 0.166982], 'p_i': 10, 'u_i': 1.8047},
        {'id': 1, 'e_m': 2.437651, 'e_o_k': [2.132945, 1.279767], 'p_i': 20, 'u_i': 1.0945},
        {'id': 2, 'e_m': 1.991584, 'e_o_k': [1.209324, 0.725594, 0.435357, 0.261214, 0.156728], 'p_i': 40, 'u_i': 2.4137},
        {'id': 3, 'e_m': 10.739727, 'e_o_k': [9.397261, 5.638356], 'p_i': 80, 'u_i': 1.6729},
        {'id': 4, 'e_m': 1.836977, 'e_o_k': [1.079051, 0.647431, 0.388458, 0.233075, 0.139845, 0.083907], 'p_i': 40, 'u_i': 2.8481},
        {'id': 5, 'e_m': 1.702926, 'e_o_k': [1.095632, 0.657379, 0.394428, 0.236657], 'p_i': 10, 'u_i': 3.6691},
        {'id': 6, 'e_m': 2.860437, 'e_o_k': [1.840355, 1.104213, 0.662528, 0.397517], 'p_i': 20, 'u_i': 3.0767},
        {'id': 7, 'e_m': 8.242902, 'e_o_k': [4.841930, 2.905158, 1.743095, 1.045857, 0.627514, 0.376509], 'p_i': 80, 'u_i': 1.7471},
    ]
    B_BUDGET = 176.639994
    return processors, tasks, B_BUDGET
