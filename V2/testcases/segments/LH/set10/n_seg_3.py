"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319984, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319984, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.221612, 'e_o_k': [0.127154, 0.101723, 0.081379], 'p_i': 10, 'u_i': 2.5678},
        {'id': 1, 'e_m': 0.192518, 'e_o_k': [0.110461, 0.088369, 0.070695], 'p_i': 20, 'u_i': 3.0744},
        {'id': 2, 'e_m': 3.593476, 'e_o_k': [2.061830, 1.649464, 1.319571], 'p_i': 40, 'u_i': 3.1102},
        {'id': 3, 'e_m': 10.310356, 'e_o_k': [5.915778, 4.732622, 3.786098], 'p_i': 80, 'u_i': 3.9862},
        {'id': 4, 'e_m': 0.725770, 'e_o_k': [0.416425, 0.333140, 0.266512], 'p_i': 20, 'u_i': 1.5757},
        {'id': 5, 'e_m': 0.673150, 'e_o_k': [0.386234, 0.308987, 0.247189], 'p_i': 10, 'u_i': 4.9941},
        {'id': 6, 'e_m': 1.033969, 'e_o_k': [0.593261, 0.474609, 0.379687], 'p_i': 40, 'u_i': 1.7632},
        {'id': 7, 'e_m': 0.801753, 'e_o_k': [0.460022, 0.368018, 0.294414], 'p_i': 40, 'u_i': 1.4284},
    ]
    B_BUDGET = 88.319984
    return processors, tasks, B_BUDGET
