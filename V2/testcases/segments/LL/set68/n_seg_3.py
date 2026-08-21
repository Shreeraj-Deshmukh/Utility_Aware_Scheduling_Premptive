"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199993, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199993, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.465316, 'e_o_k': [0.095352, 0.076281, 0.061025], 'p_i': 10, 'u_i': 3.1458},
        {'id': 1, 'e_m': 1.632139, 'e_o_k': [0.334455, 0.267564, 0.214051], 'p_i': 20, 'u_i': 4.9683},
        {'id': 2, 'e_m': 1.388565, 'e_o_k': [0.284542, 0.227634, 0.182107], 'p_i': 40, 'u_i': 2.4718},
        {'id': 3, 'e_m': 4.132141, 'e_o_k': [0.846750, 0.677400, 0.541920], 'p_i': 80, 'u_i': 3.8875},
        {'id': 4, 'e_m': 1.499437, 'e_o_k': [0.307262, 0.245809, 0.196647], 'p_i': 80, 'u_i': 3.3599},
        {'id': 5, 'e_m': 0.197682, 'e_o_k': [0.040509, 0.032407, 0.025926], 'p_i': 40, 'u_i': 3.9269},
        {'id': 6, 'e_m': 1.272876, 'e_o_k': [0.260835, 0.208668, 0.166935], 'p_i': 10, 'u_i': 3.4836},
        {'id': 7, 'e_m': 1.380915, 'e_o_k': [0.282974, 0.226379, 0.181104], 'p_i': 40, 'u_i': 2.8974},
    ]
    B_BUDGET = 55.199993
    return processors, tasks, B_BUDGET
