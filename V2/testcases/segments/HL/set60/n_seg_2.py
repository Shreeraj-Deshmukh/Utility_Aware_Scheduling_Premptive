"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400005, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400005, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.456621, 'e_o_k': [0.404617, 0.323694], 'p_i': 10, 'u_i': 4.9967},
        {'id': 1, 'e_m': 6.472983, 'e_o_k': [1.798051, 1.438441], 'p_i': 20, 'u_i': 3.1686},
        {'id': 2, 'e_m': 1.070031, 'e_o_k': [0.297231, 0.237785], 'p_i': 40, 'u_i': 1.4833},
        {'id': 3, 'e_m': 9.500976, 'e_o_k': [2.639160, 2.111328], 'p_i': 80, 'u_i': 4.1202},
        {'id': 4, 'e_m': 0.365435, 'e_o_k': [0.101510, 0.081208], 'p_i': 40, 'u_i': 4.7898},
        {'id': 5, 'e_m': 0.184044, 'e_o_k': [0.051123, 0.040899], 'p_i': 10, 'u_i': 3.8151},
        {'id': 6, 'e_m': 5.282667, 'e_o_k': [1.467407, 1.173926], 'p_i': 40, 'u_i': 2.4922},
        {'id': 7, 'e_m': 0.255688, 'e_o_k': [0.071024, 0.056820], 'p_i': 10, 'u_i': 1.4417},
    ]
    B_BUDGET = 110.400005
    return processors, tasks, B_BUDGET
