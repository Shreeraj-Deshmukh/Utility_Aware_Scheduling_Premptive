"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520001, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520001, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.601342, 'e_o_k': [0.142909, 0.114327, 0.091462, 0.073169, 0.058535], 'p_i': 10, 'u_i': 4.6830},
        {'id': 1, 'e_m': 9.155403, 'e_o_k': [1.525901, 1.220720], 'p_i': 20, 'u_i': 2.4027},
        {'id': 2, 'e_m': 6.806633, 'e_o_k': [1.134439, 0.907551], 'p_i': 40, 'u_i': 2.7203},
        {'id': 3, 'e_m': 6.082419, 'e_o_k': [0.494602, 0.395682, 0.316545, 0.253236, 0.202589, 0.162071], 'p_i': 80, 'u_i': 2.4000},
        {'id': 4, 'e_m': 0.523768, 'e_o_k': [0.087295, 0.069836], 'p_i': 20, 'u_i': 2.9059},
        {'id': 5, 'e_m': 1.036487, 'e_o_k': [0.127437, 0.101950, 0.081560], 'p_i': 10, 'u_i': 3.1411},
        {'id': 6, 'e_m': 8.154884, 'e_o_k': [0.828748, 0.662999, 0.530399, 0.424319], 'p_i': 80, 'u_i': 3.1206},
        {'id': 7, 'e_m': 4.165056, 'e_o_k': [0.512097, 0.409678, 0.327742], 'p_i': 40, 'u_i': 4.7030},
    ]
    B_BUDGET = 143.520001
    return processors, tasks, B_BUDGET
