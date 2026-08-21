"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519999, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519999, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.455943, 'e_o_k': [0.129933, 0.103946, 0.083157, 0.066526, 0.053221], 'p_i': 10, 'u_i': 1.8657},
        {'id': 1, 'e_m': 4.384516, 'e_o_k': [0.391288, 0.313031, 0.250425, 0.200340, 0.160272], 'p_i': 20, 'u_i': 1.6547},
        {'id': 2, 'e_m': 1.664855, 'e_o_k': [0.169193, 0.135354, 0.108283, 0.086627], 'p_i': 40, 'u_i': 3.2690},
        {'id': 3, 'e_m': 5.472919, 'e_o_k': [0.672900, 0.538320, 0.430656], 'p_i': 80, 'u_i': 2.0883},
        {'id': 4, 'e_m': 1.552673, 'e_o_k': [0.190902, 0.152722, 0.122178], 'p_i': 10, 'u_i': 2.4453},
        {'id': 5, 'e_m': 15.187828, 'e_o_k': [1.355411, 1.084329, 0.867463, 0.693970, 0.555176], 'p_i': 40, 'u_i': 4.4841},
        {'id': 6, 'e_m': 7.337823, 'e_o_k': [0.902191, 0.721753, 0.577402], 'p_i': 40, 'u_i': 2.2759},
        {'id': 7, 'e_m': 0.539071, 'e_o_k': [0.089845, 0.071876], 'p_i': 80, 'u_i': 4.2544},
    ]
    B_BUDGET = 143.519999
    return processors, tasks, B_BUDGET
