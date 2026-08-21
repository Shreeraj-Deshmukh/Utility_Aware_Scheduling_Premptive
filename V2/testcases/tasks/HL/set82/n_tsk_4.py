"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399989, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399989, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.401182, 'e_o_k': [0.505887, 0.404710, 0.323768, 0.259014, 0.207211], 'p_i': 10, 'u_i': 2.1126},
        {'id': 1, 'e_m': 0.754885, 'e_o_k': [0.127860, 0.102288, 0.081830, 0.065464], 'p_i': 20, 'u_i': 1.1880},
        {'id': 2, 'e_m': 7.815327, 'e_o_k': [2.170924, 1.736739], 'p_i': 40, 'u_i': 4.0095},
        {'id': 3, 'e_m': 18.140351, 'e_o_k': [2.698172, 2.158538, 1.726830, 1.381464, 1.105171], 'p_i': 80, 'u_i': 4.5444},
    ]
    B_BUDGET = 110.399989
    return processors, tasks, B_BUDGET
