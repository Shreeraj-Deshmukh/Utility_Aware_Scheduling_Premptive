"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.68001, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.68001, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.573701, 'e_o_k': [0.140442, 0.112354, 0.089883, 0.071906, 0.057525], 'p_i': 10, 'u_i': 3.6650},
        {'id': 1, 'e_m': 1.488704, 'e_o_k': [0.121056, 0.096845, 0.077476, 0.061981, 0.049585, 0.039668], 'p_i': 20, 'u_i': 1.3163},
        {'id': 2, 'e_m': 1.136090, 'e_o_k': [0.115456, 0.092365, 0.073892, 0.059114], 'p_i': 40, 'u_i': 1.2768},
        {'id': 3, 'e_m': 13.753139, 'e_o_k': [1.690960, 1.352768, 1.082214], 'p_i': 80, 'u_i': 1.7506},
        {'id': 4, 'e_m': 5.982379, 'e_o_k': [0.735538, 0.588431, 0.470745], 'p_i': 40, 'u_i': 4.5685},
        {'id': 5, 'e_m': 0.674012, 'e_o_k': [0.060151, 0.048121, 0.038497, 0.030797, 0.024638], 'p_i': 10, 'u_i': 2.7344},
        {'id': 6, 'e_m': 0.887834, 'e_o_k': [0.147972, 0.118378], 'p_i': 40, 'u_i': 1.1398},
        {'id': 7, 'e_m': 10.297741, 'e_o_k': [0.919004, 0.735203, 0.588162, 0.470530, 0.376424], 'p_i': 80, 'u_i': 4.8954},
    ]
    B_BUDGET = 95.680010
    return processors, tasks, B_BUDGET
