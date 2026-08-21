"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120013, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120013, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.965524, 'e_o_k': [0.504626, 0.403701, 0.322961, 0.258369], 'p_i': 10, 'u_i': 4.6332},
        {'id': 1, 'e_m': 9.663140, 'e_o_k': [0.982026, 0.785621, 0.628497, 0.502798], 'p_i': 20, 'u_i': 4.7857},
        {'id': 2, 'e_m': 9.582502, 'e_o_k': [0.855173, 0.684139, 0.547311, 0.437849, 0.350279], 'p_i': 40, 'u_i': 1.8112},
        {'id': 3, 'e_m': 7.877945, 'e_o_k': [0.703053, 0.562443, 0.449954, 0.359963, 0.287971], 'p_i': 80, 'u_i': 2.4016},
        {'id': 4, 'e_m': 9.529790, 'e_o_k': [0.774931, 0.619945, 0.495956, 0.396765, 0.317412, 0.253929], 'p_i': 80, 'u_i': 3.4510},
        {'id': 5, 'e_m': 2.334262, 'e_o_k': [0.189814, 0.151852, 0.121481, 0.097185, 0.077748, 0.062198], 'p_i': 40, 'u_i': 2.8583},
        {'id': 6, 'e_m': 3.529750, 'e_o_k': [0.588292, 0.470633], 'p_i': 10, 'u_i': 4.0832},
        {'id': 7, 'e_m': 3.517999, 'e_o_k': [0.313958, 0.251166, 0.200933, 0.160746, 0.128597], 'p_i': 10, 'u_i': 2.2012},
    ]
    B_BUDGET = 263.120013
    return processors, tasks, B_BUDGET
