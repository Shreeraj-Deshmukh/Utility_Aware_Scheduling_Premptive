"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519999, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519999, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.148983, 'e_o_k': [0.421645, 0.337316, 0.269853, 0.215882], 'p_i': 10, 'u_i': 4.4798},
        {'id': 1, 'e_m': 3.844813, 'e_o_k': [0.640802, 0.512642], 'p_i': 20, 'u_i': 2.0952},
        {'id': 2, 'e_m': 3.889995, 'e_o_k': [0.478278, 0.382622, 0.306098], 'p_i': 40, 'u_i': 3.6547},
        {'id': 3, 'e_m': 10.726244, 'e_o_k': [1.318801, 1.055040, 0.844032], 'p_i': 80, 'u_i': 2.4225},
        {'id': 4, 'e_m': 0.832956, 'e_o_k': [0.067733, 0.054187, 0.043349, 0.034679, 0.027744, 0.022195], 'p_i': 20, 'u_i': 3.0832},
        {'id': 5, 'e_m': 2.973160, 'e_o_k': [0.265334, 0.212267, 0.169814, 0.135851, 0.108681], 'p_i': 20, 'u_i': 3.4868},
        {'id': 6, 'e_m': 1.913787, 'e_o_k': [0.318964, 0.255172], 'p_i': 20, 'u_i': 3.8765},
        {'id': 7, 'e_m': 1.510759, 'e_o_k': [0.134825, 0.107860, 0.086288, 0.069030, 0.055224], 'p_i': 20, 'u_i': 3.4288},
    ]
    B_BUDGET = 143.519999
    return processors, tasks, B_BUDGET
