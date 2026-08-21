"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320014, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320014, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.553947, 'e_o_k': [0.317838, 0.254271, 0.203417], 'p_i': 10, 'u_i': 1.6802},
        {'id': 1, 'e_m': 1.797565, 'e_o_k': [1.398106, 1.118485], 'p_i': 20, 'u_i': 4.8914},
        {'id': 2, 'e_m': 2.095061, 'e_o_k': [0.795029, 0.636023, 0.508819, 0.407055, 0.325644, 0.260515], 'p_i': 40, 'u_i': 2.7135},
        {'id': 3, 'e_m': 12.004113, 'e_o_k': [4.555295, 3.644236, 2.915389, 2.332311, 1.865849, 1.492679], 'p_i': 80, 'u_i': 1.9259},
        {'id': 4, 'e_m': 1.675111, 'e_o_k': [0.794430, 0.635544, 0.508435, 0.406748], 'p_i': 40, 'u_i': 2.2208},
        {'id': 5, 'e_m': 0.416855, 'e_o_k': [0.173607, 0.138886, 0.111108, 0.088887, 0.071109], 'p_i': 40, 'u_i': 3.1305},
    ]
    B_BUDGET = 88.320014
    return processors, tasks, B_BUDGET
