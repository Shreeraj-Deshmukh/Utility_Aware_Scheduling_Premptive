"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119989, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119989, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.646968, 'e_o_k': [0.414710, 0.331768, 0.265415, 0.212332, 0.169865], 'p_i': 10, 'u_i': 3.8434},
        {'id': 1, 'e_m': 0.976716, 'e_o_k': [0.162786, 0.130229], 'p_i': 20, 'u_i': 3.7460},
        {'id': 2, 'e_m': 7.884487, 'e_o_k': [0.801269, 0.641015, 0.512812, 0.410250], 'p_i': 40, 'u_i': 2.3844},
        {'id': 3, 'e_m': 9.618742, 'e_o_k': [1.603124, 1.282499], 'p_i': 80, 'u_i': 3.6397},
        {'id': 4, 'e_m': 38.032676, 'e_o_k': [3.092691, 2.474153, 1.979322, 1.583458, 1.266766, 1.013413], 'p_i': 80, 'u_i': 2.0089},
        {'id': 5, 'e_m': 8.529209, 'e_o_k': [0.866790, 0.693432, 0.554745, 0.443796], 'p_i': 20, 'u_i': 4.2973},
        {'id': 6, 'e_m': 0.611273, 'e_o_k': [0.101879, 0.081503], 'p_i': 10, 'u_i': 3.5880},
        {'id': 7, 'e_m': 8.122494, 'e_o_k': [0.660494, 0.528395, 0.422716, 0.338173, 0.270538, 0.216431], 'p_i': 20, 'u_i': 4.0384},
    ]
    B_BUDGET = 263.119989
    return processors, tasks, B_BUDGET
