"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400006, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400006, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.685913, 'e_o_k': [0.190531, 0.152425], 'p_i': 10, 'u_i': 3.1491},
        {'id': 1, 'e_m': 2.484409, 'e_o_k': [0.690114, 0.552091], 'p_i': 20, 'u_i': 2.2531},
        {'id': 2, 'e_m': 0.048071, 'e_o_k': [0.013353, 0.010682], 'p_i': 40, 'u_i': 4.0598},
        {'id': 3, 'e_m': 11.321347, 'e_o_k': [3.144819, 2.515855], 'p_i': 80, 'u_i': 4.5014},
        {'id': 4, 'e_m': 9.862979, 'e_o_k': [2.739717, 2.191773], 'p_i': 40, 'u_i': 4.8694},
        {'id': 5, 'e_m': 3.207163, 'e_o_k': [0.890879, 0.712703], 'p_i': 40, 'u_i': 3.6293},
        {'id': 6, 'e_m': 9.607054, 'e_o_k': [2.668626, 2.134901], 'p_i': 80, 'u_i': 4.0966},
        {'id': 7, 'e_m': 1.410237, 'e_o_k': [0.391732, 0.313386], 'p_i': 80, 'u_i': 3.0738},
    ]
    B_BUDGET = 110.400006
    return processors, tasks, B_BUDGET
