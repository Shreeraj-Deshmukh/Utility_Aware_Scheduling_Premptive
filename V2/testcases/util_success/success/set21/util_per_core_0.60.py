"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.52001, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.52001, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.037163, 'e_o_k': [0.127520, 0.102016, 0.081613], 'p_i': 10, 'u_i': 2.6945},
        {'id': 1, 'e_m': 5.476766, 'e_o_k': [0.445352, 0.356282, 0.285026, 0.228020, 0.182416, 0.145933], 'p_i': 20, 'u_i': 1.0830},
        {'id': 2, 'e_m': 8.054565, 'e_o_k': [1.342427, 1.073942], 'p_i': 40, 'u_i': 1.9156},
        {'id': 3, 'e_m': 14.480551, 'e_o_k': [1.177510, 0.942008, 0.753607, 0.602885, 0.482308, 0.385847], 'p_i': 80, 'u_i': 2.8864},
        {'id': 4, 'e_m': 1.135219, 'e_o_k': [0.101311, 0.081048, 0.064839, 0.051871, 0.041497], 'p_i': 10, 'u_i': 1.3892},
        {'id': 5, 'e_m': 1.124461, 'e_o_k': [0.114274, 0.091420, 0.073136, 0.058509], 'p_i': 10, 'u_i': 2.4866},
        {'id': 6, 'e_m': 10.122939, 'e_o_k': [0.903404, 0.722723, 0.578178, 0.462543, 0.370034], 'p_i': 80, 'u_i': 4.5153},
        {'id': 7, 'e_m': 3.502788, 'e_o_k': [0.312600, 0.250080, 0.200064, 0.160051, 0.128041], 'p_i': 40, 'u_i': 1.1207},
    ]
    B_BUDGET = 143.520010
    return processors, tasks, B_BUDGET
