"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400005, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400005, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.685913, 'e_o_k': [0.140556, 0.112445, 0.089956], 'p_i': 10, 'u_i': 3.1491},
        {'id': 1, 'e_m': 2.484409, 'e_o_k': [0.509100, 0.407280, 0.325824], 'p_i': 20, 'u_i': 2.2531},
        {'id': 2, 'e_m': 0.048071, 'e_o_k': [0.009851, 0.007880, 0.006304], 'p_i': 40, 'u_i': 4.0598},
        {'id': 3, 'e_m': 11.321347, 'e_o_k': [2.319948, 1.855958, 1.484767], 'p_i': 80, 'u_i': 4.5014},
        {'id': 4, 'e_m': 9.862979, 'e_o_k': [2.021102, 1.616882, 1.293505], 'p_i': 40, 'u_i': 4.8694},
        {'id': 5, 'e_m': 3.207163, 'e_o_k': [0.657205, 0.525764, 0.420612], 'p_i': 40, 'u_i': 3.6293},
        {'id': 6, 'e_m': 9.607054, 'e_o_k': [1.968659, 1.574927, 1.259941], 'p_i': 80, 'u_i': 4.0966},
        {'id': 7, 'e_m': 1.410237, 'e_o_k': [0.288983, 0.231186, 0.184949], 'p_i': 80, 'u_i': 3.0738},
    ]
    B_BUDGET = 110.400005
    return processors, tasks, B_BUDGET
