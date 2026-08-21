"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280009, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280009, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.802065, 'e_o_k': [0.339309, 0.271447, 0.217157, 0.173726, 0.138981], 'p_i': 10, 'u_i': 3.8434},
        {'id': 1, 'e_m': 0.799131, 'e_o_k': [0.133189, 0.106551], 'p_i': 20, 'u_i': 3.7460},
        {'id': 2, 'e_m': 6.450944, 'e_o_k': [0.655584, 0.524467, 0.419574, 0.335659], 'p_i': 40, 'u_i': 2.3844},
        {'id': 3, 'e_m': 7.869880, 'e_o_k': [1.311647, 1.049317], 'p_i': 80, 'u_i': 3.6397},
        {'id': 4, 'e_m': 31.117644, 'e_o_k': [2.530383, 2.024307, 1.619445, 1.295556, 1.036445, 0.829156], 'p_i': 80, 'u_i': 2.0089},
        {'id': 5, 'e_m': 6.978444, 'e_o_k': [0.709191, 0.567353, 0.453883, 0.363106], 'p_i': 20, 'u_i': 4.2973},
        {'id': 6, 'e_m': 0.500133, 'e_o_k': [0.083355, 0.066684], 'p_i': 10, 'u_i': 3.5880},
        {'id': 7, 'e_m': 6.645677, 'e_o_k': [0.540404, 0.432324, 0.345859, 0.276687, 0.221350, 0.177080], 'p_i': 20, 'u_i': 4.0384},
    ]
    B_BUDGET = 215.280009
    return processors, tasks, B_BUDGET
