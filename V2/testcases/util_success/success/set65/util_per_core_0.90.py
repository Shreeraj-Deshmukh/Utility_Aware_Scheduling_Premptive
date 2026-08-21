"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280015, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280015, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.541633, 'e_o_k': [0.055044, 0.044035, 0.035228, 0.028183], 'p_i': 10, 'u_i': 1.3616},
        {'id': 1, 'e_m': 2.927593, 'e_o_k': [0.297520, 0.238016, 0.190413, 0.152330], 'p_i': 20, 'u_i': 4.6708},
        {'id': 2, 'e_m': 0.411902, 'e_o_k': [0.068650, 0.054920], 'p_i': 40, 'u_i': 4.1589},
        {'id': 3, 'e_m': 22.908918, 'e_o_k': [1.862877, 1.490302, 1.192241, 0.953793, 0.763034, 0.610428], 'p_i': 80, 'u_i': 3.1031},
        {'id': 4, 'e_m': 3.640798, 'e_o_k': [0.370000, 0.296000, 0.236800, 0.189440], 'p_i': 10, 'u_i': 2.2660},
        {'id': 5, 'e_m': 0.808678, 'e_o_k': [0.099428, 0.079542, 0.063634], 'p_i': 10, 'u_i': 4.9712},
        {'id': 6, 'e_m': 4.508378, 'e_o_k': [0.458169, 0.366535, 0.293228, 0.234582], 'p_i': 10, 'u_i': 1.2379},
        {'id': 7, 'e_m': 16.280503, 'e_o_k': [1.323876, 1.059101, 0.847281, 0.677825, 0.542260, 0.433808], 'p_i': 40, 'u_i': 2.3403},
    ]
    B_BUDGET = 215.280015
    return processors, tasks, B_BUDGET
