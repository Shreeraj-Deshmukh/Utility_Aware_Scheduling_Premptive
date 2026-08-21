"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.178484, 'e_o_k': [0.194415, 0.155532, 0.124426, 0.099540, 0.079632], 'p_i': 10, 'u_i': 1.4156},
        {'id': 1, 'e_m': 6.006743, 'e_o_k': [1.001124, 0.800899], 'p_i': 20, 'u_i': 4.7114},
        {'id': 2, 'e_m': 15.882122, 'e_o_k': [1.417372, 1.133897, 0.907118, 0.725694, 0.580555], 'p_i': 40, 'u_i': 3.0006},
        {'id': 3, 'e_m': 22.741294, 'e_o_k': [2.796061, 2.236849, 1.789479], 'p_i': 80, 'u_i': 1.2816},
        {'id': 4, 'e_m': 2.923170, 'e_o_k': [0.297070, 0.237656, 0.190125, 0.152100], 'p_i': 40, 'u_i': 2.2759},
        {'id': 5, 'e_m': 8.699681, 'e_o_k': [0.707429, 0.565943, 0.452755, 0.362204, 0.289763, 0.231810], 'p_i': 20, 'u_i': 1.7983},
        {'id': 6, 'e_m': 0.132606, 'e_o_k': [0.022101, 0.017681], 'p_i': 10, 'u_i': 2.1310},
        {'id': 7, 'e_m': 5.583427, 'e_o_k': [0.454026, 0.363221, 0.290576, 0.232461, 0.185969, 0.148775], 'p_i': 20, 'u_i': 2.4443},
    ]
    B_BUDGET = 239.200001
    return processors, tasks, B_BUDGET
