"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399992, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399992, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.094835, 'e_o_k': [0.224352, 0.179481, 0.143585], 'p_i': 10, 'u_i': 4.0093},
        {'id': 1, 'e_m': 6.015361, 'e_o_k': [1.232656, 0.986125, 0.788900], 'p_i': 20, 'u_i': 1.1110},
        {'id': 2, 'e_m': 1.364859, 'e_o_k': [0.279684, 0.223747, 0.178998], 'p_i': 40, 'u_i': 1.4549},
        {'id': 3, 'e_m': 1.209297, 'e_o_k': [0.247807, 0.198245, 0.158596], 'p_i': 80, 'u_i': 2.4103},
        {'id': 4, 'e_m': 2.498208, 'e_o_k': [0.511928, 0.409542, 0.327634], 'p_i': 20, 'u_i': 1.7953},
        {'id': 5, 'e_m': 0.889705, 'e_o_k': [0.182317, 0.145853, 0.116683], 'p_i': 20, 'u_i': 3.8298},
        {'id': 6, 'e_m': 0.376895, 'e_o_k': [0.077233, 0.061786, 0.049429], 'p_i': 10, 'u_i': 2.6902},
        {'id': 7, 'e_m': 5.337019, 'e_o_k': [1.093651, 0.874921, 0.699937], 'p_i': 40, 'u_i': 2.7407},
    ]
    B_BUDGET = 110.399992
    return processors, tasks, B_BUDGET
