"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680009, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680009, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.006839, 'e_o_k': [0.203947, 0.163158, 0.130526, 0.104421], 'p_i': 10, 'u_i': 2.9329},
        {'id': 1, 'e_m': 0.143860, 'e_o_k': [0.014620, 0.011696, 0.009357, 0.007485], 'p_i': 20, 'u_i': 4.3550},
        {'id': 2, 'e_m': 4.365284, 'e_o_k': [0.389572, 0.311658, 0.249326, 0.199461, 0.159569], 'p_i': 40, 'u_i': 2.2741},
        {'id': 3, 'e_m': 1.921148, 'e_o_k': [0.236207, 0.188965, 0.151172], 'p_i': 80, 'u_i': 2.5808},
        {'id': 4, 'e_m': 3.369376, 'e_o_k': [0.300694, 0.240555, 0.192444, 0.153955, 0.123164], 'p_i': 40, 'u_i': 4.5356},
        {'id': 5, 'e_m': 1.402420, 'e_o_k': [0.172429, 0.137943, 0.110354], 'p_i': 20, 'u_i': 4.4130},
        {'id': 6, 'e_m': 6.817126, 'e_o_k': [0.838171, 0.670537, 0.536430], 'p_i': 80, 'u_i': 1.1305},
        {'id': 7, 'e_m': 2.194072, 'e_o_k': [0.222975, 0.178380, 0.142704, 0.114163], 'p_i': 10, 'u_i': 4.7707},
    ]
    B_BUDGET = 95.680009
    return processors, tasks, B_BUDGET
