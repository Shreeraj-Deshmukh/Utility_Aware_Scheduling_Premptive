"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.283857, 'e_o_k': [0.951154, 0.760923, 0.608739, 0.486991, 0.389593], 'p_i': 10, 'u_i': 1.7421},
        {'id': 1, 'e_m': 1.330238, 'e_o_k': [0.504796, 0.403837, 0.323069, 0.258456, 0.206764, 0.165412], 'p_i': 20, 'u_i': 1.9951},
        {'id': 2, 'e_m': 2.256874, 'e_o_k': [1.755347, 1.404277], 'p_i': 40, 'u_i': 1.2617},
        {'id': 3, 'e_m': 3.894442, 'e_o_k': [1.477854, 1.182284, 0.945827, 0.756661, 0.605329, 0.484263], 'p_i': 80, 'u_i': 4.5683},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
