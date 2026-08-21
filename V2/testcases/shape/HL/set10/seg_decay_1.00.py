"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399995, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.399995, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.443224, 'e_o_k': [0.036935, 0.036935, 0.036935, 0.036935, 0.036935, 0.036935], 'p_i': 10, 'u_i': 3.7777},
        {'id': 1, 'e_m': 0.385037, 'e_o_k': [0.038504, 0.038504, 0.038504, 0.038504, 0.038504], 'p_i': 20, 'u_i': 2.9102},
        {'id': 2, 'e_m': 7.186952, 'e_o_k': [0.898369, 0.898369, 0.898369, 0.898369], 'p_i': 40, 'u_i': 3.0744},
        {'id': 3, 'e_m': 20.620712, 'e_o_k': [5.155178, 5.155178], 'p_i': 80, 'u_i': 3.1102},
        {'id': 4, 'e_m': 1.451540, 'e_o_k': [0.120962, 0.120962, 0.120962, 0.120962, 0.120962, 0.120962], 'p_i': 20, 'u_i': 3.9746},
        {'id': 5, 'e_m': 1.346300, 'e_o_k': [0.224383, 0.224383, 0.224383], 'p_i': 10, 'u_i': 1.5757},
        {'id': 6, 'e_m': 2.067937, 'e_o_k': [0.344656, 0.344656, 0.344656], 'p_i': 40, 'u_i': 4.9941},
        {'id': 7, 'e_m': 1.603507, 'e_o_k': [0.400877, 0.400877], 'p_i': 40, 'u_i': 1.7632},
    ]
    B_BUDGET = 110.399995
    return processors, tasks, B_BUDGET
