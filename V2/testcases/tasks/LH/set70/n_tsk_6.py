"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320005, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320005, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.762181, 'e_o_k': [0.592808, 0.474246], 'p_i': 10, 'u_i': 1.8882},
        {'id': 1, 'e_m': 2.928001, 'e_o_k': [1.219420, 0.975536, 0.780429, 0.624343, 0.499474], 'p_i': 20, 'u_i': 2.0463},
        {'id': 2, 'e_m': 5.383574, 'e_o_k': [2.242088, 1.793671, 1.434936, 1.147949, 0.918359], 'p_i': 40, 'u_i': 1.5718},
        {'id': 3, 'e_m': 1.416998, 'e_o_k': [1.102110, 0.881688], 'p_i': 80, 'u_i': 2.9208},
        {'id': 4, 'e_m': 0.074139, 'e_o_k': [0.028134, 0.022507, 0.018006, 0.014405, 0.011524, 0.009219], 'p_i': 20, 'u_i': 4.6964},
        {'id': 5, 'e_m': 1.709844, 'e_o_k': [0.981058, 0.784847, 0.627877], 'p_i': 80, 'u_i': 4.6519},
    ]
    B_BUDGET = 88.320005
    return processors, tasks, B_BUDGET
