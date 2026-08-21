"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319995, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319995, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.597822, 'e_o_k': [0.343013, 0.274410, 0.219528], 'p_i': 10, 'u_i': 1.3138},
        {'id': 1, 'e_m': 0.537328, 'e_o_k': [0.308303, 0.246642, 0.197314], 'p_i': 20, 'u_i': 3.5906},
        {'id': 2, 'e_m': 1.853768, 'e_o_k': [1.063637, 0.850910, 0.680728], 'p_i': 40, 'u_i': 2.7107},
        {'id': 3, 'e_m': 4.965351, 'e_o_k': [2.848972, 2.279177, 1.823342], 'p_i': 80, 'u_i': 4.0673},
        {'id': 4, 'e_m': 0.125857, 'e_o_k': [0.072213, 0.057771, 0.046216], 'p_i': 10, 'u_i': 2.2713},
        {'id': 5, 'e_m': 0.986987, 'e_o_k': [0.566304, 0.453043, 0.362435], 'p_i': 80, 'u_i': 2.2740},
        {'id': 6, 'e_m': 11.937053, 'e_o_k': [6.849129, 5.479303, 4.383442], 'p_i': 80, 'u_i': 2.9164},
        {'id': 7, 'e_m': 1.232163, 'e_o_k': [0.706979, 0.565583, 0.452467], 'p_i': 40, 'u_i': 4.5766},
    ]
    B_BUDGET = 88.319995
    return processors, tasks, B_BUDGET
