"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639993, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639993, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.602748, 'e_o_k': [0.345839, 0.276671, 0.221337], 'p_i': 10, 'u_i': 4.0696},
        {'id': 1, 'e_m': 5.070740, 'e_o_k': [3.943909, 3.155127], 'p_i': 20, 'u_i': 1.5844},
        {'id': 2, 'e_m': 2.297287, 'e_o_k': [1.786778, 1.429423], 'p_i': 40, 'u_i': 4.9877},
        {'id': 3, 'e_m': 26.256921, 'e_o_k': [20.422050, 16.337640], 'p_i': 80, 'u_i': 3.4936},
        {'id': 4, 'e_m': 0.797956, 'e_o_k': [0.378435, 0.302748, 0.242198, 0.193758], 'p_i': 80, 'u_i': 4.0270},
        {'id': 5, 'e_m': 0.905700, 'e_o_k': [0.429533, 0.343626, 0.274901, 0.219921], 'p_i': 10, 'u_i': 3.7051},
    ]
    B_BUDGET = 176.639993
    return processors, tasks, B_BUDGET
