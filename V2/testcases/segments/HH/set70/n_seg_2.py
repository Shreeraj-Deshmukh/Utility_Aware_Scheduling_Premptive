"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.121191, 'e_o_k': [0.872038, 0.697630], 'p_i': 10, 'u_i': 2.9208},
        {'id': 1, 'e_m': 4.546458, 'e_o_k': [3.536134, 2.828907], 'p_i': 20, 'u_i': 4.6519},
        {'id': 2, 'e_m': 10.573229, 'e_o_k': [8.223622, 6.578898], 'p_i': 40, 'u_i': 4.9020},
        {'id': 3, 'e_m': 3.680258, 'e_o_k': [2.862423, 2.289939], 'p_i': 80, 'u_i': 4.4826},
        {'id': 4, 'e_m': 0.623936, 'e_o_k': [0.485283, 0.388227], 'p_i': 80, 'u_i': 1.3844},
        {'id': 5, 'e_m': 3.160733, 'e_o_k': [2.458348, 1.966678], 'p_i': 40, 'u_i': 3.8571},
        {'id': 6, 'e_m': 4.750875, 'e_o_k': [3.695125, 2.956100], 'p_i': 80, 'u_i': 3.6185},
        {'id': 7, 'e_m': 0.080412, 'e_o_k': [0.062542, 0.050034], 'p_i': 20, 'u_i': 1.1495},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
