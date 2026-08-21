"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320013, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.320013, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.003420, 'e_o_k': [0.645582, 0.387349, 0.232410, 0.139446], 'p_i': 10, 'u_i': 2.9329},
        {'id': 1, 'e_m': 0.071930, 'e_o_k': [0.046279, 0.027767, 0.016660, 0.009996], 'p_i': 20, 'u_i': 4.3550},
        {'id': 2, 'e_m': 2.182642, 'e_o_k': [1.325338, 0.795203, 0.477122, 0.286273, 0.171764], 'p_i': 40, 'u_i': 2.2741},
        {'id': 3, 'e_m': 0.960574, 'e_o_k': [0.686124, 0.411674, 0.247005], 'p_i': 80, 'u_i': 2.5808},
        {'id': 4, 'e_m': 1.684688, 'e_o_k': [1.022971, 0.613783, 0.368270, 0.220962, 0.132577], 'p_i': 40, 'u_i': 4.5356},
        {'id': 5, 'e_m': 0.701210, 'e_o_k': [0.500864, 0.300519, 0.180311], 'p_i': 20, 'u_i': 4.4130},
        {'id': 6, 'e_m': 3.408563, 'e_o_k': [2.434688, 1.460813, 0.876488], 'p_i': 80, 'u_i': 1.1305},
        {'id': 7, 'e_m': 1.097036, 'e_o_k': [0.705814, 0.423488, 0.254093, 0.152456], 'p_i': 10, 'u_i': 4.7707},
    ]
    B_BUDGET = 88.320013
    return processors, tasks, B_BUDGET
