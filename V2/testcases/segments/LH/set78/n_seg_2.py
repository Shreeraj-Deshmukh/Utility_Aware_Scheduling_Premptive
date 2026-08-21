"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.143220, 'e_o_k': [0.889171, 0.711337], 'p_i': 10, 'u_i': 1.7025},
        {'id': 1, 'e_m': 0.721620, 'e_o_k': [0.561260, 0.449008], 'p_i': 20, 'u_i': 2.0058},
        {'id': 2, 'e_m': 0.561215, 'e_o_k': [0.436501, 0.349200], 'p_i': 40, 'u_i': 3.5722},
        {'id': 3, 'e_m': 9.907138, 'e_o_k': [7.705552, 6.164442], 'p_i': 80, 'u_i': 1.2384},
        {'id': 4, 'e_m': 0.924900, 'e_o_k': [0.719367, 0.575493], 'p_i': 40, 'u_i': 4.5379},
        {'id': 5, 'e_m': 1.311382, 'e_o_k': [1.019964, 0.815971], 'p_i': 20, 'u_i': 1.9982},
        {'id': 6, 'e_m': 0.152759, 'e_o_k': [0.118813, 0.095050], 'p_i': 20, 'u_i': 2.1252},
        {'id': 7, 'e_m': 1.231826, 'e_o_k': [0.958087, 0.766470], 'p_i': 80, 'u_i': 4.2384},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
