"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320011, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.320011, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.446887, 'e_o_k': [0.347579, 0.278063], 'p_i': 10, 'u_i': 4.1325},
        {'id': 1, 'e_m': 0.001026, 'e_o_k': [0.000798, 0.000638], 'p_i': 20, 'u_i': 2.4718},
        {'id': 2, 'e_m': 6.562599, 'e_o_k': [5.104244, 4.083395], 'p_i': 40, 'u_i': 2.6491},
        {'id': 3, 'e_m': 2.341741, 'e_o_k': [1.821354, 1.457083], 'p_i': 80, 'u_i': 3.7785},
        {'id': 4, 'e_m': 0.177678, 'e_o_k': [0.138194, 0.110555], 'p_i': 10, 'u_i': 2.0110},
        {'id': 5, 'e_m': 0.341853, 'e_o_k': [0.265885, 0.212708], 'p_i': 10, 'u_i': 2.7392},
        {'id': 6, 'e_m': 6.037977, 'e_o_k': [4.696204, 3.756963], 'p_i': 80, 'u_i': 4.5700},
        {'id': 7, 'e_m': 0.689911, 'e_o_k': [0.536598, 0.429278], 'p_i': 20, 'u_i': 2.3393},
    ]
    B_BUDGET = 88.320011
    return processors, tasks, B_BUDGET
