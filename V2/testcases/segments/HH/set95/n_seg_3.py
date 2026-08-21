"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639999, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639999, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.583822, 'e_o_k': [0.908750, 0.727000, 0.581600], 'p_i': 10, 'u_i': 1.9313},
        {'id': 1, 'e_m': 2.910187, 'e_o_k': [1.669780, 1.335824, 1.068659], 'p_i': 20, 'u_i': 4.0147},
        {'id': 2, 'e_m': 6.823232, 'e_o_k': [3.914969, 3.131975, 2.505580], 'p_i': 40, 'u_i': 4.3076},
        {'id': 3, 'e_m': 3.019671, 'e_o_k': [1.732598, 1.386078, 1.108863], 'p_i': 80, 'u_i': 2.0651},
        {'id': 4, 'e_m': 3.916411, 'e_o_k': [2.247121, 1.797697, 1.438157], 'p_i': 80, 'u_i': 2.7475},
        {'id': 5, 'e_m': 2.706466, 'e_o_k': [1.552890, 1.242312, 0.993850], 'p_i': 40, 'u_i': 2.9584},
        {'id': 6, 'e_m': 8.231295, 'e_o_k': [4.722874, 3.778299, 3.022639], 'p_i': 80, 'u_i': 3.8181},
        {'id': 7, 'e_m': 1.365476, 'e_o_k': [0.783470, 0.626776, 0.501421], 'p_i': 20, 'u_i': 3.4213},
    ]
    B_BUDGET = 176.639999
    return processors, tasks, B_BUDGET
