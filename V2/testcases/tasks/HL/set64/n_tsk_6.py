"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399991, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399991, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.944933, 'e_o_k': [0.329426, 0.263541, 0.210833, 0.168666], 'p_i': 10, 'u_i': 2.8432},
        {'id': 1, 'e_m': 6.208162, 'e_o_k': [1.272164, 1.017731, 0.814185], 'p_i': 20, 'u_i': 4.5844},
        {'id': 2, 'e_m': 2.068426, 'e_o_k': [0.574563, 0.459650], 'p_i': 40, 'u_i': 1.8342},
        {'id': 3, 'e_m': 5.947133, 'e_o_k': [1.218675, 0.974940, 0.779952], 'p_i': 80, 'u_i': 2.1428},
        {'id': 4, 'e_m': 1.464929, 'e_o_k': [0.248125, 0.198500, 0.158800, 0.127040], 'p_i': 10, 'u_i': 3.7337},
        {'id': 5, 'e_m': 0.902234, 'e_o_k': [0.134197, 0.107358, 0.085886, 0.068709, 0.054967], 'p_i': 40, 'u_i': 3.4112},
    ]
    B_BUDGET = 110.399991
    return processors, tasks, B_BUDGET
