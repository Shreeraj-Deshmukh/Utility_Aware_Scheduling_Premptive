"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 21, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "freq", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 21, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "freq", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.667633, 'e_o_k': [0.316628, 0.253302, 0.202642, 0.162114], 'p_i': 10, 'u_i': 1.6879},
        {'id': 1, 'e_m': 1.022805, 'e_o_k': [0.485070, 0.388056, 0.310445, 0.248356], 'p_i': 20, 'u_i': 2.2588},
        {'id': 2, 'e_m': 4.952657, 'e_o_k': [3.852067, 3.081653], 'p_i': 40, 'u_i': 4.0829},
        {'id': 3, 'e_m': 7.527601, 'e_o_k': [4.319115, 3.455292, 2.764234], 'p_i': 80, 'u_i': 1.6866},
        {'id': 4, 'e_m': 0.525923, 'e_o_k': [0.301759, 0.241407, 0.193126], 'p_i': 40, 'u_i': 3.5950},
        {'id': 5, 'e_m': 15.701459, 'e_o_k': [12.212246, 9.769797], 'p_i': 80, 'u_i': 4.2025},
        {'id': 6, 'e_m': 6.203629, 'e_o_k': [4.825045, 3.860036], 'p_i': 40, 'u_i': 3.6883},
        {'id': 7, 'e_m': 7.974239, 'e_o_k': [6.202186, 4.961749], 'p_i': 80, 'u_i': 1.6967},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
