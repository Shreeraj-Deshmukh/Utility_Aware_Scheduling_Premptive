"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399998, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399998, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.381593, 'e_o_k': [0.661554, 0.529243], 'p_i': 10, 'u_i': 3.1340},
        {'id': 1, 'e_m': 0.718285, 'e_o_k': [0.199524, 0.159619], 'p_i': 20, 'u_i': 4.7064},
        {'id': 2, 'e_m': 1.663706, 'e_o_k': [0.462141, 0.369713], 'p_i': 40, 'u_i': 3.9461},
        {'id': 3, 'e_m': 20.841520, 'e_o_k': [5.789311, 4.631449], 'p_i': 80, 'u_i': 2.2173},
        {'id': 4, 'e_m': 1.314253, 'e_o_k': [0.365070, 0.292056], 'p_i': 20, 'u_i': 4.4667},
        {'id': 5, 'e_m': 0.736106, 'e_o_k': [0.204474, 0.163579], 'p_i': 10, 'u_i': 3.9626},
        {'id': 6, 'e_m': 1.268397, 'e_o_k': [0.352332, 0.281866], 'p_i': 20, 'u_i': 1.6271},
        {'id': 7, 'e_m': 0.842866, 'e_o_k': [0.234129, 0.187304], 'p_i': 40, 'u_i': 2.4987},
    ]
    B_BUDGET = 110.399998
    return processors, tasks, B_BUDGET
