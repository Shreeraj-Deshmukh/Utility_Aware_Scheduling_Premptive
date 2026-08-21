"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 21, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 21, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.667633, 'e_o_k': [0.316628, 0.253302, 0.202642, 0.162114], 'p_i': 10, 'u_i': 2.6720},
        {'id': 1, 'e_m': 1.022805, 'e_o_k': [0.485070, 0.388056, 0.310445, 0.248356], 'p_i': 20, 'u_i': 2.8147},
        {'id': 2, 'e_m': 4.952657, 'e_o_k': [3.852067, 3.081653], 'p_i': 40, 'u_i': 3.2707},
        {'id': 3, 'e_m': 7.527601, 'e_o_k': [4.319115, 3.455292, 2.764234], 'p_i': 80, 'u_i': 2.6716},
        {'id': 4, 'e_m': 0.525923, 'e_o_k': [0.301759, 0.241407, 0.193126], 'p_i': 40, 'u_i': 3.1488},
        {'id': 5, 'e_m': 15.701459, 'e_o_k': [12.212246, 9.769797], 'p_i': 80, 'u_i': 3.3006},
        {'id': 6, 'e_m': 6.203629, 'e_o_k': [4.825045, 3.860036], 'p_i': 40, 'u_i': 3.1721},
        {'id': 7, 'e_m': 7.974239, 'e_o_k': [6.202186, 4.961749], 'p_i': 80, 'u_i': 2.6742},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
