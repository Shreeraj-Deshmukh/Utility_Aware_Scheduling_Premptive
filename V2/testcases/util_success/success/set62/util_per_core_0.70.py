"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440003, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440003, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.369785, 'e_o_k': [0.037580, 0.030064, 0.024051, 0.019241], 'p_i': 10, 'u_i': 1.2796},
        {'id': 1, 'e_m': 8.248729, 'e_o_k': [0.838285, 0.670628, 0.536503, 0.429202], 'p_i': 20, 'u_i': 2.4526},
        {'id': 2, 'e_m': 15.930750, 'e_o_k': [1.958699, 1.566959, 1.253567], 'p_i': 40, 'u_i': 3.7482},
        {'id': 3, 'e_m': 10.044128, 'e_o_k': [0.896370, 0.717096, 0.573677, 0.458942, 0.367153], 'p_i': 80, 'u_i': 2.1247},
        {'id': 4, 'e_m': 4.904429, 'e_o_k': [0.498418, 0.398734, 0.318987, 0.255190], 'p_i': 40, 'u_i': 4.6336},
        {'id': 5, 'e_m': 1.810037, 'e_o_k': [0.222545, 0.178036, 0.142429], 'p_i': 80, 'u_i': 4.4629},
        {'id': 6, 'e_m': 1.343284, 'e_o_k': [0.119879, 0.095903, 0.076723, 0.061378, 0.049102], 'p_i': 10, 'u_i': 1.2397},
        {'id': 7, 'e_m': 1.472001, 'e_o_k': [0.149594, 0.119675, 0.095740, 0.076592], 'p_i': 10, 'u_i': 2.9672},
    ]
    B_BUDGET = 167.440003
    return processors, tasks, B_BUDGET
