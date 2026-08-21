"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519999, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519999, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.184540, 'e_o_k': [0.120380, 0.096304, 0.077043, 0.061635], 'p_i': 10, 'u_i': 4.2289},
        {'id': 1, 'e_m': 0.367942, 'e_o_k': [0.061324, 0.049059], 'p_i': 20, 'u_i': 3.6434},
        {'id': 2, 'e_m': 4.966192, 'e_o_k': [0.403834, 0.323067, 0.258454, 0.206763, 0.165410, 0.132328], 'p_i': 40, 'u_i': 4.1771},
        {'id': 3, 'e_m': 2.442779, 'e_o_k': [0.248250, 0.198600, 0.158880, 0.127104], 'p_i': 80, 'u_i': 4.0903},
        {'id': 4, 'e_m': 3.076728, 'e_o_k': [0.312676, 0.250140, 0.200112, 0.160090], 'p_i': 20, 'u_i': 2.9627},
        {'id': 5, 'e_m': 0.165524, 'e_o_k': [0.016822, 0.013457, 0.010766, 0.008613], 'p_i': 80, 'u_i': 1.9286},
        {'id': 6, 'e_m': 4.835561, 'e_o_k': [0.491419, 0.393135, 0.314508, 0.251606], 'p_i': 10, 'u_i': 3.5955},
        {'id': 7, 'e_m': 10.759914, 'e_o_k': [0.960249, 0.768199, 0.614560, 0.491648, 0.393318], 'p_i': 40, 'u_i': 1.8182},
    ]
    B_BUDGET = 143.519999
    return processors, tasks, B_BUDGET
