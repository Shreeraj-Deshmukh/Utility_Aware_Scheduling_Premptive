"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399994, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399994, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.484964, 'e_o_k': [0.099378, 0.079502, 0.063602], 'p_i': 10, 'u_i': 1.7042},
        {'id': 1, 'e_m': 0.736640, 'e_o_k': [0.150951, 0.120761, 0.096609], 'p_i': 20, 'u_i': 4.3788},
        {'id': 2, 'e_m': 4.567615, 'e_o_k': [0.935987, 0.748789, 0.599031], 'p_i': 40, 'u_i': 3.2500},
        {'id': 3, 'e_m': 2.590483, 'e_o_k': [0.530837, 0.424669, 0.339735], 'p_i': 80, 'u_i': 3.9101},
        {'id': 4, 'e_m': 1.196360, 'e_o_k': [0.245156, 0.196125, 0.156900], 'p_i': 80, 'u_i': 2.7187},
        {'id': 5, 'e_m': 5.644234, 'e_o_k': [1.156605, 0.925284, 0.740227], 'p_i': 40, 'u_i': 1.9356},
        {'id': 6, 'e_m': 25.995886, 'e_o_k': [5.327026, 4.261621, 3.409297], 'p_i': 80, 'u_i': 1.5831},
        {'id': 7, 'e_m': 3.483648, 'e_o_k': [0.713862, 0.571090, 0.456872], 'p_i': 40, 'u_i': 3.6851},
    ]
    B_BUDGET = 110.399994
    return processors, tasks, B_BUDGET
