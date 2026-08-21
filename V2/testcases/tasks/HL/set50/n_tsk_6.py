"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399998, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399998, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.622274, 'e_o_k': [0.241295, 0.193036, 0.154429, 0.123543, 0.098834], 'p_i': 10, 'u_i': 4.0918},
        {'id': 1, 'e_m': 1.480680, 'e_o_k': [0.220234, 0.176188, 0.140950, 0.112760, 0.090208], 'p_i': 20, 'u_i': 2.7075},
        {'id': 2, 'e_m': 5.279637, 'e_o_k': [0.894247, 0.715398, 0.572318, 0.457855], 'p_i': 40, 'u_i': 3.4005},
        {'id': 3, 'e_m': 14.191480, 'e_o_k': [3.942078, 3.153662], 'p_i': 80, 'u_i': 3.5378},
        {'id': 4, 'e_m': 0.440421, 'e_o_k': [0.059689, 0.047751, 0.038201, 0.030561, 0.024449, 0.019559], 'p_i': 10, 'u_i': 2.8954},
        {'id': 5, 'e_m': 4.206242, 'e_o_k': [0.625631, 0.500505, 0.400404, 0.320323, 0.256258], 'p_i': 20, 'u_i': 2.6615},
    ]
    B_BUDGET = 110.399998
    return processors, tasks, B_BUDGET
