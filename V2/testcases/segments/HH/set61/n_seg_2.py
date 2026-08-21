"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640006, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640006, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.685913, 'e_o_k': [0.533488, 0.426790], 'p_i': 10, 'u_i': 3.1491},
        {'id': 1, 'e_m': 2.484409, 'e_o_k': [1.932318, 1.545854], 'p_i': 20, 'u_i': 2.2531},
        {'id': 2, 'e_m': 0.048071, 'e_o_k': [0.037388, 0.029911], 'p_i': 40, 'u_i': 4.0598},
        {'id': 3, 'e_m': 11.321347, 'e_o_k': [8.805492, 7.044394], 'p_i': 80, 'u_i': 4.5014},
        {'id': 4, 'e_m': 9.862979, 'e_o_k': [7.671206, 6.136965], 'p_i': 40, 'u_i': 4.8694},
        {'id': 5, 'e_m': 3.207163, 'e_o_k': [2.494460, 1.995568], 'p_i': 40, 'u_i': 3.6293},
        {'id': 6, 'e_m': 9.607054, 'e_o_k': [7.472153, 5.977722], 'p_i': 80, 'u_i': 4.0966},
        {'id': 7, 'e_m': 1.410237, 'e_o_k': [1.096851, 0.877481], 'p_i': 80, 'u_i': 3.0738},
    ]
    B_BUDGET = 176.640006
    return processors, tasks, B_BUDGET
