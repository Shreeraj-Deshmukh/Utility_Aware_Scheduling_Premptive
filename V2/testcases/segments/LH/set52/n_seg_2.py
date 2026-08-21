"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.036217, 'e_o_k': [0.028169, 0.022535], 'p_i': 10, 'u_i': 2.7495},
        {'id': 1, 'e_m': 0.574084, 'e_o_k': [0.446510, 0.357208], 'p_i': 20, 'u_i': 1.5180},
        {'id': 2, 'e_m': 5.044978, 'e_o_k': [3.923872, 3.139098], 'p_i': 40, 'u_i': 2.4726},
        {'id': 3, 'e_m': 7.817224, 'e_o_k': [6.080063, 4.864050], 'p_i': 80, 'u_i': 4.1932},
        {'id': 4, 'e_m': 2.653896, 'e_o_k': [2.064142, 1.651313], 'p_i': 80, 'u_i': 2.7154},
        {'id': 5, 'e_m': 2.164181, 'e_o_k': [1.683252, 1.346602], 'p_i': 40, 'u_i': 4.3253},
        {'id': 6, 'e_m': 2.331763, 'e_o_k': [1.813593, 1.450875], 'p_i': 80, 'u_i': 1.0005},
        {'id': 7, 'e_m': 1.096363, 'e_o_k': [0.852727, 0.682181], 'p_i': 40, 'u_i': 1.9051},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET
