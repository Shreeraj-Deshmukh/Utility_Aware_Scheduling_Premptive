"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520002, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520002, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.836232, 'e_o_k': [0.139372, 0.111498], 'p_i': 10, 'u_i': 2.2547},
        {'id': 1, 'e_m': 2.372827, 'e_o_k': [0.395471, 0.316377], 'p_i': 20, 'u_i': 3.3628},
        {'id': 2, 'e_m': 0.660582, 'e_o_k': [0.110097, 0.088078], 'p_i': 40, 'u_i': 1.9431},
        {'id': 3, 'e_m': 38.515617, 'e_o_k': [3.437258, 2.749806, 2.199845, 1.759876, 1.407901], 'p_i': 80, 'u_i': 4.2381},
        {'id': 4, 'e_m': 5.211437, 'e_o_k': [0.640750, 0.512600, 0.410080], 'p_i': 80, 'u_i': 1.5683},
        {'id': 5, 'e_m': 23.594971, 'e_o_k': [3.932495, 3.145996], 'p_i': 80, 'u_i': 1.7999},
        {'id': 6, 'e_m': 3.187800, 'e_o_k': [0.391943, 0.313554, 0.250843], 'p_i': 80, 'u_i': 3.1757},
        {'id': 7, 'e_m': 0.998481, 'e_o_k': [0.122764, 0.098211, 0.078569], 'p_i': 10, 'u_i': 2.2510},
    ]
    B_BUDGET = 143.520002
    return processors, tasks, B_BUDGET
