"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399991, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.399991, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.381593, 'e_o_k': [0.744248, 0.446549], 'p_i': 10, 'u_i': 3.1340},
        {'id': 1, 'e_m': 0.718285, 'e_o_k': [0.165047, 0.099028, 0.059417, 0.035650], 'p_i': 20, 'u_i': 4.7064},
        {'id': 2, 'e_m': 1.663706, 'e_o_k': [0.360797, 0.216478, 0.129887, 0.077932, 0.046759], 'p_i': 40, 'u_i': 3.9461},
        {'id': 3, 'e_m': 20.841520, 'e_o_k': [4.788952, 2.873371, 1.724023, 1.034414], 'p_i': 80, 'u_i': 2.2173},
        {'id': 4, 'e_m': 1.314253, 'e_o_k': [0.410704, 0.246422], 'p_i': 20, 'u_i': 4.4667},
        {'id': 5, 'e_m': 0.736106, 'e_o_k': [0.159634, 0.095781, 0.057468, 0.034481, 0.020689], 'p_i': 10, 'u_i': 3.9626},
        {'id': 6, 'e_m': 1.268397, 'e_o_k': [0.323571, 0.194142, 0.116485], 'p_i': 20, 'u_i': 1.6271},
        {'id': 7, 'e_m': 0.842866, 'e_o_k': [0.182787, 0.109672, 0.065803, 0.039482, 0.023689], 'p_i': 40, 'u_i': 2.4987},
    ]
    B_BUDGET = 110.399991
    return processors, tasks, B_BUDGET
