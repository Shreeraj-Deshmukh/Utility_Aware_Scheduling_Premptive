"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400005, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400005, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.644057, 'e_o_k': [0.336897, 0.269518, 0.215614], 'p_i': 10, 'u_i': 2.9699},
        {'id': 1, 'e_m': 0.317213, 'e_o_k': [0.065003, 0.052002, 0.041602], 'p_i': 20, 'u_i': 1.6736},
        {'id': 2, 'e_m': 1.169415, 'e_o_k': [0.239634, 0.191707, 0.153366], 'p_i': 40, 'u_i': 2.6796},
        {'id': 3, 'e_m': 12.303905, 'e_o_k': [2.521292, 2.017034, 1.613627], 'p_i': 80, 'u_i': 2.5270},
        {'id': 4, 'e_m': 2.417694, 'e_o_k': [0.495429, 0.396343, 0.317075], 'p_i': 20, 'u_i': 1.9244},
        {'id': 5, 'e_m': 1.761783, 'e_o_k': [0.361021, 0.288817, 0.231054], 'p_i': 10, 'u_i': 4.2011},
        {'id': 6, 'e_m': 1.036762, 'e_o_k': [0.212451, 0.169961, 0.135969], 'p_i': 40, 'u_i': 3.3831},
        {'id': 7, 'e_m': 2.274347, 'e_o_k': [0.466055, 0.372844, 0.298275], 'p_i': 20, 'u_i': 4.9669},
    ]
    B_BUDGET = 110.400005
    return processors, tasks, B_BUDGET
