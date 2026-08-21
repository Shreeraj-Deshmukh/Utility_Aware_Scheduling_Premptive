"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399994, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399994, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.253914, 'e_o_k': [0.070532, 0.056425], 'p_i': 10, 'u_i': 1.1447},
        {'id': 1, 'e_m': 2.444497, 'e_o_k': [0.679027, 0.543222], 'p_i': 20, 'u_i': 4.1970},
        {'id': 2, 'e_m': 1.438401, 'e_o_k': [0.399556, 0.319645], 'p_i': 40, 'u_i': 2.1490},
        {'id': 3, 'e_m': 9.006906, 'e_o_k': [2.501918, 2.001535], 'p_i': 80, 'u_i': 1.5069},
        {'id': 4, 'e_m': 0.947423, 'e_o_k': [0.263173, 0.210538], 'p_i': 20, 'u_i': 3.9372},
        {'id': 5, 'e_m': 0.973099, 'e_o_k': [0.270305, 0.216244], 'p_i': 20, 'u_i': 1.6580},
        {'id': 6, 'e_m': 1.046300, 'e_o_k': [0.290639, 0.232511], 'p_i': 20, 'u_i': 4.1894},
        {'id': 7, 'e_m': 28.439701, 'e_o_k': [7.899917, 6.319934], 'p_i': 80, 'u_i': 4.9102},
    ]
    B_BUDGET = 110.399994
    return processors, tasks, B_BUDGET
