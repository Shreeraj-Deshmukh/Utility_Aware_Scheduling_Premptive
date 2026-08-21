"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679995, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679995, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.443349, 'e_o_k': [0.128809, 0.103047, 0.082438, 0.065950, 0.052760], 'p_i': 10, 'u_i': 4.7302},
        {'id': 1, 'e_m': 4.992277, 'e_o_k': [0.832046, 0.665637], 'p_i': 20, 'u_i': 1.8342},
        {'id': 2, 'e_m': 1.773001, 'e_o_k': [0.217992, 0.174394, 0.139515], 'p_i': 40, 'u_i': 2.1428},
        {'id': 3, 'e_m': 4.820922, 'e_o_k': [0.489931, 0.391945, 0.313556, 0.250845], 'p_i': 80, 'u_i': 3.7337},
        {'id': 4, 'e_m': 5.896724, 'e_o_k': [0.526243, 0.420994, 0.336795, 0.269436, 0.215549], 'p_i': 40, 'u_i': 3.4112},
        {'id': 5, 'e_m': 9.193774, 'e_o_k': [1.532296, 1.225837], 'p_i': 80, 'u_i': 2.7179},
        {'id': 6, 'e_m': 0.009519, 'e_o_k': [0.000967, 0.000774, 0.000619, 0.000495], 'p_i': 40, 'u_i': 2.6898},
        {'id': 7, 'e_m': 0.777730, 'e_o_k': [0.095622, 0.076498, 0.061198], 'p_i': 20, 'u_i': 4.5690},
    ]
    B_BUDGET = 95.679995
    return processors, tasks, B_BUDGET
