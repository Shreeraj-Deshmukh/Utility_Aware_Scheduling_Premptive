"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319992, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319992, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.036217, 'e_o_k': [0.020780, 0.016624, 0.013299], 'p_i': 10, 'u_i': 2.7495},
        {'id': 1, 'e_m': 0.574084, 'e_o_k': [0.329392, 0.263514, 0.210811], 'p_i': 20, 'u_i': 1.5180},
        {'id': 2, 'e_m': 5.044978, 'e_o_k': [2.894660, 2.315728, 1.852582], 'p_i': 40, 'u_i': 2.4726},
        {'id': 3, 'e_m': 7.817224, 'e_o_k': [4.485292, 3.588234, 2.870587], 'p_i': 80, 'u_i': 4.1932},
        {'id': 4, 'e_m': 2.653896, 'e_o_k': [1.522727, 1.218182, 0.974546], 'p_i': 80, 'u_i': 2.7154},
        {'id': 5, 'e_m': 2.164181, 'e_o_k': [1.241743, 0.993395, 0.794716], 'p_i': 40, 'u_i': 4.3253},
        {'id': 6, 'e_m': 2.331763, 'e_o_k': [1.337897, 1.070317, 0.856254], 'p_i': 80, 'u_i': 1.0005},
        {'id': 7, 'e_m': 1.096363, 'e_o_k': [0.629061, 0.503249, 0.402599], 'p_i': 40, 'u_i': 1.9051},
    ]
    B_BUDGET = 88.319992
    return processors, tasks, B_BUDGET
