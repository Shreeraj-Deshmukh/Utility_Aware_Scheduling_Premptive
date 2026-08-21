"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199986, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199986, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.539503, 'e_o_k': [0.423251, 0.338600], 'p_i': 10, 'u_i': 2.9155},
        {'id': 1, 'e_m': 1.974787, 'e_o_k': [0.160583, 0.128466, 0.102773, 0.082219, 0.065775, 0.052620], 'p_i': 20, 'u_i': 4.9157},
        {'id': 2, 'e_m': 18.029552, 'e_o_k': [1.466103, 1.172883, 0.938306, 0.750645, 0.600516, 0.480413], 'p_i': 40, 'u_i': 2.9652},
        {'id': 3, 'e_m': 28.559838, 'e_o_k': [2.902423, 2.321938, 1.857550, 1.486040], 'p_i': 80, 'u_i': 4.8689},
        {'id': 4, 'e_m': 14.705456, 'e_o_k': [1.195799, 0.956639, 0.765311, 0.612249, 0.489799, 0.391839], 'p_i': 40, 'u_i': 4.7382},
        {'id': 5, 'e_m': 0.577266, 'e_o_k': [0.070975, 0.056780, 0.045424], 'p_i': 10, 'u_i': 1.0574},
        {'id': 6, 'e_m': 10.093225, 'e_o_k': [1.025734, 0.820587, 0.656470, 0.525176], 'p_i': 80, 'u_i': 3.6223},
        {'id': 7, 'e_m': 23.043618, 'e_o_k': [3.840603, 3.072482], 'p_i': 80, 'u_i': 4.9982},
    ]
    B_BUDGET = 239.199986
    return processors, tasks, B_BUDGET
