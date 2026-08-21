"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 22, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 22, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.057702, 'e_o_k': [0.011824, 0.009459, 0.007568], 'p_i': 10, 'u_i': 3.1857},
        {'id': 1, 'e_m': 0.850087, 'e_o_k': [0.174198, 0.139359, 0.111487], 'p_i': 20, 'u_i': 3.0673},
        {'id': 2, 'e_m': 0.742953, 'e_o_k': [0.152245, 0.121796, 0.097436], 'p_i': 40, 'u_i': 1.1608},
        {'id': 3, 'e_m': 7.198095, 'e_o_k': [1.475019, 1.180016, 0.944012], 'p_i': 80, 'u_i': 3.0557},
        {'id': 4, 'e_m': 10.841114, 'e_o_k': [2.221540, 1.777232, 1.421785], 'p_i': 80, 'u_i': 1.7105},
        {'id': 5, 'e_m': 30.342716, 'e_o_k': [6.217770, 4.974216, 3.979373], 'p_i': 80, 'u_i': 2.7562},
        {'id': 6, 'e_m': 1.267486, 'e_o_k': [0.259731, 0.207785, 0.166228], 'p_i': 20, 'u_i': 4.1777},
        {'id': 7, 'e_m': 5.200256, 'e_o_k': [1.065626, 0.852501, 0.682001], 'p_i': 80, 'u_i': 1.3396},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
