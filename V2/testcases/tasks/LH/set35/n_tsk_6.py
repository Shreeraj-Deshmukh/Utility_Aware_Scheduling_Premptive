"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32001, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.32001, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.212980, 'e_o_k': [0.080821, 0.064657, 0.051726, 0.041381, 0.033104, 0.026484], 'p_i': 10, 'u_i': 3.7793},
        {'id': 1, 'e_m': 0.218042, 'e_o_k': [0.103407, 0.082726, 0.066181, 0.052945], 'p_i': 20, 'u_i': 1.9533},
        {'id': 2, 'e_m': 3.500668, 'e_o_k': [1.660209, 1.328167, 1.062533, 0.850027], 'p_i': 40, 'u_i': 2.6246},
        {'id': 3, 'e_m': 10.920079, 'e_o_k': [4.143928, 3.315142, 2.652114, 2.121691, 1.697353, 1.357882], 'p_i': 80, 'u_i': 2.3478},
        {'id': 4, 'e_m': 10.673673, 'e_o_k': [6.124239, 4.899391, 3.919513], 'p_i': 80, 'u_i': 2.5491},
        {'id': 5, 'e_m': 0.103613, 'e_o_k': [0.043151, 0.034521, 0.027617, 0.022094, 0.017675], 'p_i': 10, 'u_i': 2.9783},
    ]
    B_BUDGET = 88.320010
    return processors, tasks, B_BUDGET
