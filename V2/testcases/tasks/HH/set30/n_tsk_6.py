"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639994, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639994, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.068547, 'e_o_k': [0.053314, 0.042651], 'p_i': 10, 'u_i': 2.7951},
        {'id': 1, 'e_m': 3.049223, 'e_o_k': [1.749554, 1.399644, 1.119715], 'p_i': 20, 'u_i': 4.2173},
        {'id': 2, 'e_m': 4.038573, 'e_o_k': [3.141112, 2.512890], 'p_i': 40, 'u_i': 4.5788},
        {'id': 3, 'e_m': 8.227761, 'e_o_k': [4.720846, 3.776677, 3.021342], 'p_i': 80, 'u_i': 1.6533},
        {'id': 4, 'e_m': 28.357108, 'e_o_k': [13.448493, 10.758794, 8.607035, 6.885628], 'p_i': 80, 'u_i': 4.3793},
        {'id': 5, 'e_m': 6.592717, 'e_o_k': [3.126627, 2.501302, 2.001042, 1.600833], 'p_i': 80, 'u_i': 2.7000},
    ]
    B_BUDGET = 176.639994
    return processors, tasks, B_BUDGET
