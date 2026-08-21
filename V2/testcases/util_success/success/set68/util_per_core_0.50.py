"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600007, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600007, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.163291, 'e_o_k': [0.193882, 0.155105], 'p_i': 10, 'u_i': 3.1458},
        {'id': 1, 'e_m': 4.080348, 'e_o_k': [0.414670, 0.331736, 0.265389, 0.212311], 'p_i': 20, 'u_i': 4.9683},
        {'id': 2, 'e_m': 3.471412, 'e_o_k': [0.578569, 0.462855], 'p_i': 40, 'u_i': 2.4718},
        {'id': 3, 'e_m': 10.330352, 'e_o_k': [0.840030, 0.672024, 0.537619, 0.430095, 0.344076, 0.275261], 'p_i': 80, 'u_i': 4.0774},
        {'id': 4, 'e_m': 3.748591, 'e_o_k': [0.304823, 0.243858, 0.195087, 0.156069, 0.124855, 0.099884], 'p_i': 80, 'u_i': 2.9703},
        {'id': 5, 'e_m': 0.494206, 'e_o_k': [0.044105, 0.035284, 0.028227, 0.022582, 0.018065], 'p_i': 40, 'u_i': 3.9269},
        {'id': 6, 'e_m': 3.182191, 'e_o_k': [0.530365, 0.424292], 'p_i': 10, 'u_i': 3.4836},
        {'id': 7, 'e_m': 3.452287, 'e_o_k': [0.308093, 0.246475, 0.197180, 0.157744, 0.126195], 'p_i': 40, 'u_i': 2.8974},
    ]
    B_BUDGET = 119.600007
    return processors, tasks, B_BUDGET
