"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639993, "H": 80, "J": 35, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.639993, "H": 80, "J": 35, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.435325, 'e_o_k': [0.380909, 0.228546], 'p_i': 10, 'u_i': 1.4412},
        {'id': 1, 'e_m': 3.692417, 'e_o_k': [2.375636, 1.425381, 0.855229, 0.513137], 'p_i': 20, 'u_i': 3.7136},
        {'id': 2, 'e_m': 1.661795, 'e_o_k': [0.976148, 0.585689, 0.351413, 0.210848, 0.126509, 0.075905], 'p_i': 40, 'u_i': 3.0715},
        {'id': 3, 'e_m': 21.880045, 'e_o_k': [12.852470, 7.711482, 4.626889, 2.776134, 1.665680, 0.999408], 'p_i': 80, 'u_i': 2.1053},
        {'id': 4, 'e_m': 0.175787, 'e_o_k': [0.153813, 0.092288], 'p_i': 20, 'u_i': 3.9261},
        {'id': 5, 'e_m': 0.532000, 'e_o_k': [0.465500, 0.279300], 'p_i': 20, 'u_i': 2.2961},
        {'id': 6, 'e_m': 0.171451, 'e_o_k': [0.104108, 0.062465, 0.037479, 0.022487, 0.013492], 'p_i': 10, 'u_i': 1.3761},
        {'id': 7, 'e_m': 4.085336, 'e_o_k': [2.918097, 1.750858, 1.050515], 'p_i': 20, 'u_i': 2.1930},
    ]
    B_BUDGET = 176.639993
    return processors, tasks, B_BUDGET
