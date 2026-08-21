"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680006, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680006, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.073209, 'e_o_k': [0.087270, 0.069816, 0.055853, 0.044682, 0.035746, 0.028597], 'p_i': 10, 'u_i': 3.0333},
        {'id': 1, 'e_m': 2.009822, 'e_o_k': [0.163432, 0.130746, 0.104597, 0.083677, 0.066942, 0.053553], 'p_i': 20, 'u_i': 1.6855},
        {'id': 2, 'e_m': 4.500422, 'e_o_k': [0.401632, 0.321306, 0.257045, 0.205636, 0.164509], 'p_i': 40, 'u_i': 1.7213},
        {'id': 3, 'e_m': 5.174123, 'e_o_k': [0.420743, 0.336594, 0.269275, 0.215420, 0.172336, 0.137869], 'p_i': 80, 'u_i': 2.0710},
        {'id': 4, 'e_m': 4.541214, 'e_o_k': [0.461506, 0.369204, 0.295364, 0.236291], 'p_i': 80, 'u_i': 2.4462},
        {'id': 5, 'e_m': 0.685731, 'e_o_k': [0.069688, 0.055750, 0.044600, 0.035680], 'p_i': 10, 'u_i': 2.4016},
        {'id': 6, 'e_m': 15.096114, 'e_o_k': [1.856080, 1.484864, 1.187891], 'p_i': 80, 'u_i': 3.4602},
        {'id': 7, 'e_m': 8.076896, 'e_o_k': [0.820823, 0.656658, 0.525327, 0.420261], 'p_i': 80, 'u_i': 3.9709},
    ]
    B_BUDGET = 95.680006
    return processors, tasks, B_BUDGET
