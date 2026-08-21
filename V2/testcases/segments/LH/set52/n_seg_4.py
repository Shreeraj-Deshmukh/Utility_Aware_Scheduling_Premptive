"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "segments", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "segments", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.036217, 'e_o_k': [0.017176, 0.013741, 0.010993, 0.008794], 'p_i': 10, 'u_i': 2.7495},
        {'id': 1, 'e_m': 0.574084, 'e_o_k': [0.272262, 0.217810, 0.174248, 0.139398], 'p_i': 20, 'u_i': 1.5180},
        {'id': 2, 'e_m': 5.044978, 'e_o_k': [2.392605, 1.914084, 1.531267, 1.225014], 'p_i': 40, 'u_i': 2.4726},
        {'id': 3, 'e_m': 7.817224, 'e_o_k': [3.707355, 2.965884, 2.372707, 1.898166], 'p_i': 80, 'u_i': 4.1932},
        {'id': 4, 'e_m': 2.653896, 'e_o_k': [1.258623, 1.006898, 0.805519, 0.644415], 'p_i': 80, 'u_i': 2.7154},
        {'id': 5, 'e_m': 2.164181, 'e_o_k': [1.026373, 0.821099, 0.656879, 0.525503], 'p_i': 40, 'u_i': 4.3253},
        {'id': 6, 'e_m': 2.331763, 'e_o_k': [1.105849, 0.884680, 0.707744, 0.566195], 'p_i': 80, 'u_i': 1.0005},
        {'id': 7, 'e_m': 1.096363, 'e_o_k': [0.519955, 0.415964, 0.332771, 0.266217], 'p_i': 40, 'u_i': 1.9051},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
