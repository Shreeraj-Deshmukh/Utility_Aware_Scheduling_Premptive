"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319995, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319995, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.465316, 'e_o_k': [0.361913, 0.289530], 'p_i': 10, 'u_i': 3.1458},
        {'id': 1, 'e_m': 1.632139, 'e_o_k': [1.269442, 1.015553], 'p_i': 20, 'u_i': 4.9683},
        {'id': 2, 'e_m': 1.388565, 'e_o_k': [1.079995, 0.863996], 'p_i': 40, 'u_i': 2.4718},
        {'id': 3, 'e_m': 4.132141, 'e_o_k': [3.213887, 2.571110], 'p_i': 80, 'u_i': 3.8875},
        {'id': 4, 'e_m': 1.499437, 'e_o_k': [1.166228, 0.932983], 'p_i': 80, 'u_i': 3.3599},
        {'id': 5, 'e_m': 0.197682, 'e_o_k': [0.153753, 0.123002], 'p_i': 40, 'u_i': 3.9269},
        {'id': 6, 'e_m': 1.272876, 'e_o_k': [0.990015, 0.792012], 'p_i': 10, 'u_i': 3.4836},
        {'id': 7, 'e_m': 1.380915, 'e_o_k': [1.074045, 0.859236], 'p_i': 40, 'u_i': 2.8974},
    ]
    B_BUDGET = 88.319995
    return processors, tasks, B_BUDGET
