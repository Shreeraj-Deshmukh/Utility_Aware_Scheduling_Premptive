"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.143043, 'e_o_k': [0.433759, 0.347008, 0.277606, 0.222085, 0.177668, 0.142134], 'p_i': 10, 'u_i': 2.5404},
        {'id': 1, 'e_m': 2.851808, 'e_o_k': [1.636283, 1.309026, 1.047221], 'p_i': 20, 'u_i': 1.0986},
        {'id': 2, 'e_m': 3.105701, 'e_o_k': [2.415545, 1.932436], 'p_i': 40, 'u_i': 3.7025},
        {'id': 3, 'e_m': 18.529161, 'e_o_k': [14.411570, 11.529256], 'p_i': 80, 'u_i': 4.4926},
        {'id': 4, 'e_m': 1.923092, 'e_o_k': [1.103414, 0.882731, 0.706185], 'p_i': 80, 'u_i': 3.2922},
        {'id': 5, 'e_m': 8.392386, 'e_o_k': [6.527411, 5.221929], 'p_i': 40, 'u_i': 3.7450},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET
