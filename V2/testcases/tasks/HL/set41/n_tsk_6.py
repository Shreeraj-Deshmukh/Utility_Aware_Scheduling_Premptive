"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.201708, 'e_o_k': [0.162865, 0.130292, 0.104233, 0.083387, 0.066709, 0.053368], 'p_i': 10, 'u_i': 4.4924},
        {'id': 1, 'e_m': 2.441029, 'e_o_k': [0.500211, 0.400169, 0.320135], 'p_i': 20, 'u_i': 4.2054},
        {'id': 2, 'e_m': 17.653473, 'e_o_k': [2.625755, 2.100604, 1.680483, 1.344386, 1.075509], 'p_i': 40, 'u_i': 2.8306},
        {'id': 3, 'e_m': 1.130039, 'e_o_k': [0.313900, 0.251120], 'p_i': 80, 'u_i': 2.8504},
        {'id': 4, 'e_m': 0.811483, 'e_o_k': [0.109978, 0.087983, 0.070386, 0.056309, 0.045047, 0.036038], 'p_i': 10, 'u_i': 1.4385},
        {'id': 5, 'e_m': 1.693371, 'e_o_k': [0.229499, 0.183599, 0.146879, 0.117503, 0.094003, 0.075202], 'p_i': 80, 'u_i': 4.3024},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET
