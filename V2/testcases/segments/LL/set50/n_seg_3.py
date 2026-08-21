"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.597822, 'e_o_k': [0.122505, 0.098004, 0.078403], 'p_i': 10, 'u_i': 1.3138},
        {'id': 1, 'e_m': 0.537328, 'e_o_k': [0.110108, 0.088087, 0.070469], 'p_i': 20, 'u_i': 3.5906},
        {'id': 2, 'e_m': 1.853768, 'e_o_k': [0.379870, 0.303896, 0.243117], 'p_i': 40, 'u_i': 2.7107},
        {'id': 3, 'e_m': 4.965351, 'e_o_k': [1.017490, 0.813992, 0.651194], 'p_i': 80, 'u_i': 4.0673},
        {'id': 4, 'e_m': 0.125857, 'e_o_k': [0.025790, 0.020632, 0.016506], 'p_i': 10, 'u_i': 2.2713},
        {'id': 5, 'e_m': 0.986987, 'e_o_k': [0.202251, 0.161801, 0.129441], 'p_i': 80, 'u_i': 2.2740},
        {'id': 6, 'e_m': 11.937053, 'e_o_k': [2.446117, 1.956894, 1.565515], 'p_i': 80, 'u_i': 2.9164},
        {'id': 7, 'e_m': 1.232163, 'e_o_k': [0.252493, 0.201994, 0.161595], 'p_i': 40, 'u_i': 4.5766},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
