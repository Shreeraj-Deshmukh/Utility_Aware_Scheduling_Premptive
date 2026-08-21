"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680005, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680005, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.667633, 'e_o_k': [0.067849, 0.054279, 0.043423, 0.034739], 'p_i': 10, 'u_i': 1.6879},
        {'id': 1, 'e_m': 1.022805, 'e_o_k': [0.103944, 0.083155, 0.066524, 0.053219], 'p_i': 20, 'u_i': 2.2588},
        {'id': 2, 'e_m': 4.952657, 'e_o_k': [0.825443, 0.660354], 'p_i': 40, 'u_i': 4.0829},
        {'id': 3, 'e_m': 7.527601, 'e_o_k': [0.925525, 0.740420, 0.592336], 'p_i': 80, 'u_i': 1.6866},
        {'id': 4, 'e_m': 0.525923, 'e_o_k': [0.064663, 0.051730, 0.041384], 'p_i': 40, 'u_i': 3.5950},
        {'id': 5, 'e_m': 15.701459, 'e_o_k': [2.616910, 2.093528], 'p_i': 80, 'u_i': 4.2025},
        {'id': 6, 'e_m': 6.203629, 'e_o_k': [1.033938, 0.827150], 'p_i': 40, 'u_i': 3.6883},
        {'id': 7, 'e_m': 7.974239, 'e_o_k': [1.329040, 1.063232], 'p_i': 80, 'u_i': 1.6967},
    ]
    B_BUDGET = 95.680005
    return processors, tasks, B_BUDGET
