"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.28, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.28, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.087026, 'e_o_k': [0.514504, 0.411603], 'p_i': 10, 'u_i': 2.6470},
        {'id': 1, 'e_m': 7.848747, 'e_o_k': [0.965010, 0.772008, 0.617606], 'p_i': 20, 'u_i': 4.9479},
        {'id': 2, 'e_m': 0.215920, 'e_o_k': [0.026548, 0.021238, 0.016990], 'p_i': 40, 'u_i': 2.1346},
        {'id': 3, 'e_m': 8.683940, 'e_o_k': [1.447323, 1.157859], 'p_i': 80, 'u_i': 1.3827},
        {'id': 4, 'e_m': 26.184883, 'e_o_k': [4.364147, 3.491318], 'p_i': 80, 'u_i': 3.9576},
        {'id': 5, 'e_m': 4.916820, 'e_o_k': [0.438793, 0.351034, 0.280827, 0.224662, 0.179730], 'p_i': 20, 'u_i': 4.9670},
        {'id': 6, 'e_m': 3.789343, 'e_o_k': [0.338173, 0.270539, 0.216431, 0.173145, 0.138516], 'p_i': 10, 'u_i': 4.5958},
        {'id': 7, 'e_m': 2.626116, 'e_o_k': [0.234363, 0.187490, 0.149992, 0.119994, 0.095995], 'p_i': 80, 'u_i': 1.9552},
    ]
    B_BUDGET = 215.280000
    return processors, tasks, B_BUDGET
