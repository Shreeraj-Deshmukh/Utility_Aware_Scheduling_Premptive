"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 84.639995, "H": 80, "J": 22, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.3, "seed": 1069, "set": 69, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.30"}
"""

_SPEC = '{"B": 84.639995, "H": 80, "J": 22, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.3, "seed": 1069, "set": 69, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.057702, 'e_o_k': [0.011824, 0.009459, 0.007568], 'p_i': 10, 'u_i': 3.1857},
        {'id': 1, 'e_m': 0.850087, 'e_o_k': [0.236135, 0.188908], 'p_i': 20, 'u_i': 3.0673},
        {'id': 2, 'e_m': 0.742953, 'e_o_k': [0.110506, 0.088405, 0.070724, 0.056579, 0.045263], 'p_i': 40, 'u_i': 1.1608},
        {'id': 3, 'e_m': 7.198095, 'e_o_k': [1.475019, 1.180016, 0.944012], 'p_i': 80, 'u_i': 3.0557},
        {'id': 4, 'e_m': 10.841114, 'e_o_k': [1.612493, 1.289995, 1.031996, 0.825596, 0.660477], 'p_i': 80, 'u_i': 1.7105},
        {'id': 5, 'e_m': 30.342716, 'e_o_k': [6.217770, 4.974216, 3.979373], 'p_i': 80, 'u_i': 2.7562},
        {'id': 6, 'e_m': 1.267486, 'e_o_k': [0.214683, 0.171746, 0.137397, 0.109918], 'p_i': 20, 'u_i': 4.1777},
        {'id': 7, 'e_m': 5.200256, 'e_o_k': [1.444516, 1.155613], 'p_i': 80, 'u_i': 1.3396},
    ]
    B_BUDGET = 84.639995
    return processors, tasks, B_BUDGET
