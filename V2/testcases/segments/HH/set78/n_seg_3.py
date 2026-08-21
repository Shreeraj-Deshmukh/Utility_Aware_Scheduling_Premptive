"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640005, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640005, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.286440, 'e_o_k': [1.311892, 1.049514, 0.839611], 'p_i': 10, 'u_i': 1.7025},
        {'id': 1, 'e_m': 1.443240, 'e_o_k': [0.828089, 0.662471, 0.529977], 'p_i': 20, 'u_i': 2.0058},
        {'id': 2, 'e_m': 1.122430, 'e_o_k': [0.644017, 0.515214, 0.412171], 'p_i': 40, 'u_i': 3.5722},
        {'id': 3, 'e_m': 19.814276, 'e_o_k': [11.368847, 9.095078, 7.276062], 'p_i': 80, 'u_i': 1.2384},
        {'id': 4, 'e_m': 1.849800, 'e_o_k': [1.061361, 0.849089, 0.679271], 'p_i': 40, 'u_i': 4.5379},
        {'id': 5, 'e_m': 2.622764, 'e_o_k': [1.504864, 1.203892, 0.963113], 'p_i': 20, 'u_i': 1.9982},
        {'id': 6, 'e_m': 0.305518, 'e_o_k': [0.175297, 0.140238, 0.112190], 'p_i': 20, 'u_i': 2.1252},
        {'id': 7, 'e_m': 2.463653, 'e_o_k': [1.413571, 1.130857, 0.904686], 'p_i': 80, 'u_i': 4.2384},
    ]
    B_BUDGET = 176.640005
    return processors, tasks, B_BUDGET
