"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.43999, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.43999, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.246255, 'e_o_k': [0.200463, 0.160370, 0.128296, 0.102637, 0.082110], 'p_i': 10, 'u_i': 4.7898},
        {'id': 1, 'e_m': 7.228070, 'e_o_k': [0.645056, 0.516045, 0.412836, 0.330269, 0.264215], 'p_i': 20, 'u_i': 3.8151},
        {'id': 2, 'e_m': 2.123702, 'e_o_k': [0.215823, 0.172659, 0.138127, 0.110502], 'p_i': 40, 'u_i': 2.4922},
        {'id': 3, 'e_m': 9.116308, 'e_o_k': [0.741308, 0.593046, 0.474437, 0.379550, 0.303640, 0.242912], 'p_i': 80, 'u_i': 2.2134},
        {'id': 4, 'e_m': 3.962541, 'e_o_k': [0.487198, 0.389758, 0.311807], 'p_i': 20, 'u_i': 4.2486},
        {'id': 5, 'e_m': 0.716141, 'e_o_k': [0.058234, 0.046587, 0.037270, 0.029816, 0.023853, 0.019082], 'p_i': 10, 'u_i': 3.7555},
        {'id': 6, 'e_m': 3.453897, 'e_o_k': [0.575649, 0.460520], 'p_i': 20, 'u_i': 3.0652},
        {'id': 7, 'e_m': 2.044886, 'e_o_k': [0.340814, 0.272651], 'p_i': 10, 'u_i': 3.3025},
    ]
    B_BUDGET = 167.439990
    return processors, tasks, B_BUDGET
