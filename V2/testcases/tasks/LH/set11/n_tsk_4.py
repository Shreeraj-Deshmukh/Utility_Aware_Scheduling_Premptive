"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.136367, 'e_o_k': [0.473261, 0.378609, 0.302887, 0.242309, 0.193848], 'p_i': 10, 'u_i': 2.5944},
        {'id': 1, 'e_m': 4.722654, 'e_o_k': [1.966836, 1.573469, 1.258775, 1.007020, 0.805616], 'p_i': 20, 'u_i': 4.8069},
        {'id': 2, 'e_m': 1.652632, 'e_o_k': [0.783768, 0.627015, 0.501612, 0.401289], 'p_i': 40, 'u_i': 1.7136},
        {'id': 3, 'e_m': 0.713186, 'e_o_k': [0.297019, 0.237616, 0.190092, 0.152074, 0.121659], 'p_i': 80, 'u_i': 3.6562},
    ]
    B_BUDGET = 88.320007
    return processors, tasks, B_BUDGET
