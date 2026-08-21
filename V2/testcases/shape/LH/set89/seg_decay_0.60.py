"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 47, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 47, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.612231, 'e_o_k': [0.359628, 0.215777, 0.129466, 0.077680, 0.046608, 0.027965], 'p_i': 10, 'u_i': 1.1682},
        {'id': 1, 'e_m': 0.818720, 'e_o_k': [0.480921, 0.288553, 0.173132, 0.103879, 0.062327, 0.037396], 'p_i': 20, 'u_i': 1.7372},
        {'id': 2, 'e_m': 1.130553, 'e_o_k': [0.664094, 0.398456, 0.239074, 0.143444, 0.086067, 0.051640], 'p_i': 40, 'u_i': 1.2016},
        {'id': 3, 'e_m': 0.013730, 'e_o_k': [0.012014, 0.007208], 'p_i': 80, 'u_i': 4.7805},
        {'id': 4, 'e_m': 0.810047, 'e_o_k': [0.578605, 0.347163, 0.208298], 'p_i': 10, 'u_i': 3.7064},
        {'id': 5, 'e_m': 1.453435, 'e_o_k': [1.271756, 0.763053], 'p_i': 10, 'u_i': 4.7396},
        {'id': 6, 'e_m': 0.030685, 'e_o_k': [0.026849, 0.016110], 'p_i': 10, 'u_i': 4.0832},
        {'id': 7, 'e_m': 0.399887, 'e_o_k': [0.242818, 0.145691, 0.087415, 0.052449, 0.031469], 'p_i': 10, 'u_i': 1.4400},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
