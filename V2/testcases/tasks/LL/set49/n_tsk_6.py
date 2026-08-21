"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199993, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199993, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.001301, 'e_o_k': [0.000176, 0.000141, 0.000113, 0.000090, 0.000072, 0.000058], 'p_i': 10, 'u_i': 2.0413},
        {'id': 1, 'e_m': 0.760011, 'e_o_k': [0.155740, 0.124592, 0.099674], 'p_i': 20, 'u_i': 1.2036},
        {'id': 2, 'e_m': 0.400720, 'e_o_k': [0.111311, 0.089049], 'p_i': 40, 'u_i': 1.4564},
        {'id': 3, 'e_m': 3.071005, 'e_o_k': [0.520157, 0.416125, 0.332900, 0.266320], 'p_i': 80, 'u_i': 1.4719},
        {'id': 4, 'e_m': 23.514057, 'e_o_k': [4.818454, 3.854763, 3.083811], 'p_i': 80, 'u_i': 1.0831},
        {'id': 5, 'e_m': 0.781522, 'e_o_k': [0.116243, 0.092994, 0.074395, 0.059516, 0.047613], 'p_i': 40, 'u_i': 3.5025},
    ]
    B_BUDGET = 55.199993
    return processors, tasks, B_BUDGET
