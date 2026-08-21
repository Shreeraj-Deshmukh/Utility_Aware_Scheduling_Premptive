"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439991, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439991, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.459914, 'e_o_k': [0.243319, 0.194655], 'p_i': 10, 'u_i': 4.4926},
        {'id': 1, 'e_m': 3.610161, 'e_o_k': [0.443872, 0.355098, 0.284078], 'p_i': 20, 'u_i': 3.2922},
        {'id': 2, 'e_m': 3.796237, 'e_o_k': [0.632706, 0.506165], 'p_i': 40, 'u_i': 3.7450},
        {'id': 3, 'e_m': 22.797225, 'e_o_k': [2.316791, 1.853433, 1.482746, 1.186197], 'p_i': 80, 'u_i': 4.8771},
        {'id': 4, 'e_m': 0.492636, 'e_o_k': [0.082106, 0.065685], 'p_i': 20, 'u_i': 4.0203},
        {'id': 5, 'e_m': 2.120506, 'e_o_k': [0.215499, 0.172399, 0.137919, 0.110335], 'p_i': 10, 'u_i': 3.4418},
        {'id': 6, 'e_m': 2.073658, 'e_o_k': [0.254958, 0.203966, 0.163173], 'p_i': 10, 'u_i': 4.8003},
        {'id': 7, 'e_m': 2.495810, 'e_o_k': [0.306862, 0.245490, 0.196392], 'p_i': 10, 'u_i': 3.9154},
    ]
    B_BUDGET = 167.439991
    return processors, tasks, B_BUDGET
