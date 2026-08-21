"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 38.639997, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.1, "seed": 1004, "set": 4, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.10"}
"""

_SPEC = '{"B": 38.639997, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.1, "seed": 1004, "set": 4, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.464878, 'e_o_k': [0.063004, 0.050403, 0.040322, 0.032258, 0.025806, 0.020645], 'p_i': 10, 'u_i': 2.4783},
        {'id': 1, 'e_m': 0.028439, 'e_o_k': [0.003854, 0.003083, 0.002467, 0.001973, 0.001579, 0.001263], 'p_i': 20, 'u_i': 1.9438},
        {'id': 2, 'e_m': 1.311997, 'e_o_k': [0.364444, 0.291555], 'p_i': 40, 'u_i': 1.5728},
        {'id': 3, 'e_m': 2.237336, 'e_o_k': [0.621482, 0.497186], 'p_i': 80, 'u_i': 1.5110},
        {'id': 4, 'e_m': 1.174834, 'e_o_k': [0.326343, 0.261074], 'p_i': 20, 'u_i': 4.3454},
        {'id': 5, 'e_m': 5.271494, 'e_o_k': [0.892868, 0.714295, 0.571436, 0.457149], 'p_i': 40, 'u_i': 2.7253},
        {'id': 6, 'e_m': 0.171228, 'e_o_k': [0.047563, 0.038051], 'p_i': 10, 'u_i': 1.4714},
        {'id': 7, 'e_m': 1.673435, 'e_o_k': [0.464843, 0.371875], 'p_i': 20, 'u_i': 2.9160},
    ]
    B_BUDGET = 38.639997
    return processors, tasks, B_BUDGET
