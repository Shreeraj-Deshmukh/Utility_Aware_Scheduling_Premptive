"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600009, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600009, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.508549, 'e_o_k': [0.254934, 0.203947, 0.163158, 0.130526], 'p_i': 10, 'u_i': 2.9329},
        {'id': 1, 'e_m': 0.179825, 'e_o_k': [0.018275, 0.014620, 0.011696, 0.009357], 'p_i': 20, 'u_i': 4.3550},
        {'id': 2, 'e_m': 5.456604, 'e_o_k': [0.486965, 0.389572, 0.311658, 0.249326, 0.199461], 'p_i': 40, 'u_i': 2.2741},
        {'id': 3, 'e_m': 2.401434, 'e_o_k': [0.295258, 0.236207, 0.188965], 'p_i': 80, 'u_i': 2.5808},
        {'id': 4, 'e_m': 4.211720, 'e_o_k': [0.375867, 0.300694, 0.240555, 0.192444, 0.153955], 'p_i': 40, 'u_i': 4.5356},
        {'id': 5, 'e_m': 1.753025, 'e_o_k': [0.215536, 0.172429, 0.137943], 'p_i': 20, 'u_i': 4.4130},
        {'id': 6, 'e_m': 8.521408, 'e_o_k': [1.047714, 0.838171, 0.670537], 'p_i': 80, 'u_i': 1.1305},
        {'id': 7, 'e_m': 2.742590, 'e_o_k': [0.278718, 0.222975, 0.178380, 0.142704], 'p_i': 10, 'u_i': 4.7707},
    ]
    B_BUDGET = 119.600009
    return processors, tasks, B_BUDGET
