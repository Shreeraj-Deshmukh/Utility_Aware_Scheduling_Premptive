"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679989, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679989, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.067561, 'e_o_k': [0.095273, 0.076218, 0.060974, 0.048780, 0.039024], 'p_i': 10, 'u_i': 4.6830},
        {'id': 1, 'e_m': 6.103602, 'e_o_k': [1.017267, 0.813814], 'p_i': 20, 'u_i': 2.4027},
        {'id': 2, 'e_m': 4.537756, 'e_o_k': [0.756293, 0.605034], 'p_i': 40, 'u_i': 2.7203},
        {'id': 3, 'e_m': 4.054946, 'e_o_k': [0.329735, 0.263788, 0.211030, 0.168824, 0.135059, 0.108047], 'p_i': 80, 'u_i': 2.4000},
        {'id': 4, 'e_m': 0.349178, 'e_o_k': [0.058196, 0.046557], 'p_i': 20, 'u_i': 2.9059},
        {'id': 5, 'e_m': 0.690991, 'e_o_k': [0.084958, 0.067966, 0.054373], 'p_i': 10, 'u_i': 3.1411},
        {'id': 6, 'e_m': 5.436589, 'e_o_k': [0.552499, 0.441999, 0.353599, 0.282879], 'p_i': 80, 'u_i': 3.1206},
        {'id': 7, 'e_m': 2.776704, 'e_o_k': [0.341398, 0.273118, 0.218495], 'p_i': 40, 'u_i': 4.7030},
    ]
    B_BUDGET = 95.679989
    return processors, tasks, B_BUDGET
