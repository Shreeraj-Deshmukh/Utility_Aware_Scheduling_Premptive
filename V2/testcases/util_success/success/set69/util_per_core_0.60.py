"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520011, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520011, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.084542, 'e_o_k': [0.006875, 0.005500, 0.004400, 0.003520, 0.002816, 0.002253], 'p_i': 10, 'u_i': 1.5924},
        {'id': 1, 'e_m': 2.691874, 'e_o_k': [0.273564, 0.218852, 0.175081, 0.140065], 'p_i': 20, 'u_i': 4.1777},
        {'id': 2, 'e_m': 6.566993, 'e_o_k': [1.094499, 0.875599], 'p_i': 40, 'u_i': 1.3396},
        {'id': 3, 'e_m': 10.015162, 'e_o_k': [1.017801, 0.814241, 0.651393, 0.521114], 'p_i': 80, 'u_i': 3.6971},
        {'id': 4, 'e_m': 9.524369, 'e_o_k': [1.171029, 0.936823, 0.749459], 'p_i': 20, 'u_i': 2.7456},
        {'id': 5, 'e_m': 11.760194, 'e_o_k': [1.445926, 1.156740, 0.925392], 'p_i': 80, 'u_i': 1.4781},
        {'id': 6, 'e_m': 11.085155, 'e_o_k': [0.901408, 0.721126, 0.576901, 0.461521, 0.369217, 0.295373], 'p_i': 80, 'u_i': 4.2271},
        {'id': 7, 'e_m': 0.116048, 'e_o_k': [0.011794, 0.009435, 0.007548, 0.006038], 'p_i': 20, 'u_i': 2.1613},
    ]
    B_BUDGET = 143.520011
    return processors, tasks, B_BUDGET
