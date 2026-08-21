"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.971116, 'e_o_k': [1.237376, 0.989901, 0.791921, 0.633537, 0.506829], 'p_i': 10, 'u_i': 1.3731},
        {'id': 1, 'e_m': 7.668867, 'e_o_k': [4.400170, 3.520136, 2.816109], 'p_i': 20, 'u_i': 1.2580},
        {'id': 2, 'e_m': 2.097251, 'e_o_k': [0.994631, 0.795705, 0.636564, 0.509251], 'p_i': 40, 'u_i': 4.0597},
        {'id': 3, 'e_m': 5.361097, 'e_o_k': [2.232727, 1.786182, 1.428945, 1.143156, 0.914525], 'p_i': 80, 'u_i': 2.2779},
    ]
    B_BUDGET = 176.640005
    return processors, tasks, B_BUDGET
