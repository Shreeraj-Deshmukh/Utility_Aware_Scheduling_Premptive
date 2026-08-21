"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359999, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359999, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.636122, 'e_o_k': [0.106020, 0.084816], 'p_i': 10, 'u_i': 1.8047},
        {'id': 1, 'e_m': 4.875303, 'e_o_k': [0.812550, 0.650040], 'p_i': 20, 'u_i': 1.0945},
        {'id': 2, 'e_m': 3.983168, 'e_o_k': [0.355471, 0.284377, 0.227501, 0.182001, 0.145601], 'p_i': 40, 'u_i': 2.4137},
        {'id': 3, 'e_m': 21.479453, 'e_o_k': [3.579909, 2.863927], 'p_i': 80, 'u_i': 1.6729},
        {'id': 4, 'e_m': 3.673954, 'e_o_k': [0.298754, 0.239003, 0.191202, 0.152962, 0.122370, 0.097896], 'p_i': 40, 'u_i': 2.8481},
        {'id': 5, 'e_m': 3.405852, 'e_o_k': [0.346123, 0.276899, 0.221519, 0.177215], 'p_i': 10, 'u_i': 3.6691},
        {'id': 6, 'e_m': 5.720874, 'e_o_k': [0.581390, 0.465112, 0.372089, 0.297671], 'p_i': 20, 'u_i': 3.0767},
        {'id': 7, 'e_m': 16.485805, 'e_o_k': [1.340571, 1.072457, 0.857965, 0.686372, 0.549098, 0.439278], 'p_i': 80, 'u_i': 1.7471},
    ]
    B_BUDGET = 191.359999
    return processors, tasks, B_BUDGET
