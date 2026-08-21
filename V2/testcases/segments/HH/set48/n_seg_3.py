"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640014, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640014, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.372012, 'e_o_k': [0.787220, 0.629776, 0.503821], 'p_i': 10, 'u_i': 2.6470},
        {'id': 1, 'e_m': 3.488332, 'e_o_k': [2.001502, 1.601202, 1.280961], 'p_i': 20, 'u_i': 4.9479},
        {'id': 2, 'e_m': 0.095964, 'e_o_k': [0.055062, 0.044049, 0.035239], 'p_i': 40, 'u_i': 2.1346},
        {'id': 3, 'e_m': 3.859529, 'e_o_k': [2.214484, 1.771587, 1.417270], 'p_i': 80, 'u_i': 1.3827},
        {'id': 4, 'e_m': 11.637726, 'e_o_k': [6.677384, 5.341907, 4.273526], 'p_i': 80, 'u_i': 3.9576},
        {'id': 5, 'e_m': 2.185253, 'e_o_k': [1.253834, 1.003067, 0.802454], 'p_i': 20, 'u_i': 4.9670},
        {'id': 6, 'e_m': 1.684152, 'e_o_k': [0.966317, 0.773054, 0.618443], 'p_i': 10, 'u_i': 4.5958},
        {'id': 7, 'e_m': 1.167163, 'e_o_k': [0.669684, 0.535747, 0.428597], 'p_i': 80, 'u_i': 1.9552},
    ]
    B_BUDGET = 176.640014
    return processors, tasks, B_BUDGET
