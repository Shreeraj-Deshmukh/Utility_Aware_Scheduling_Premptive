"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.435325, 'e_o_k': [0.120924, 0.096739], 'p_i': 10, 'u_i': 1.4412},
        {'id': 1, 'e_m': 3.692417, 'e_o_k': [1.025671, 0.820537], 'p_i': 20, 'u_i': 3.7136},
        {'id': 2, 'e_m': 1.661795, 'e_o_k': [0.461610, 0.369288], 'p_i': 40, 'u_i': 4.0270},
        {'id': 3, 'e_m': 21.880045, 'e_o_k': [6.077790, 4.862232], 'p_i': 80, 'u_i': 3.7051},
        {'id': 4, 'e_m': 0.175787, 'e_o_k': [0.048830, 0.039064], 'p_i': 20, 'u_i': 3.9261},
        {'id': 5, 'e_m': 0.532000, 'e_o_k': [0.147778, 0.118222], 'p_i': 20, 'u_i': 2.2961},
        {'id': 6, 'e_m': 0.171451, 'e_o_k': [0.047625, 0.038100], 'p_i': 10, 'u_i': 1.3761},
        {'id': 7, 'e_m': 4.085336, 'e_o_k': [1.134815, 0.907852], 'p_i': 20, 'u_i': 2.1930},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
