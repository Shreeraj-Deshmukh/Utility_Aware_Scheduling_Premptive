"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439975, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439975, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.410386, 'e_o_k': [0.173408, 0.138726, 0.110981], 'p_i': 10, 'u_i': 3.7384},
        {'id': 1, 'e_m': 3.126766, 'e_o_k': [0.254258, 0.203407, 0.162725, 0.130180, 0.104144, 0.083315], 'p_i': 20, 'u_i': 1.0034},
        {'id': 2, 'e_m': 16.985859, 'e_o_k': [1.515873, 1.212698, 0.970159, 0.776127, 0.620901], 'p_i': 40, 'u_i': 2.3713},
        {'id': 3, 'e_m': 14.262456, 'e_o_k': [1.159776, 0.927820, 0.742256, 0.593805, 0.475044, 0.380035], 'p_i': 80, 'u_i': 1.9623},
        {'id': 4, 'e_m': 1.513998, 'e_o_k': [0.135114, 0.108091, 0.086473, 0.069178, 0.055343], 'p_i': 10, 'u_i': 1.2428},
        {'id': 5, 'e_m': 0.349778, 'e_o_k': [0.031215, 0.024972, 0.019978, 0.015982, 0.012786], 'p_i': 20, 'u_i': 4.6455},
        {'id': 6, 'e_m': 0.935035, 'e_o_k': [0.095024, 0.076019, 0.060815, 0.048652], 'p_i': 10, 'u_i': 2.5101},
        {'id': 7, 'e_m': 9.492148, 'e_o_k': [1.167067, 0.933654, 0.746923], 'p_i': 40, 'u_i': 1.7945},
    ]
    B_BUDGET = 167.439975
    return processors, tasks, B_BUDGET
