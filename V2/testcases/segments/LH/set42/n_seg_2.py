"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320011, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.320011, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.719577, 'e_o_k': [0.559671, 0.447737], 'p_i': 10, 'u_i': 3.9504},
        {'id': 1, 'e_m': 1.039680, 'e_o_k': [0.808640, 0.646912], 'p_i': 20, 'u_i': 2.1226},
        {'id': 2, 'e_m': 0.147163, 'e_o_k': [0.114460, 0.091568], 'p_i': 40, 'u_i': 2.4300},
        {'id': 3, 'e_m': 0.657518, 'e_o_k': [0.511403, 0.409122], 'p_i': 80, 'u_i': 4.3958},
        {'id': 4, 'e_m': 4.480226, 'e_o_k': [3.484620, 2.787696], 'p_i': 80, 'u_i': 3.0676},
        {'id': 5, 'e_m': 0.024458, 'e_o_k': [0.019023, 0.015218], 'p_i': 80, 'u_i': 1.8128},
        {'id': 6, 'e_m': 1.000458, 'e_o_k': [0.778134, 0.622507], 'p_i': 20, 'u_i': 1.5689},
        {'id': 7, 'e_m': 6.313154, 'e_o_k': [4.910231, 3.928185], 'p_i': 40, 'u_i': 4.8976},
    ]
    B_BUDGET = 88.320011
    return processors, tasks, B_BUDGET
