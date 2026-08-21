"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399997, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399997, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.548867, 'e_o_k': [0.092965, 0.074372, 0.059498, 0.047598], 'p_i': 10, 'u_i': 2.8575},
        {'id': 1, 'e_m': 2.063126, 'e_o_k': [0.306867, 0.245493, 0.196395, 0.157116, 0.125693], 'p_i': 20, 'u_i': 2.8209},
        {'id': 2, 'e_m': 0.270075, 'e_o_k': [0.075021, 0.060017], 'p_i': 40, 'u_i': 2.9332},
        {'id': 3, 'e_m': 4.026670, 'e_o_k': [0.825137, 0.660110, 0.528088], 'p_i': 80, 'u_i': 1.0372},
        {'id': 4, 'e_m': 4.012113, 'e_o_k': [0.822154, 0.657723, 0.526179], 'p_i': 10, 'u_i': 1.7921},
        {'id': 5, 'e_m': 7.346417, 'e_o_k': [0.995644, 0.796515, 0.637212, 0.509770, 0.407816, 0.326253], 'p_i': 40, 'u_i': 1.1296},
    ]
    B_BUDGET = 110.399997
    return processors, tasks, B_BUDGET
