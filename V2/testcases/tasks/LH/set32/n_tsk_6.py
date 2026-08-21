"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319993, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319993, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.692176, 'e_o_k': [0.328268, 0.262614, 0.210091, 0.168073], 'p_i': 10, 'u_i': 1.0669},
        {'id': 1, 'e_m': 0.927432, 'e_o_k': [0.439839, 0.351871, 0.281497, 0.225198], 'p_i': 20, 'u_i': 2.5210},
        {'id': 2, 'e_m': 0.897482, 'e_o_k': [0.514949, 0.411959, 0.329567], 'p_i': 40, 'u_i': 3.1907},
        {'id': 3, 'e_m': 8.776195, 'e_o_k': [4.162152, 3.329722, 2.663777, 2.131022], 'p_i': 80, 'u_i': 4.8710},
        {'id': 4, 'e_m': 1.647999, 'e_o_k': [1.281777, 1.025422], 'p_i': 20, 'u_i': 3.8865},
        {'id': 5, 'e_m': 0.698713, 'e_o_k': [0.543444, 0.434755], 'p_i': 10, 'u_i': 3.2848},
    ]
    B_BUDGET = 88.319993
    return processors, tasks, B_BUDGET
