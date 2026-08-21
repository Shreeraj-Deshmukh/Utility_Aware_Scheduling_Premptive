"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319991, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319991, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.490613, 'e_o_k': [0.186177, 0.148941, 0.119153, 0.095323, 0.076258, 0.061006], 'p_i': 10, 'u_i': 4.9438},
        {'id': 1, 'e_m': 0.074164, 'e_o_k': [0.028144, 0.022515, 0.018012, 0.014410, 0.011528, 0.009222], 'p_i': 20, 'u_i': 2.3791},
        {'id': 2, 'e_m': 4.192385, 'e_o_k': [3.260744, 2.608595], 'p_i': 40, 'u_i': 3.1569},
        {'id': 3, 'e_m': 3.073173, 'e_o_k': [1.457467, 1.165974, 0.932779, 0.746223], 'p_i': 80, 'u_i': 2.0315},
        {'id': 4, 'e_m': 0.152558, 'e_o_k': [0.063536, 0.050828, 0.040663, 0.032530, 0.026024], 'p_i': 10, 'u_i': 1.5871},
        {'id': 5, 'e_m': 3.775007, 'e_o_k': [2.936117, 2.348893], 'p_i': 20, 'u_i': 1.8711},
    ]
    B_BUDGET = 88.319991
    return processors, tasks, B_BUDGET
