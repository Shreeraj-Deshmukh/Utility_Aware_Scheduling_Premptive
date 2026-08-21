"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.63997, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 176.63997, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.094835, 'e_o_k': [0.383192, 0.383192, 0.383192, 0.383192], 'p_i': 10, 'u_i': 4.0093},
        {'id': 1, 'e_m': 6.015361, 'e_o_k': [2.807168, 2.807168, 2.807168], 'p_i': 20, 'u_i': 1.1110},
        {'id': 2, 'e_m': 1.364859, 'e_o_k': [0.318467, 0.318467, 0.318467, 0.318467, 0.318467, 0.318467], 'p_i': 40, 'u_i': 1.1701},
        {'id': 3, 'e_m': 1.209297, 'e_o_k': [0.564339, 0.564339, 0.564339], 'p_i': 80, 'u_i': 4.4848},
        {'id': 4, 'e_m': 2.498208, 'e_o_k': [0.874373, 0.874373, 0.874373, 0.874373], 'p_i': 20, 'u_i': 3.6888},
        {'id': 5, 'e_m': 0.889705, 'e_o_k': [0.415196, 0.415196, 0.415196], 'p_i': 20, 'u_i': 2.1778},
        {'id': 6, 'e_m': 0.376895, 'e_o_k': [0.263827, 0.263827], 'p_i': 10, 'u_i': 3.8298},
        {'id': 7, 'e_m': 5.337019, 'e_o_k': [3.735913, 3.735913], 'p_i': 40, 'u_i': 2.6902},
    ]
    B_BUDGET = 176.639970
    return processors, tasks, B_BUDGET
