"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120008, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120008, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.773032, 'e_o_k': [0.628839, 0.503071], 'p_i': 10, 'u_i': 2.6470},
        {'id': 1, 'e_m': 9.592913, 'e_o_k': [1.179457, 0.943565, 0.754852], 'p_i': 20, 'u_i': 4.9479},
        {'id': 2, 'e_m': 0.263902, 'e_o_k': [0.032447, 0.025958, 0.020766], 'p_i': 40, 'u_i': 2.1346},
        {'id': 3, 'e_m': 10.613704, 'e_o_k': [1.768951, 1.415161], 'p_i': 80, 'u_i': 1.3827},
        {'id': 4, 'e_m': 32.003746, 'e_o_k': [5.333958, 4.267166], 'p_i': 80, 'u_i': 3.9576},
        {'id': 5, 'e_m': 6.009447, 'e_o_k': [0.536302, 0.429042, 0.343234, 0.274587, 0.219669], 'p_i': 20, 'u_i': 4.9670},
        {'id': 6, 'e_m': 4.631419, 'e_o_k': [0.413323, 0.330658, 0.264527, 0.211621, 0.169297], 'p_i': 10, 'u_i': 4.5958},
        {'id': 7, 'e_m': 3.209698, 'e_o_k': [0.286444, 0.229155, 0.183324, 0.146659, 0.117327], 'p_i': 80, 'u_i': 1.9552},
    ]
    B_BUDGET = 263.120008
    return processors, tasks, B_BUDGET
