"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.39999, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.39999, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.396008, 'e_o_k': [0.081149, 0.064919, 0.051935], 'p_i': 10, 'u_i': 2.2582},
        {'id': 1, 'e_m': 1.438192, 'e_o_k': [0.294711, 0.235769, 0.188615], 'p_i': 20, 'u_i': 2.9332},
        {'id': 2, 'e_m': 0.174158, 'e_o_k': [0.035688, 0.028551, 0.022840], 'p_i': 40, 'u_i': 1.0372},
        {'id': 3, 'e_m': 2.213172, 'e_o_k': [0.453519, 0.362815, 0.290252], 'p_i': 80, 'u_i': 1.7921},
        {'id': 4, 'e_m': 8.410664, 'e_o_k': [1.723497, 1.378797, 1.103038], 'p_i': 40, 'u_i': 3.3121},
        {'id': 5, 'e_m': 14.019005, 'e_o_k': [2.872747, 2.298197, 1.838558], 'p_i': 40, 'u_i': 3.7636},
        {'id': 6, 'e_m': 1.468623, 'e_o_k': [0.300947, 0.240758, 0.192606], 'p_i': 80, 'u_i': 1.1326},
        {'id': 7, 'e_m': 6.189722, 'e_o_k': [1.268386, 1.014708, 0.811767], 'p_i': 80, 'u_i': 3.1203},
    ]
    B_BUDGET = 110.399990
    return processors, tasks, B_BUDGET
