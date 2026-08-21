"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320001, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320001, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.686006, 'e_o_k': [0.393610, 0.314888, 0.251910], 'p_i': 10, 'u_i': 2.6470},
        {'id': 1, 'e_m': 1.744166, 'e_o_k': [1.000751, 0.800601, 0.640481], 'p_i': 20, 'u_i': 4.9479},
        {'id': 2, 'e_m': 0.047982, 'e_o_k': [0.027531, 0.022025, 0.017620], 'p_i': 40, 'u_i': 2.1346},
        {'id': 3, 'e_m': 1.929764, 'e_o_k': [1.107242, 0.885794, 0.708635], 'p_i': 80, 'u_i': 1.3827},
        {'id': 4, 'e_m': 5.818863, 'e_o_k': [3.338692, 2.670953, 2.136763], 'p_i': 80, 'u_i': 3.9576},
        {'id': 5, 'e_m': 1.092627, 'e_o_k': [0.626917, 0.501534, 0.401227], 'p_i': 20, 'u_i': 4.9670},
        {'id': 6, 'e_m': 0.842076, 'e_o_k': [0.483158, 0.386527, 0.309221], 'p_i': 10, 'u_i': 4.5958},
        {'id': 7, 'e_m': 0.583581, 'e_o_k': [0.334842, 0.267873, 0.214299], 'p_i': 80, 'u_i': 1.9552},
    ]
    B_BUDGET = 88.320001
    return processors, tasks, B_BUDGET
