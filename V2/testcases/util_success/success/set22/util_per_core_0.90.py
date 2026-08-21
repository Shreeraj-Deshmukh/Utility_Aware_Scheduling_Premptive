"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.28001, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.28001, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.515388, 'e_o_k': [0.458881, 0.367105, 0.293684, 0.234947], 'p_i': 10, 'u_i': 2.9329},
        {'id': 1, 'e_m': 0.323685, 'e_o_k': [0.032895, 0.026316, 0.021053, 0.016842], 'p_i': 20, 'u_i': 4.3550},
        {'id': 2, 'e_m': 9.821888, 'e_o_k': [0.876537, 0.701230, 0.560984, 0.448787, 0.359030], 'p_i': 40, 'u_i': 2.2741},
        {'id': 3, 'e_m': 4.322582, 'e_o_k': [0.531465, 0.425172, 0.340138], 'p_i': 80, 'u_i': 2.5808},
        {'id': 4, 'e_m': 7.581095, 'e_o_k': [0.676561, 0.541249, 0.432999, 0.346399, 0.277120], 'p_i': 40, 'u_i': 4.5356},
        {'id': 5, 'e_m': 3.155445, 'e_o_k': [0.387965, 0.310372, 0.248297], 'p_i': 20, 'u_i': 4.4130},
        {'id': 6, 'e_m': 15.338534, 'e_o_k': [1.885885, 1.508708, 1.206967], 'p_i': 80, 'u_i': 1.1305},
        {'id': 7, 'e_m': 4.936661, 'e_o_k': [0.501693, 0.401355, 0.321084, 0.256867], 'p_i': 10, 'u_i': 4.7707},
    ]
    B_BUDGET = 215.280010
    return processors, tasks, B_BUDGET
