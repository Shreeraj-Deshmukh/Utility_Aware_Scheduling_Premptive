"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320014, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.320014, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.075032, 'e_o_k': [0.250841, 0.250841, 0.250841, 0.250841, 0.250841, 0.250841], 'p_i': 10, 'u_i': 3.8590},
        {'id': 1, 'e_m': 0.138443, 'e_o_k': [0.038764, 0.038764, 0.038764, 0.038764, 0.038764], 'p_i': 20, 'u_i': 3.6983},
        {'id': 2, 'e_m': 0.518452, 'e_o_k': [0.145166, 0.145166, 0.145166, 0.145166, 0.145166], 'p_i': 40, 'u_i': 3.0670},
        {'id': 3, 'e_m': 0.130830, 'e_o_k': [0.091581, 0.091581], 'p_i': 80, 'u_i': 2.2547},
        {'id': 4, 'e_m': 6.327178, 'e_o_k': [4.429025, 4.429025], 'p_i': 80, 'u_i': 3.3628},
        {'id': 5, 'e_m': 0.084400, 'e_o_k': [0.059080, 0.059080], 'p_i': 10, 'u_i': 1.9431},
        {'id': 6, 'e_m': 1.306253, 'e_o_k': [0.365751, 0.365751, 0.365751, 0.365751, 0.365751], 'p_i': 80, 'u_i': 4.2381},
        {'id': 7, 'e_m': 1.671201, 'e_o_k': [0.779894, 0.779894, 0.779894], 'p_i': 10, 'u_i': 1.5683},
    ]
    B_BUDGET = 88.320014
    return processors, tasks, B_BUDGET
