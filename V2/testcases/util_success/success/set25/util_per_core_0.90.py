"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280006, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280006, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.239789, 'e_o_k': [0.521286, 0.417028, 0.333623], 'p_i': 10, 'u_i': 4.7626},
        {'id': 1, 'e_m': 7.234938, 'e_o_k': [0.645669, 0.516535, 0.413228, 0.330583, 0.264466], 'p_i': 20, 'u_i': 4.6664},
        {'id': 2, 'e_m': 13.935864, 'e_o_k': [1.416246, 1.132997, 0.906398, 0.725118], 'p_i': 40, 'u_i': 1.4428},
        {'id': 3, 'e_m': 2.357218, 'e_o_k': [0.289822, 0.231857, 0.185486], 'p_i': 80, 'u_i': 2.0321},
        {'id': 4, 'e_m': 1.130378, 'e_o_k': [0.091919, 0.073535, 0.058828, 0.047062, 0.037650, 0.030120], 'p_i': 40, 'u_i': 4.9425},
        {'id': 5, 'e_m': 0.750003, 'e_o_k': [0.092214, 0.073771, 0.059017], 'p_i': 10, 'u_i': 3.1847},
        {'id': 6, 'e_m': 0.863200, 'e_o_k': [0.143867, 0.115093], 'p_i': 20, 'u_i': 1.0596},
        {'id': 7, 'e_m': 19.599703, 'e_o_k': [1.991840, 1.593472, 1.274777, 1.019822], 'p_i': 40, 'u_i': 2.6779},
    ]
    B_BUDGET = 215.280006
    return processors, tasks, B_BUDGET
