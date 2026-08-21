"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320007, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.320007, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.460174, 'e_o_k': [1.135691, 0.908552], 'p_i': 10, 'u_i': 1.9752},
        {'id': 1, 'e_m': 0.417207, 'e_o_k': [0.324494, 0.259595], 'p_i': 20, 'u_i': 3.9662},
        {'id': 2, 'e_m': 2.317386, 'e_o_k': [1.802412, 1.441929], 'p_i': 40, 'u_i': 1.9890},
        {'id': 3, 'e_m': 0.317304, 'e_o_k': [0.246792, 0.197434], 'p_i': 80, 'u_i': 3.3639},
        {'id': 4, 'e_m': 1.728593, 'e_o_k': [1.344461, 1.075569], 'p_i': 40, 'u_i': 4.7869},
        {'id': 5, 'e_m': 0.210554, 'e_o_k': [0.163765, 0.131012], 'p_i': 10, 'u_i': 2.7944},
        {'id': 6, 'e_m': 0.207004, 'e_o_k': [0.161003, 0.128802], 'p_i': 10, 'u_i': 4.7769},
        {'id': 7, 'e_m': 0.862507, 'e_o_k': [0.670839, 0.536671], 'p_i': 10, 'u_i': 1.3167},
    ]
    B_BUDGET = 88.320007
    return processors, tasks, B_BUDGET
