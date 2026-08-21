"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520001, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520001, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.543626, 'e_o_k': [0.288156, 0.230525, 0.184420, 0.147536, 0.118029, 0.094423], 'p_i': 10, 'u_i': 4.5134},
        {'id': 1, 'e_m': 2.727558, 'e_o_k': [0.335355, 0.268284, 0.214627], 'p_i': 20, 'u_i': 4.5874},
        {'id': 2, 'e_m': 3.027600, 'e_o_k': [0.372246, 0.297797, 0.238237], 'p_i': 40, 'u_i': 2.7347},
        {'id': 3, 'e_m': 16.466407, 'e_o_k': [2.024558, 1.619647, 1.295717], 'p_i': 80, 'u_i': 4.9671},
        {'id': 4, 'e_m': 8.159995, 'e_o_k': [0.728224, 0.582579, 0.466064, 0.372851, 0.298281], 'p_i': 80, 'u_i': 4.8761},
        {'id': 5, 'e_m': 0.426152, 'e_o_k': [0.043308, 0.034647, 0.027717, 0.022174], 'p_i': 10, 'u_i': 2.5248},
        {'id': 6, 'e_m': 2.183606, 'e_o_k': [0.363934, 0.291147], 'p_i': 40, 'u_i': 4.9532},
        {'id': 7, 'e_m': 9.141364, 'e_o_k': [0.929000, 0.743200, 0.594560, 0.475648], 'p_i': 40, 'u_i': 2.2979},
    ]
    B_BUDGET = 143.520001
    return processors, tasks, B_BUDGET
