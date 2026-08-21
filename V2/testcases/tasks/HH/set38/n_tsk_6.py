"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.827540, 'e_o_k': [2.199198, 1.759358], 'p_i': 10, 'u_i': 1.1650},
        {'id': 1, 'e_m': 2.999858, 'e_o_k': [1.422697, 1.138158, 0.910526, 0.728421], 'p_i': 20, 'u_i': 2.0635},
        {'id': 2, 'e_m': 7.357385, 'e_o_k': [5.722411, 4.577928], 'p_i': 40, 'u_i': 4.3065},
        {'id': 3, 'e_m': 4.404242, 'e_o_k': [1.671312, 1.337050, 1.069640, 0.855712, 0.684569, 0.547656], 'p_i': 80, 'u_i': 1.2855},
        {'id': 4, 'e_m': 5.560674, 'e_o_k': [2.110152, 1.688122, 1.350498, 1.080398, 0.864318, 0.691455], 'p_i': 80, 'u_i': 4.6522},
        {'id': 5, 'e_m': 1.175140, 'e_o_k': [0.489409, 0.391527, 0.313222, 0.250577, 0.200462], 'p_i': 20, 'u_i': 4.9928},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
