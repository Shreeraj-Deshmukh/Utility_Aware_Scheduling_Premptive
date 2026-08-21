"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639989, "H": 80, "J": 22, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "utility", "util_per_core": 0.4, "value": "1.0-5.0"}
"""

_SPEC = '{"B": 176.639989, "H": 80, "J": 22, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "utility", "util_per_core": 0.4, "value": "1.0-5.0"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.057702, 'e_o_k': [0.033108, 0.026486, 0.021189], 'p_i': 10, 'u_i': 3.1857},
        {'id': 1, 'e_m': 0.850087, 'e_o_k': [0.661179, 0.528943], 'p_i': 20, 'u_i': 3.0673},
        {'id': 2, 'e_m': 0.742953, 'e_o_k': [0.309416, 0.247533, 0.198027, 0.158421, 0.126737], 'p_i': 40, 'u_i': 1.1608},
        {'id': 3, 'e_m': 7.198095, 'e_o_k': [4.130055, 3.304044, 2.643235], 'p_i': 80, 'u_i': 3.0557},
        {'id': 4, 'e_m': 10.841114, 'e_o_k': [4.514981, 3.611985, 2.889588, 2.311670, 1.849336], 'p_i': 80, 'u_i': 1.7105},
        {'id': 5, 'e_m': 30.342716, 'e_o_k': [17.409755, 13.927804, 11.142243], 'p_i': 80, 'u_i': 2.7562},
        {'id': 6, 'e_m': 1.267486, 'e_o_k': [0.601111, 0.480889, 0.384711, 0.307769], 'p_i': 20, 'u_i': 4.1777},
        {'id': 7, 'e_m': 5.200256, 'e_o_k': [4.044644, 3.235715], 'p_i': 80, 'u_i': 1.3396},
    ]
    B_BUDGET = 176.639989
    return processors, tasks, B_BUDGET
