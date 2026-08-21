"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.675362, 'e_o_k': [0.187601, 0.150080], 'p_i': 10, 'u_i': 2.3226},
        {'id': 1, 'e_m': 1.331439, 'e_o_k': [0.369844, 0.295875], 'p_i': 20, 'u_i': 1.3159},
        {'id': 2, 'e_m': 3.504342, 'e_o_k': [0.973428, 0.778743], 'p_i': 40, 'u_i': 2.3324},
        {'id': 3, 'e_m': 7.942253, 'e_o_k': [1.181320, 0.945056, 0.756045, 0.604836, 0.483869], 'p_i': 80, 'u_i': 2.7878},
        {'id': 4, 'e_m': 1.377209, 'e_o_k': [0.282215, 0.225772, 0.180618], 'p_i': 40, 'u_i': 1.7467},
        {'id': 5, 'e_m': 4.445749, 'e_o_k': [0.602523, 0.482018, 0.385614, 0.308492, 0.246793, 0.197435], 'p_i': 10, 'u_i': 1.9890},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
