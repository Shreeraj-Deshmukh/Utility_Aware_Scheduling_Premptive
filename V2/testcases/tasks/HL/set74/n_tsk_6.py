"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.330892, 'e_o_k': [0.049216, 0.039373, 0.031499, 0.025199, 0.020159], 'p_i': 10, 'u_i': 3.5312},
        {'id': 1, 'e_m': 3.283430, 'e_o_k': [0.444996, 0.355997, 0.284797, 0.227838, 0.182270, 0.145816], 'p_i': 20, 'u_i': 1.4207},
        {'id': 2, 'e_m': 10.363895, 'e_o_k': [1.541512, 1.233210, 0.986568, 0.789254, 0.631403], 'p_i': 40, 'u_i': 4.1417},
        {'id': 3, 'e_m': 21.476872, 'e_o_k': [3.194442, 2.555553, 2.044443, 1.635554, 1.308443], 'p_i': 80, 'u_i': 4.9795},
        {'id': 4, 'e_m': 0.405589, 'e_o_k': [0.083113, 0.066490, 0.053192], 'p_i': 20, 'u_i': 4.9448},
        {'id': 5, 'e_m': 0.549016, 'e_o_k': [0.081660, 0.065328, 0.052262, 0.041810, 0.033448], 'p_i': 10, 'u_i': 4.4554},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET
