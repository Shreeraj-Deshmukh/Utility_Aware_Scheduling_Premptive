"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399997, "H": 80, "J": 21, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "freq", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399997, "H": 80, "J": 21, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "freq", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.667633, 'e_o_k': [0.113081, 0.090465, 0.072372, 0.057898], 'p_i': 10, 'u_i': 1.6879},
        {'id': 1, 'e_m': 1.022805, 'e_o_k': [0.173239, 0.138592, 0.110873, 0.088699], 'p_i': 20, 'u_i': 2.2588},
        {'id': 2, 'e_m': 4.952657, 'e_o_k': [1.375738, 1.100590], 'p_i': 40, 'u_i': 4.0829},
        {'id': 3, 'e_m': 7.527601, 'e_o_k': [1.542541, 1.234033, 0.987226], 'p_i': 80, 'u_i': 1.6866},
        {'id': 4, 'e_m': 0.525923, 'e_o_k': [0.107771, 0.086217, 0.068974], 'p_i': 40, 'u_i': 3.5950},
        {'id': 5, 'e_m': 15.701459, 'e_o_k': [4.361516, 3.489213], 'p_i': 80, 'u_i': 4.2025},
        {'id': 6, 'e_m': 6.203629, 'e_o_k': [1.723230, 1.378584], 'p_i': 40, 'u_i': 3.6883},
        {'id': 7, 'e_m': 7.974239, 'e_o_k': [2.215066, 1.772053], 'p_i': 80, 'u_i': 1.6967},
    ]
    B_BUDGET = 110.399997
    return processors, tasks, B_BUDGET
