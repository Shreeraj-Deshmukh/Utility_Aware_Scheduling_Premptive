"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280002, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280002, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.391956, 'e_o_k': [0.034979, 0.027984, 0.022387, 0.017909, 0.014328], 'p_i': 10, 'u_i': 2.2173},
        {'id': 1, 'e_m': 7.525889, 'e_o_k': [0.764826, 0.611861, 0.489489, 0.391591], 'p_i': 20, 'u_i': 3.2312},
        {'id': 2, 'e_m': 10.036347, 'e_o_k': [1.233977, 0.987182, 0.789745], 'p_i': 40, 'u_i': 3.7207},
        {'id': 3, 'e_m': 22.322357, 'e_o_k': [2.744552, 2.195642, 1.756513], 'p_i': 80, 'u_i': 2.0745},
        {'id': 4, 'e_m': 0.030081, 'e_o_k': [0.005013, 0.004011], 'p_i': 10, 'u_i': 4.8505},
        {'id': 5, 'e_m': 1.168973, 'e_o_k': [0.104323, 0.083458, 0.066767, 0.053413, 0.042731], 'p_i': 10, 'u_i': 1.9965},
        {'id': 6, 'e_m': 9.641753, 'e_o_k': [0.860461, 0.688369, 0.550695, 0.440556, 0.352445], 'p_i': 20, 'u_i': 3.3766},
        {'id': 7, 'e_m': 20.206302, 'e_o_k': [1.803275, 1.442620, 1.154096, 0.923277, 0.738622], 'p_i': 80, 'u_i': 1.4786},
    ]
    B_BUDGET = 215.280002
    return processors, tasks, B_BUDGET
