"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120006, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120006, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.917779, 'e_o_k': [0.438878, 0.351103, 0.280882, 0.224706, 0.179765], 'p_i': 10, 'u_i': 2.2213},
        {'id': 1, 'e_m': 4.390138, 'e_o_k': [0.446152, 0.356922, 0.285537, 0.228430], 'p_i': 20, 'u_i': 1.5658},
        {'id': 2, 'e_m': 17.460343, 'e_o_k': [1.774425, 1.419540, 1.135632, 0.908506], 'p_i': 40, 'u_i': 3.4291},
        {'id': 3, 'e_m': 26.487736, 'e_o_k': [4.414623, 3.531698], 'p_i': 80, 'u_i': 2.0089},
        {'id': 4, 'e_m': 0.397572, 'e_o_k': [0.032329, 0.025863, 0.020691, 0.016553, 0.013242, 0.010594], 'p_i': 10, 'u_i': 2.8690},
        {'id': 5, 'e_m': 2.239944, 'e_o_k': [0.373324, 0.298659], 'p_i': 10, 'u_i': 4.7846},
        {'id': 6, 'e_m': 1.120709, 'e_o_k': [0.137792, 0.110234, 0.088187], 'p_i': 10, 'u_i': 2.6284},
        {'id': 7, 'e_m': 13.811497, 'e_o_k': [1.698135, 1.358508, 1.086806], 'p_i': 40, 'u_i': 3.5588},
    ]
    B_BUDGET = 263.120006
    return processors, tasks, B_BUDGET
