"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359999, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359999, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.744023, 'e_o_k': [0.457337, 0.365870], 'p_i': 10, 'u_i': 2.6470},
        {'id': 1, 'e_m': 6.976664, 'e_o_k': [0.857787, 0.686229, 0.548983], 'p_i': 20, 'u_i': 4.9479},
        {'id': 2, 'e_m': 0.191929, 'e_o_k': [0.023598, 0.018878, 0.015103], 'p_i': 40, 'u_i': 2.1346},
        {'id': 3, 'e_m': 7.719058, 'e_o_k': [1.286510, 1.029208], 'p_i': 80, 'u_i': 1.3827},
        {'id': 4, 'e_m': 23.275451, 'e_o_k': [3.879242, 3.103394], 'p_i': 80, 'u_i': 3.9576},
        {'id': 5, 'e_m': 4.370507, 'e_o_k': [0.390038, 0.312030, 0.249624, 0.199700, 0.159760], 'p_i': 20, 'u_i': 4.9670},
        {'id': 6, 'e_m': 3.368305, 'e_o_k': [0.300598, 0.240479, 0.192383, 0.153906, 0.123125], 'p_i': 10, 'u_i': 4.5958},
        {'id': 7, 'e_m': 2.334326, 'e_o_k': [0.208323, 0.166658, 0.133327, 0.106661, 0.085329], 'p_i': 80, 'u_i': 1.9552},
    ]
    B_BUDGET = 191.359999
    return processors, tasks, B_BUDGET
