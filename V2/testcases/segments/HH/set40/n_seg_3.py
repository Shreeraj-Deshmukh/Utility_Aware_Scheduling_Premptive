"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640005, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640005, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.249202, 'e_o_k': [0.716756, 0.573404, 0.458724], 'p_i': 10, 'u_i': 1.9682},
        {'id': 1, 'e_m': 1.221788, 'e_o_k': [0.701026, 0.560821, 0.448657], 'p_i': 20, 'u_i': 4.1538},
        {'id': 2, 'e_m': 6.176629, 'e_o_k': [3.543968, 2.835174, 2.268139], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 8.093637, 'e_o_k': [4.643890, 3.715112, 2.972090], 'p_i': 80, 'u_i': 4.6912},
        {'id': 4, 'e_m': 0.742083, 'e_o_k': [0.425786, 0.340628, 0.272503], 'p_i': 40, 'u_i': 2.4684},
        {'id': 5, 'e_m': 6.497443, 'e_o_k': [3.728041, 2.982433, 2.385946], 'p_i': 40, 'u_i': 2.6468},
        {'id': 6, 'e_m': 0.756149, 'e_o_k': [0.433856, 0.347085, 0.277668], 'p_i': 20, 'u_i': 2.0597},
        {'id': 7, 'e_m': 11.168684, 'e_o_k': [6.408261, 5.126609, 4.101287], 'p_i': 80, 'u_i': 3.8347},
    ]
    B_BUDGET = 176.640005
    return processors, tasks, B_BUDGET
