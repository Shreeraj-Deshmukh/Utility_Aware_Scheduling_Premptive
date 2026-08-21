"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199991, "H": 80, "J": 25, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.199991, "H": 80, "J": 25, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.573508, 'e_o_k': [0.179221, 0.107533], 'p_i': 10, 'u_i': 2.5980},
        {'id': 1, 'e_m': 1.886878, 'e_o_k': [0.589649, 0.353790], 'p_i': 20, 'u_i': 2.9083},
        {'id': 2, 'e_m': 2.675239, 'e_o_k': [0.682459, 0.409475, 0.245685], 'p_i': 40, 'u_i': 4.8275},
        {'id': 3, 'e_m': 8.484623, 'e_o_k': [1.840003, 1.104002, 0.662401, 0.397441, 0.238464], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 0.549748, 'e_o_k': [0.140242, 0.084145, 0.050487], 'p_i': 20, 'u_i': 1.8333},
        {'id': 5, 'e_m': 0.074482, 'e_o_k': [0.016152, 0.009691, 0.005815, 0.003489, 0.002093], 'p_i': 20, 'u_i': 4.5368},
        {'id': 6, 'e_m': 1.648956, 'e_o_k': [0.345931, 0.207559, 0.124535, 0.074721, 0.044833, 0.026900], 'p_i': 80, 'u_i': 4.6383},
        {'id': 7, 'e_m': 1.883445, 'e_o_k': [0.408450, 0.245070, 0.147042, 0.088225, 0.052935], 'p_i': 80, 'u_i': 3.5515},
    ]
    B_BUDGET = 55.199991
    return processors, tasks, B_BUDGET
