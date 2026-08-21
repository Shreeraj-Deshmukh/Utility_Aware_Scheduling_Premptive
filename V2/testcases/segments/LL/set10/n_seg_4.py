"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "segments", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "segments", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.221612, 'e_o_k': [0.037536, 0.030029, 0.024023, 0.019218], 'p_i': 10, 'u_i': 2.5678},
        {'id': 1, 'e_m': 0.192518, 'e_o_k': [0.032608, 0.026087, 0.020869, 0.016695], 'p_i': 20, 'u_i': 3.0744},
        {'id': 2, 'e_m': 3.593476, 'e_o_k': [0.608651, 0.486921, 0.389537, 0.311629], 'p_i': 40, 'u_i': 3.1102},
        {'id': 3, 'e_m': 10.310356, 'e_o_k': [1.746334, 1.397067, 1.117654, 0.894123], 'p_i': 80, 'u_i': 3.9862},
        {'id': 4, 'e_m': 0.725770, 'e_o_k': [0.122929, 0.098343, 0.078674, 0.062939], 'p_i': 20, 'u_i': 1.5757},
        {'id': 5, 'e_m': 0.673150, 'e_o_k': [0.114016, 0.091213, 0.072970, 0.058376], 'p_i': 10, 'u_i': 4.9941},
        {'id': 6, 'e_m': 1.033969, 'e_o_k': [0.175130, 0.140104, 0.112083, 0.089667], 'p_i': 40, 'u_i': 1.7632},
        {'id': 7, 'e_m': 0.801753, 'e_o_k': [0.135798, 0.108639, 0.086911, 0.069529], 'p_i': 40, 'u_i': 1.4284},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
