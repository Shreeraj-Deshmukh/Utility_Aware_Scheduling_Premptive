"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519997, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519997, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.973944, 'e_o_k': [0.079198, 0.063358, 0.050687, 0.040549, 0.032439, 0.025952], 'p_i': 10, 'u_i': 4.0993},
        {'id': 1, 'e_m': 0.958966, 'e_o_k': [0.159828, 0.127862], 'p_i': 20, 'u_i': 2.5958},
        {'id': 2, 'e_m': 11.482275, 'e_o_k': [1.411755, 1.129404, 0.903523], 'p_i': 40, 'u_i': 1.3643},
        {'id': 3, 'e_m': 10.319339, 'e_o_k': [0.839134, 0.671308, 0.537046, 0.429637, 0.343709, 0.274968], 'p_i': 80, 'u_i': 1.6218},
        {'id': 4, 'e_m': 4.646352, 'e_o_k': [0.472190, 0.377752, 0.302202, 0.241761], 'p_i': 20, 'u_i': 1.2955},
        {'id': 5, 'e_m': 1.230475, 'e_o_k': [0.125048, 0.100039, 0.080031, 0.064025], 'p_i': 10, 'u_i': 2.7520},
        {'id': 6, 'e_m': 9.089822, 'e_o_k': [0.811205, 0.648964, 0.519171, 0.415337, 0.332270], 'p_i': 40, 'u_i': 2.0302},
        {'id': 7, 'e_m': 0.559980, 'e_o_k': [0.068850, 0.055080, 0.044064], 'p_i': 10, 'u_i': 2.5969},
    ]
    B_BUDGET = 143.519997
    return processors, tasks, B_BUDGET
