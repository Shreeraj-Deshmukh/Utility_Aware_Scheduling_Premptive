"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360005, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360005, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.474455, 'e_o_k': [0.579076, 0.463261], 'p_i': 10, 'u_i': 1.8132},
        {'id': 1, 'e_m': 2.828128, 'e_o_k': [0.229974, 0.183979, 0.147183, 0.117747, 0.094197, 0.075358], 'p_i': 20, 'u_i': 1.3118},
        {'id': 2, 'e_m': 17.789923, 'e_o_k': [1.587630, 1.270104, 1.016083, 0.812867, 0.650293], 'p_i': 40, 'u_i': 1.6432},
        {'id': 3, 'e_m': 7.984641, 'e_o_k': [1.330774, 1.064619], 'p_i': 80, 'u_i': 3.2827},
        {'id': 4, 'e_m': 0.312043, 'e_o_k': [0.027848, 0.022278, 0.017823, 0.014258, 0.011406], 'p_i': 20, 'u_i': 1.0597},
        {'id': 5, 'e_m': 0.704355, 'e_o_k': [0.086601, 0.069281, 0.055425], 'p_i': 20, 'u_i': 4.4596},
        {'id': 6, 'e_m': 10.254176, 'e_o_k': [1.042091, 0.833673, 0.666938, 0.533551], 'p_i': 40, 'u_i': 4.8824},
        {'id': 7, 'e_m': 2.594177, 'e_o_k': [0.318956, 0.255165, 0.204132], 'p_i': 10, 'u_i': 1.5609},
    ]
    B_BUDGET = 191.360005
    return processors, tasks, B_BUDGET
