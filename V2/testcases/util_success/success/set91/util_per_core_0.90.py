"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279997, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279997, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.229741, 'e_o_k': [0.151198, 0.120958, 0.096766], 'p_i': 10, 'u_i': 1.0994},
        {'id': 1, 'e_m': 1.968949, 'e_o_k': [0.160108, 0.128087, 0.102469, 0.081976, 0.065580, 0.052464], 'p_i': 20, 'u_i': 4.8716},
        {'id': 2, 'e_m': 17.782666, 'e_o_k': [1.446027, 1.156822, 0.925458, 0.740366, 0.592293, 0.473834], 'p_i': 40, 'u_i': 3.1304},
        {'id': 3, 'e_m': 4.406668, 'e_o_k': [0.447832, 0.358266, 0.286613, 0.229290], 'p_i': 80, 'u_i': 4.2274},
        {'id': 4, 'e_m': 16.987013, 'e_o_k': [1.381328, 1.105062, 0.884050, 0.707240, 0.565792, 0.452633], 'p_i': 40, 'u_i': 1.7494},
        {'id': 5, 'e_m': 1.756028, 'e_o_k': [0.178458, 0.142766, 0.114213, 0.091371], 'p_i': 10, 'u_i': 4.2042},
        {'id': 6, 'e_m': 18.771979, 'e_o_k': [2.308030, 1.846424, 1.477139], 'p_i': 80, 'u_i': 1.0373},
        {'id': 7, 'e_m': 9.760024, 'e_o_k': [1.626671, 1.301337], 'p_i': 40, 'u_i': 1.4059},
    ]
    B_BUDGET = 215.279997
    return processors, tasks, B_BUDGET
