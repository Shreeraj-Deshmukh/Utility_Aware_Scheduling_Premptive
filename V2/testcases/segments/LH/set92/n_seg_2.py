"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320008, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.320008, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.279536, 'e_o_k': [0.217417, 0.173933], 'p_i': 10, 'u_i': 3.7403},
        {'id': 1, 'e_m': 0.807491, 'e_o_k': [0.628048, 0.502439], 'p_i': 20, 'u_i': 1.2645},
        {'id': 2, 'e_m': 3.179023, 'e_o_k': [2.472573, 1.978059], 'p_i': 40, 'u_i': 2.2756},
        {'id': 3, 'e_m': 7.775197, 'e_o_k': [6.047375, 4.837900], 'p_i': 80, 'u_i': 2.5093},
        {'id': 4, 'e_m': 0.001832, 'e_o_k': [0.001425, 0.001140], 'p_i': 10, 'u_i': 3.6510},
        {'id': 5, 'e_m': 1.937647, 'e_o_k': [1.507059, 1.205647], 'p_i': 80, 'u_i': 3.1983},
        {'id': 6, 'e_m': 0.361320, 'e_o_k': [0.281026, 0.224821], 'p_i': 10, 'u_i': 4.3627},
        {'id': 7, 'e_m': 3.778825, 'e_o_k': [2.939086, 2.351269], 'p_i': 40, 'u_i': 4.4103},
    ]
    B_BUDGET = 88.320008
    return processors, tasks, B_BUDGET
