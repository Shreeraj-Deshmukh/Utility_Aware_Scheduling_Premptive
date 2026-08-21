"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359992, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359992, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.195798, 'e_o_k': [0.223150, 0.178520, 0.142816, 0.114253], 'p_i': 10, 'u_i': 3.8216},
        {'id': 1, 'e_m': 2.111777, 'e_o_k': [0.259645, 0.207716, 0.166173], 'p_i': 20, 'u_i': 4.3612},
        {'id': 2, 'e_m': 18.498659, 'e_o_k': [1.879945, 1.503956, 1.203165, 0.962532], 'p_i': 40, 'u_i': 2.3108},
        {'id': 3, 'e_m': 9.980987, 'e_o_k': [1.014328, 0.811462, 0.649170, 0.519336], 'p_i': 80, 'u_i': 1.0383},
        {'id': 4, 'e_m': 0.984280, 'e_o_k': [0.164047, 0.131237], 'p_i': 20, 'u_i': 2.0614},
        {'id': 5, 'e_m': 3.178416, 'e_o_k': [0.323010, 0.258408, 0.206726, 0.165381], 'p_i': 10, 'u_i': 4.6739},
        {'id': 6, 'e_m': 0.258724, 'e_o_k': [0.026293, 0.021034, 0.016828, 0.013462], 'p_i': 10, 'u_i': 3.1717},
        {'id': 7, 'e_m': 5.893490, 'e_o_k': [0.479239, 0.383391, 0.306713, 0.245370, 0.196296, 0.157037], 'p_i': 20, 'u_i': 4.1313},
    ]
    B_BUDGET = 191.359992
    return processors, tasks, B_BUDGET
