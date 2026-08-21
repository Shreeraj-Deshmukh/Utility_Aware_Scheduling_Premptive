"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.127821, 'e_o_k': [0.099416, 0.079533], 'p_i': 10, 'u_i': 1.1226},
        {'id': 1, 'e_m': 2.917468, 'e_o_k': [2.269142, 1.815313], 'p_i': 20, 'u_i': 3.8598},
        {'id': 2, 'e_m': 0.515015, 'e_o_k': [0.400567, 0.320454], 'p_i': 40, 'u_i': 4.6365},
        {'id': 3, 'e_m': 0.662519, 'e_o_k': [0.515292, 0.412234], 'p_i': 80, 'u_i': 1.0760},
        {'id': 4, 'e_m': 9.683938, 'e_o_k': [7.531952, 6.025561], 'p_i': 80, 'u_i': 3.5452},
        {'id': 5, 'e_m': 0.198293, 'e_o_k': [0.154228, 0.123382], 'p_i': 40, 'u_i': 3.7479},
        {'id': 6, 'e_m': 1.613164, 'e_o_k': [1.254683, 1.003746], 'p_i': 80, 'u_i': 4.4508},
        {'id': 7, 'e_m': 1.480331, 'e_o_k': [1.151369, 0.921095], 'p_i': 20, 'u_i': 2.7382},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
