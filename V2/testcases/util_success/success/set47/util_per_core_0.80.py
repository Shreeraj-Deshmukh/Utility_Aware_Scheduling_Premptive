"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359992, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359992, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.866872, 'e_o_k': [0.434335, 0.347468, 0.277975, 0.222380, 0.177904], 'p_i': 10, 'u_i': 3.4259},
        {'id': 1, 'e_m': 3.357329, 'e_o_k': [0.341192, 0.272954, 0.218363, 0.174690], 'p_i': 20, 'u_i': 1.3819},
        {'id': 2, 'e_m': 5.395435, 'e_o_k': [0.899239, 0.719391], 'p_i': 40, 'u_i': 1.7445},
        {'id': 3, 'e_m': 11.166836, 'e_o_k': [0.908050, 0.726440, 0.581152, 0.464922, 0.371937, 0.297550], 'p_i': 80, 'u_i': 3.6642},
        {'id': 4, 'e_m': 1.919933, 'e_o_k': [0.195115, 0.156092, 0.124874, 0.099899], 'p_i': 10, 'u_i': 2.6174},
        {'id': 5, 'e_m': 2.400733, 'e_o_k': [0.214249, 0.171399, 0.137119, 0.109696, 0.087756], 'p_i': 10, 'u_i': 2.3254},
        {'id': 6, 'e_m': 0.390655, 'e_o_k': [0.065109, 0.052087], 'p_i': 10, 'u_i': 3.2626},
        {'id': 7, 'e_m': 7.993717, 'e_o_k': [0.713385, 0.570708, 0.456566, 0.365253, 0.292203], 'p_i': 40, 'u_i': 1.6837},
    ]
    B_BUDGET = 191.359992
    return processors, tasks, B_BUDGET
