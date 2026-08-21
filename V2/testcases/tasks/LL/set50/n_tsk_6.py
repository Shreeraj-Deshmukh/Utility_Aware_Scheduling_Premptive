"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199986, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199986, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.811137, 'e_o_k': [0.120647, 0.096518, 0.077214, 0.061772, 0.049417], 'p_i': 10, 'u_i': 4.0918},
        {'id': 1, 'e_m': 0.740340, 'e_o_k': [0.110117, 0.088094, 0.070475, 0.056380, 0.045104], 'p_i': 20, 'u_i': 2.7075},
        {'id': 2, 'e_m': 2.639818, 'e_o_k': [0.447124, 0.357699, 0.286159, 0.228927], 'p_i': 40, 'u_i': 3.4005},
        {'id': 3, 'e_m': 7.095740, 'e_o_k': [1.971039, 1.576831], 'p_i': 80, 'u_i': 3.5378},
        {'id': 4, 'e_m': 0.220210, 'e_o_k': [0.029845, 0.023876, 0.019101, 0.015280, 0.012224, 0.009779], 'p_i': 10, 'u_i': 2.8954},
        {'id': 5, 'e_m': 2.103121, 'e_o_k': [0.312815, 0.250252, 0.200202, 0.160162, 0.128129], 'p_i': 20, 'u_i': 2.6615},
    ]
    B_BUDGET = 55.199986
    return processors, tasks, B_BUDGET
