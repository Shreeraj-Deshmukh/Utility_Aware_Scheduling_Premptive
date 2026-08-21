"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 114.079993, "H": 80, "J": 34, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.5, "seed": 1027, "set": 27, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.50"}
"""

_SPEC = '{"B": 114.079993, "H": 80, "J": 34, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.5, "seed": 1027, "set": 27, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.707837, 'e_o_k': [0.809950, 0.647960, 0.518368, 0.414694], 'p_i': 10, 'u_i': 3.9517},
        {'id': 1, 'e_m': 0.074416, 'e_o_k': [0.030992, 0.024794, 0.019835, 0.015868, 0.012694], 'p_i': 20, 'u_i': 3.7467},
        {'id': 2, 'e_m': 1.043073, 'e_o_k': [0.434407, 0.347525, 0.278020, 0.222416, 0.177933], 'p_i': 40, 'u_i': 4.6120},
        {'id': 3, 'e_m': 0.422237, 'e_o_k': [0.328407, 0.262725], 'p_i': 80, 'u_i': 4.9202},
        {'id': 4, 'e_m': 0.946737, 'e_o_k': [0.736351, 0.589081], 'p_i': 80, 'u_i': 4.2451},
        {'id': 5, 'e_m': 0.544998, 'e_o_k': [0.423887, 0.339110], 'p_i': 10, 'u_i': 4.7909},
        {'id': 6, 'e_m': 1.274474, 'e_o_k': [0.604425, 0.483540, 0.386832, 0.309466], 'p_i': 10, 'u_i': 3.3523},
        {'id': 7, 'e_m': 0.014372, 'e_o_k': [0.006816, 0.005453, 0.004362, 0.003490], 'p_i': 40, 'u_i': 1.0347},
    ]
    B_BUDGET = 114.079993
    return processors, tasks, B_BUDGET
