"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.489600, 'e_o_k': [0.201882, 0.161506, 0.129205, 0.103364, 0.082691, 0.066153], 'p_i': 10, 'u_i': 3.7891},
        {'id': 1, 'e_m': 7.499350, 'e_o_k': [1.536752, 1.229402, 0.983521], 'p_i': 20, 'u_i': 1.3517},
        {'id': 2, 'e_m': 1.563803, 'e_o_k': [0.264872, 0.211897, 0.169518, 0.135614], 'p_i': 40, 'u_i': 4.0093},
        {'id': 3, 'e_m': 1.577415, 'e_o_k': [0.323241, 0.258593, 0.206874], 'p_i': 80, 'u_i': 1.1110},
        {'id': 4, 'e_m': 12.968885, 'e_o_k': [1.757644, 1.406116, 1.124892, 0.899914, 0.719931, 0.575945], 'p_i': 80, 'u_i': 1.1701},
        {'id': 5, 'e_m': 1.102973, 'e_o_k': [0.226019, 0.180815, 0.144652], 'p_i': 20, 'u_i': 4.4848},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET
