"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.060089, 'e_o_k': [0.572247, 0.457797], 'p_i': 10, 'u_i': 3.7892},
        {'id': 1, 'e_m': 0.339026, 'e_o_k': [0.094174, 0.075339], 'p_i': 20, 'u_i': 2.5683},
        {'id': 2, 'e_m': 15.847193, 'e_o_k': [4.401998, 3.521598], 'p_i': 40, 'u_i': 1.2577},
        {'id': 3, 'e_m': 1.762893, 'e_o_k': [0.489692, 0.391754], 'p_i': 80, 'u_i': 3.4086},
        {'id': 4, 'e_m': 0.784991, 'e_o_k': [0.218053, 0.174442], 'p_i': 40, 'u_i': 3.2935},
        {'id': 5, 'e_m': 0.814426, 'e_o_k': [0.226230, 0.180984], 'p_i': 10, 'u_i': 4.9988},
        {'id': 6, 'e_m': 0.165452, 'e_o_k': [0.045959, 0.036767], 'p_i': 20, 'u_i': 2.8879},
        {'id': 7, 'e_m': 0.989677, 'e_o_k': [0.274910, 0.219928], 'p_i': 20, 'u_i': 4.7528},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
