"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199987, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199987, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.680349, 'e_o_k': [0.136640, 0.109312, 0.087450, 0.069960, 0.055968, 0.044774], 'p_i': 10, 'u_i': 1.9884},
        {'id': 1, 'e_m': 4.468037, 'e_o_k': [0.549349, 0.439479, 0.351583], 'p_i': 20, 'u_i': 4.7767},
        {'id': 2, 'e_m': 1.484691, 'e_o_k': [0.150883, 0.120707, 0.096565, 0.077252], 'p_i': 40, 'u_i': 2.3478},
        {'id': 3, 'e_m': 36.025248, 'e_o_k': [4.429334, 3.543467, 2.834774], 'p_i': 80, 'u_i': 2.9933},
        {'id': 4, 'e_m': 30.395226, 'e_o_k': [5.065871, 4.052697], 'p_i': 80, 'u_i': 1.6969},
        {'id': 5, 'e_m': 23.083743, 'e_o_k': [2.345909, 1.876727, 1.501382, 1.201105], 'p_i': 80, 'u_i': 1.2841},
        {'id': 6, 'e_m': 1.514214, 'e_o_k': [0.186174, 0.148939, 0.119151], 'p_i': 40, 'u_i': 3.9852},
        {'id': 7, 'e_m': 33.183029, 'e_o_k': [3.372259, 2.697807, 2.158246, 1.726597], 'p_i': 80, 'u_i': 4.0749},
    ]
    B_BUDGET = 239.199987
    return processors, tasks, B_BUDGET
