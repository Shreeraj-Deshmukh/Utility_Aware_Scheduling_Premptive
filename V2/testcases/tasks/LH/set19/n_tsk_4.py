"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.700833, 'e_o_k': [1.124811, 0.899849, 0.719879, 0.575903, 0.460723], 'p_i': 10, 'u_i': 3.4397},
        {'id': 1, 'e_m': 1.395832, 'e_o_k': [0.529687, 0.423750, 0.339000, 0.271200, 0.216960, 0.173568], 'p_i': 20, 'u_i': 4.9693},
        {'id': 2, 'e_m': 0.535278, 'e_o_k': [0.307127, 0.245702, 0.196561], 'p_i': 40, 'u_i': 4.4094},
        {'id': 3, 'e_m': 3.739453, 'e_o_k': [1.773453, 1.418763, 1.135010, 0.908008], 'p_i': 80, 'u_i': 4.1932},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET
