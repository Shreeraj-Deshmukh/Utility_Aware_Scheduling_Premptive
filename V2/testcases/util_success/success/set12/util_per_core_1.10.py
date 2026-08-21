"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120016, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120016, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.494140, 'e_o_k': [0.306657, 0.245325, 0.196260], 'p_i': 10, 'u_i': 1.4024},
        {'id': 1, 'e_m': 4.506756, 'e_o_k': [0.366474, 0.293180, 0.234544, 0.187635, 0.150108, 0.120086], 'p_i': 20, 'u_i': 4.6474},
        {'id': 2, 'e_m': 10.275771, 'e_o_k': [1.044286, 0.835429, 0.668343, 0.534674], 'p_i': 40, 'u_i': 4.0494},
        {'id': 3, 'e_m': 28.593968, 'e_o_k': [4.765661, 3.812529], 'p_i': 80, 'u_i': 4.1857},
        {'id': 4, 'e_m': 6.476066, 'e_o_k': [0.526612, 0.421290, 0.337032, 0.269625, 0.215700, 0.172560], 'p_i': 20, 'u_i': 4.7496},
        {'id': 5, 'e_m': 5.655370, 'e_o_k': [0.695332, 0.556266, 0.445013], 'p_i': 40, 'u_i': 3.3289},
        {'id': 6, 'e_m': 3.763579, 'e_o_k': [0.382478, 0.305982, 0.244786, 0.195829], 'p_i': 10, 'u_i': 2.7151},
        {'id': 7, 'e_m': 2.693839, 'e_o_k': [0.331210, 0.264968, 0.211974], 'p_i': 10, 'u_i': 3.1117},
    ]
    B_BUDGET = 263.120016
    return processors, tasks, B_BUDGET
