"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.154912, 'e_o_k': [0.064516, 0.051613, 0.041290, 0.033032, 0.026426], 'p_i': 10, 'u_i': 3.6728},
        {'id': 1, 'e_m': 2.110085, 'e_o_k': [0.800731, 0.640584, 0.512468, 0.409974, 0.327979, 0.262383], 'p_i': 20, 'u_i': 2.1630},
        {'id': 2, 'e_m': 6.047745, 'e_o_k': [2.294985, 1.835988, 1.468791, 1.175032, 0.940026, 0.752021], 'p_i': 40, 'u_i': 4.2465},
        {'id': 3, 'e_m': 10.224870, 'e_o_k': [3.880112, 3.104089, 2.483271, 1.986617, 1.589294, 1.271435], 'p_i': 80, 'u_i': 1.5896},
    ]
    B_BUDGET = 88.319991
    return processors, tasks, B_BUDGET
