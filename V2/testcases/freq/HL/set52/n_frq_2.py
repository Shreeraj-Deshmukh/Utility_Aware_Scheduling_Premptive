"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400003, "H": 80, "J": 21, "factor": "n_frq", "n_frq": 2, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "freq", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400003, "H": 80, "J": 21, "factor": "n_frq", "n_frq": 2, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "freq", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 1.0]},
        {'id': 1, 'frequencies': [0.4, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.072434, 'e_o_k': [0.009817, 0.007853, 0.006283, 0.005026, 0.004021, 0.003217], 'p_i': 10, 'u_i': 2.1441},
        {'id': 1, 'e_m': 1.148168, 'e_o_k': [0.170777, 0.136622, 0.109297, 0.087438, 0.069950], 'p_i': 20, 'u_i': 1.5180},
        {'id': 2, 'e_m': 10.089957, 'e_o_k': [1.709004, 1.367203, 1.093762, 0.875010], 'p_i': 40, 'u_i': 2.4726},
        {'id': 3, 'e_m': 15.634448, 'e_o_k': [3.203780, 2.563024, 2.050419], 'p_i': 80, 'u_i': 4.1932},
        {'id': 4, 'e_m': 5.307793, 'e_o_k': [1.474387, 1.179509], 'p_i': 80, 'u_i': 2.7154},
        {'id': 5, 'e_m': 4.328363, 'e_o_k': [0.886960, 0.709568, 0.567654], 'p_i': 40, 'u_i': 4.3253},
        {'id': 6, 'e_m': 4.663525, 'e_o_k': [0.789892, 0.631914, 0.505531, 0.404425], 'p_i': 80, 'u_i': 1.0005},
        {'id': 7, 'e_m': 2.192726, 'e_o_k': [0.326143, 0.260915, 0.208732, 0.166985, 0.133588], 'p_i': 40, 'u_i': 1.9051},
    ]
    B_BUDGET = 110.400003
    return processors, tasks, B_BUDGET
