"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.465316, 'e_o_k': [0.129255, 0.103404], 'p_i': 10, 'u_i': 3.1458},
        {'id': 1, 'e_m': 1.632139, 'e_o_k': [0.453372, 0.362698], 'p_i': 20, 'u_i': 4.9683},
        {'id': 2, 'e_m': 1.388565, 'e_o_k': [0.385712, 0.308570], 'p_i': 40, 'u_i': 2.4718},
        {'id': 3, 'e_m': 4.132141, 'e_o_k': [1.147817, 0.918253], 'p_i': 80, 'u_i': 3.8875},
        {'id': 4, 'e_m': 1.499437, 'e_o_k': [0.416510, 0.333208], 'p_i': 80, 'u_i': 3.3599},
        {'id': 5, 'e_m': 0.197682, 'e_o_k': [0.054912, 0.043929], 'p_i': 40, 'u_i': 3.9269},
        {'id': 6, 'e_m': 1.272876, 'e_o_k': [0.353577, 0.282861], 'p_i': 10, 'u_i': 3.4836},
        {'id': 7, 'e_m': 1.380915, 'e_o_k': [0.383587, 0.306870], 'p_i': 40, 'u_i': 2.8974},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
