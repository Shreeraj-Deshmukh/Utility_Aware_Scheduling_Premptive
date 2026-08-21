"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.459408, 'e_o_k': [0.357317, 0.285854], 'p_i': 10, 'u_i': 4.1192},
        {'id': 1, 'e_m': 0.727754, 'e_o_k': [0.345141, 0.276113, 0.220890, 0.176712], 'p_i': 20, 'u_i': 2.9903},
        {'id': 2, 'e_m': 3.606706, 'e_o_k': [1.710497, 1.368398, 1.094718, 0.875775], 'p_i': 40, 'u_i': 3.9277},
        {'id': 3, 'e_m': 5.618102, 'e_o_k': [2.339762, 1.871809, 1.497448, 1.197958, 0.958366], 'p_i': 80, 'u_i': 2.3920},
        {'id': 4, 'e_m': 0.519589, 'e_o_k': [0.246417, 0.197134, 0.157707, 0.126166], 'p_i': 40, 'u_i': 2.2588},
        {'id': 5, 'e_m': 11.543030, 'e_o_k': [8.977912, 7.182330], 'p_i': 80, 'u_i': 4.0829},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET
