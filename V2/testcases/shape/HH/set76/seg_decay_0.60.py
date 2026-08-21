"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.63998, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.63998, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.094835, 'e_o_k': [0.704398, 0.422639, 0.253583, 0.152150], 'p_i': 10, 'u_i': 4.0093},
        {'id': 1, 'e_m': 6.015361, 'e_o_k': [4.296686, 2.578012, 1.546807], 'p_i': 20, 'u_i': 1.1110},
        {'id': 2, 'e_m': 1.364859, 'e_o_k': [0.801727, 0.481036, 0.288622, 0.173173, 0.103904, 0.062342], 'p_i': 40, 'u_i': 1.1701},
        {'id': 3, 'e_m': 1.209297, 'e_o_k': [0.863784, 0.518270, 0.310962], 'p_i': 80, 'u_i': 4.4848},
        {'id': 4, 'e_m': 2.498208, 'e_o_k': [1.607303, 0.964382, 0.578629, 0.347177], 'p_i': 20, 'u_i': 3.6888},
        {'id': 5, 'e_m': 0.889705, 'e_o_k': [0.635504, 0.381302, 0.228781], 'p_i': 20, 'u_i': 2.1778},
        {'id': 6, 'e_m': 0.376895, 'e_o_k': [0.329783, 0.197870], 'p_i': 10, 'u_i': 3.8298},
        {'id': 7, 'e_m': 5.337019, 'e_o_k': [4.669892, 2.801935], 'p_i': 40, 'u_i': 2.6902},
    ]
    B_BUDGET = 176.639980
    return processors, tasks, B_BUDGET
