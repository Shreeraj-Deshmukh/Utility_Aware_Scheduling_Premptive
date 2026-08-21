"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.135304, 'e_o_k': [1.225174, 0.980140, 0.784112], 'p_i': 10, 'u_i': 4.1455},
        {'id': 1, 'e_m': 1.429944, 'e_o_k': [0.678158, 0.542526, 0.434021, 0.347217], 'p_i': 20, 'u_i': 1.8811},
        {'id': 2, 'e_m': 5.992960, 'e_o_k': [3.438584, 2.750867, 2.200694], 'p_i': 40, 'u_i': 4.6061},
        {'id': 3, 'e_m': 29.211870, 'e_o_k': [12.165819, 9.732656, 7.786124, 6.228900, 4.983120], 'p_i': 80, 'u_i': 1.8658},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
