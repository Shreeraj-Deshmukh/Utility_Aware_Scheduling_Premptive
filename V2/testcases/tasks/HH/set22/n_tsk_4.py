"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.922344, 'e_o_k': [1.633532, 1.306826, 1.045461, 0.836369, 0.669095], 'p_i': 10, 'u_i': 3.1771},
        {'id': 1, 'e_m': 0.290131, 'e_o_k': [0.225657, 0.180526], 'p_i': 20, 'u_i': 3.8810},
        {'id': 2, 'e_m': 10.050027, 'e_o_k': [4.766273, 3.813018, 3.050415, 2.440332], 'p_i': 40, 'u_i': 1.9496},
        {'id': 3, 'e_m': 11.360669, 'e_o_k': [8.836076, 7.068861], 'p_i': 80, 'u_i': 4.0364},
    ]
    B_BUDGET = 176.640009
    return processors, tasks, B_BUDGET
