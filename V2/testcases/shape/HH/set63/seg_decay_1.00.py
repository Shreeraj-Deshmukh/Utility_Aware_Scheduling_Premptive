"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640005, "H": 80, "J": 24, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 176.640005, "H": 80, "J": 24, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.647287, 'e_o_k': [0.384367, 0.384367, 0.384367, 0.384367, 0.384367, 0.384367], 'p_i': 10, 'u_i': 3.9772},
        {'id': 1, 'e_m': 0.034300, 'e_o_k': [0.012005, 0.012005, 0.012005, 0.012005], 'p_i': 20, 'u_i': 1.4627},
        {'id': 2, 'e_m': 2.925892, 'e_o_k': [2.048124, 2.048124], 'p_i': 40, 'u_i': 4.5040},
        {'id': 3, 'e_m': 1.655242, 'e_o_k': [0.772446, 0.772446, 0.772446], 'p_i': 80, 'u_i': 4.7123},
        {'id': 4, 'e_m': 0.978124, 'e_o_k': [0.273875, 0.273875, 0.273875, 0.273875, 0.273875], 'p_i': 20, 'u_i': 4.3702},
        {'id': 5, 'e_m': 1.868312, 'e_o_k': [0.653909, 0.653909, 0.653909, 0.653909], 'p_i': 40, 'u_i': 3.7678},
        {'id': 6, 'e_m': 15.433016, 'e_o_k': [5.401556, 5.401556, 5.401556, 5.401556], 'p_i': 80, 'u_i': 3.2312},
        {'id': 7, 'e_m': 10.047671, 'e_o_k': [4.688913, 4.688913, 4.688913], 'p_i': 40, 'u_i': 3.7207},
    ]
    B_BUDGET = 176.640005
    return processors, tasks, B_BUDGET
