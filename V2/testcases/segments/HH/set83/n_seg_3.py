"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640005, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640005, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.573701, 'e_o_k': [0.902943, 0.722355, 0.577884], 'p_i': 10, 'u_i': 3.6650},
        {'id': 1, 'e_m': 1.488704, 'e_o_k': [0.854174, 0.683339, 0.546671], 'p_i': 20, 'u_i': 4.7122},
        {'id': 2, 'e_m': 1.136090, 'e_o_k': [0.651855, 0.521484, 0.417187], 'p_i': 40, 'u_i': 2.7870},
        {'id': 3, 'e_m': 13.753139, 'e_o_k': [7.891146, 6.312916, 5.050333], 'p_i': 80, 'u_i': 1.7506},
        {'id': 4, 'e_m': 5.982379, 'e_o_k': [3.432512, 2.746010, 2.196808], 'p_i': 40, 'u_i': 4.5685},
        {'id': 5, 'e_m': 0.674012, 'e_o_k': [0.386728, 0.309382, 0.247506], 'p_i': 10, 'u_i': 2.7344},
        {'id': 6, 'e_m': 0.887834, 'e_o_k': [0.509413, 0.407530, 0.326024], 'p_i': 40, 'u_i': 1.1398},
        {'id': 7, 'e_m': 10.297741, 'e_o_k': [5.908540, 4.726832, 3.781465], 'p_i': 80, 'u_i': 4.8954},
    ]
    B_BUDGET = 176.640005
    return processors, tasks, B_BUDGET
