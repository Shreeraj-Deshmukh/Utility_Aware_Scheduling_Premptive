"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.31999, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.31999, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.075032, 'e_o_k': [0.836136, 0.668909], 'p_i': 10, 'u_i': 4.6321},
        {'id': 1, 'e_m': 0.138443, 'e_o_k': [0.107678, 0.086142], 'p_i': 20, 'u_i': 3.6983},
        {'id': 2, 'e_m': 0.518452, 'e_o_k': [0.403240, 0.322592], 'p_i': 40, 'u_i': 3.0670},
        {'id': 3, 'e_m': 0.130830, 'e_o_k': [0.101757, 0.081405], 'p_i': 80, 'u_i': 2.2547},
        {'id': 4, 'e_m': 6.327178, 'e_o_k': [4.921138, 3.936911], 'p_i': 80, 'u_i': 3.3628},
        {'id': 5, 'e_m': 0.084400, 'e_o_k': [0.065644, 0.052515], 'p_i': 10, 'u_i': 1.9431},
        {'id': 6, 'e_m': 1.306253, 'e_o_k': [1.015975, 0.812780], 'p_i': 80, 'u_i': 4.2381},
        {'id': 7, 'e_m': 1.671201, 'e_o_k': [1.299823, 1.039858], 'p_i': 10, 'u_i': 1.5683},
    ]
    B_BUDGET = 88.319990
    return processors, tasks, B_BUDGET
