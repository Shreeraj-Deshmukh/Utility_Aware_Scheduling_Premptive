"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64001, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.64001, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.599440, 'e_o_k': [1.244009, 0.995207], 'p_i': 10, 'u_i': 2.3541},
        {'id': 1, 'e_m': 5.185523, 'e_o_k': [4.033185, 3.226548], 'p_i': 20, 'u_i': 4.5958},
        {'id': 2, 'e_m': 2.922224, 'e_o_k': [2.272841, 1.818273], 'p_i': 40, 'u_i': 4.0042},
        {'id': 3, 'e_m': 7.584490, 'e_o_k': [5.899048, 4.719239], 'p_i': 80, 'u_i': 1.4529},
        {'id': 4, 'e_m': 1.038987, 'e_o_k': [0.808101, 0.646481], 'p_i': 40, 'u_i': 3.3706},
        {'id': 5, 'e_m': 1.421690, 'e_o_k': [1.105759, 0.884607], 'p_i': 20, 'u_i': 1.2465},
        {'id': 6, 'e_m': 3.169787, 'e_o_k': [2.465390, 1.972312], 'p_i': 40, 'u_i': 3.7304},
        {'id': 7, 'e_m': 0.366143, 'e_o_k': [0.284778, 0.227822], 'p_i': 10, 'u_i': 3.6440},
    ]
    B_BUDGET = 176.640010
    return processors, tasks, B_BUDGET
