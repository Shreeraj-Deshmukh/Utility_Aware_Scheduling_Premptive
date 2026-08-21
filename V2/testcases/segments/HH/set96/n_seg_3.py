"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.505787, 'e_o_k': [0.290205, 0.232164, 0.185731], 'p_i': 10, 'u_i': 2.8589},
        {'id': 1, 'e_m': 0.195219, 'e_o_k': [0.112011, 0.089609, 0.071687], 'p_i': 20, 'u_i': 2.7598},
        {'id': 2, 'e_m': 10.184228, 'e_o_k': [5.843409, 4.674727, 3.739782], 'p_i': 40, 'u_i': 2.0735},
        {'id': 3, 'e_m': 6.561179, 'e_o_k': [3.764611, 3.011689, 2.409351], 'p_i': 80, 'u_i': 1.1592},
        {'id': 4, 'e_m': 4.539403, 'e_o_k': [2.604575, 2.083660, 1.666928], 'p_i': 20, 'u_i': 2.2796},
        {'id': 5, 'e_m': 6.765491, 'e_o_k': [3.881839, 3.105471, 2.484377], 'p_i': 80, 'u_i': 4.8637},
        {'id': 6, 'e_m': 1.084629, 'e_o_k': [0.622328, 0.497862, 0.398290], 'p_i': 20, 'u_i': 2.9768},
        {'id': 7, 'e_m': 0.372698, 'e_o_k': [0.213843, 0.171074, 0.136860], 'p_i': 10, 'u_i': 1.8410},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET
