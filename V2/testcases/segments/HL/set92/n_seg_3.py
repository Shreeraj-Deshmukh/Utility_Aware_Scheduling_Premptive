"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.559072, 'e_o_k': [0.114564, 0.091651, 0.073321], 'p_i': 10, 'u_i': 3.7403},
        {'id': 1, 'e_m': 1.614981, 'e_o_k': [0.330939, 0.264751, 0.211801], 'p_i': 20, 'u_i': 1.2645},
        {'id': 2, 'e_m': 6.358045, 'e_o_k': [1.302878, 1.042303, 0.833842], 'p_i': 40, 'u_i': 2.2756},
        {'id': 3, 'e_m': 15.550394, 'e_o_k': [3.186556, 2.549245, 2.039396], 'p_i': 80, 'u_i': 2.5093},
        {'id': 4, 'e_m': 0.003664, 'e_o_k': [0.000751, 0.000601, 0.000480], 'p_i': 10, 'u_i': 3.6510},
        {'id': 5, 'e_m': 3.875294, 'e_o_k': [0.794118, 0.635294, 0.508235], 'p_i': 80, 'u_i': 3.1983},
        {'id': 6, 'e_m': 0.722639, 'e_o_k': [0.148082, 0.118465, 0.094772], 'p_i': 10, 'u_i': 4.3627},
        {'id': 7, 'e_m': 7.557649, 'e_o_k': [1.548699, 1.238959, 0.991167], 'p_i': 40, 'u_i': 4.4103},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
