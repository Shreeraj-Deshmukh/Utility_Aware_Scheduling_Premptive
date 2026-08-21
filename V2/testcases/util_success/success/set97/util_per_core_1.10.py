"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120031, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120031, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.996072, 'e_o_k': [0.166012, 0.132810], 'p_i': 10, 'u_i': 4.2349},
        {'id': 1, 'e_m': 0.966700, 'e_o_k': [0.078609, 0.062887, 0.050310, 0.040248, 0.032198, 0.025759], 'p_i': 20, 'u_i': 1.9410},
        {'id': 2, 'e_m': 16.995133, 'e_o_k': [1.516700, 1.213360, 0.970688, 0.776551, 0.621240], 'p_i': 40, 'u_i': 2.4494},
        {'id': 3, 'e_m': 27.226295, 'e_o_k': [2.429762, 1.943810, 1.555048, 1.244038, 0.995231], 'p_i': 80, 'u_i': 4.2936},
        {'id': 4, 'e_m': 39.905569, 'e_o_k': [4.906422, 3.925138, 3.140110], 'p_i': 80, 'u_i': 4.6702},
        {'id': 5, 'e_m': 1.533829, 'e_o_k': [0.136884, 0.109507, 0.087606, 0.070085, 0.056068], 'p_i': 10, 'u_i': 1.5181},
        {'id': 6, 'e_m': 13.494717, 'e_o_k': [2.249120, 1.799296], 'p_i': 40, 'u_i': 3.3474},
        {'id': 7, 'e_m': 11.891218, 'e_o_k': [0.966954, 0.773563, 0.618851, 0.495081, 0.396064, 0.316852], 'p_i': 40, 'u_i': 3.4657},
    ]
    B_BUDGET = 263.120031
    return processors, tasks, B_BUDGET
