"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320001, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320001, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.786850, 'e_o_k': [0.451472, 0.361177, 0.288942], 'p_i': 10, 'u_i': 3.6650},
        {'id': 1, 'e_m': 0.744352, 'e_o_k': [0.427087, 0.341670, 0.273336], 'p_i': 20, 'u_i': 4.7122},
        {'id': 2, 'e_m': 0.568045, 'e_o_k': [0.325927, 0.260742, 0.208594], 'p_i': 40, 'u_i': 2.7870},
        {'id': 3, 'e_m': 6.876570, 'e_o_k': [3.945573, 3.156458, 2.525167], 'p_i': 80, 'u_i': 1.7506},
        {'id': 4, 'e_m': 2.991189, 'e_o_k': [1.716256, 1.373005, 1.098404], 'p_i': 40, 'u_i': 4.5685},
        {'id': 5, 'e_m': 0.337006, 'e_o_k': [0.193364, 0.154691, 0.123753], 'p_i': 10, 'u_i': 2.7344},
        {'id': 6, 'e_m': 0.443917, 'e_o_k': [0.254706, 0.203765, 0.163012], 'p_i': 40, 'u_i': 1.1398},
        {'id': 7, 'e_m': 5.148870, 'e_o_k': [2.954270, 2.363416, 1.890733], 'p_i': 80, 'u_i': 4.8954},
    ]
    B_BUDGET = 88.320001
    return processors, tasks, B_BUDGET
