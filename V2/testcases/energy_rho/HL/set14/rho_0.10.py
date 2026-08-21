"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 77.28, "H": 80, "J": 20, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.1, "seed": 1014, "set": 14, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.10"}
"""

_SPEC = '{"B": 77.28, "H": 80, "J": 20, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.1, "seed": 1014, "set": 14, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.722458, 'e_o_k': [0.200683, 0.160546], 'p_i': 10, 'u_i': 1.0216},
        {'id': 1, 'e_m': 3.086888, 'e_o_k': [0.632559, 0.506047, 0.404838], 'p_i': 20, 'u_i': 4.0085},
        {'id': 2, 'e_m': 11.212672, 'e_o_k': [2.297679, 1.838143, 1.470514], 'p_i': 40, 'u_i': 1.9931},
        {'id': 3, 'e_m': 4.466066, 'e_o_k': [0.915177, 0.732142, 0.585714], 'p_i': 80, 'u_i': 2.4773},
        {'id': 4, 'e_m': 0.168840, 'e_o_k': [0.028597, 0.022878, 0.018302, 0.014642], 'p_i': 80, 'u_i': 3.1022},
        {'id': 5, 'e_m': 1.988081, 'e_o_k': [0.269440, 0.215552, 0.172442, 0.137953, 0.110363, 0.088290], 'p_i': 40, 'u_i': 1.9821},
        {'id': 6, 'e_m': 7.911221, 'e_o_k': [1.621152, 1.296922, 1.037537], 'p_i': 80, 'u_i': 1.2190},
        {'id': 7, 'e_m': 6.925151, 'e_o_k': [1.172959, 0.938367, 0.750694, 0.600555], 'p_i': 80, 'u_i': 2.8489},
    ]
    B_BUDGET = 77.280000
    return processors, tasks, B_BUDGET
