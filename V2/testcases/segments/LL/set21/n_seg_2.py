"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.345721, 'e_o_k': [0.096034, 0.076827], 'p_i': 10, 'u_i': 2.6945},
        {'id': 1, 'e_m': 1.825589, 'e_o_k': [0.507108, 0.405686], 'p_i': 20, 'u_i': 2.2851},
        {'id': 2, 'e_m': 2.684855, 'e_o_k': [0.745793, 0.596634], 'p_i': 40, 'u_i': 1.9156},
        {'id': 3, 'e_m': 4.826850, 'e_o_k': [1.340792, 1.072633], 'p_i': 80, 'u_i': 2.3867},
        {'id': 4, 'e_m': 0.378406, 'e_o_k': [0.105113, 0.084090], 'p_i': 10, 'u_i': 1.9527},
        {'id': 5, 'e_m': 0.374820, 'e_o_k': [0.104117, 0.083293], 'p_i': 10, 'u_i': 2.5555},
        {'id': 6, 'e_m': 3.374313, 'e_o_k': [0.937309, 0.749847], 'p_i': 80, 'u_i': 2.5749},
        {'id': 7, 'e_m': 1.167596, 'e_o_k': [0.324332, 0.259466], 'p_i': 40, 'u_i': 4.5972},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET
