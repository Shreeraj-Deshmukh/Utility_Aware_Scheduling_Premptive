"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400018, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.400018, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.121191, 'e_o_k': [0.280298, 0.280298], 'p_i': 10, 'u_i': 2.9208},
        {'id': 1, 'e_m': 4.546458, 'e_o_k': [0.378872, 0.378872, 0.378872, 0.378872, 0.378872, 0.378872], 'p_i': 20, 'u_i': 4.6964},
        {'id': 2, 'e_m': 10.573229, 'e_o_k': [1.762205, 1.762205, 1.762205], 'p_i': 40, 'u_i': 4.6519},
        {'id': 3, 'e_m': 3.680258, 'e_o_k': [0.920065, 0.920065], 'p_i': 80, 'u_i': 4.9020},
        {'id': 4, 'e_m': 0.623936, 'e_o_k': [0.051995, 0.051995, 0.051995, 0.051995, 0.051995, 0.051995], 'p_i': 80, 'u_i': 1.1409},
        {'id': 5, 'e_m': 3.160733, 'e_o_k': [0.316073, 0.316073, 0.316073, 0.316073, 0.316073], 'p_i': 40, 'u_i': 1.3844},
        {'id': 6, 'e_m': 4.750875, 'e_o_k': [0.475087, 0.475087, 0.475087, 0.475087, 0.475087], 'p_i': 80, 'u_i': 3.8571},
        {'id': 7, 'e_m': 0.080412, 'e_o_k': [0.020103, 0.020103], 'p_i': 20, 'u_i': 3.6185},
    ]
    B_BUDGET = 110.400018
    return processors, tasks, B_BUDGET
