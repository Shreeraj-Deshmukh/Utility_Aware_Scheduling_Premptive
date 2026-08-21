"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279997, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279997, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.928761, 'e_o_k': [0.350615, 0.280492, 0.224394, 0.179515, 0.143612], 'p_i': 10, 'u_i': 4.9659},
        {'id': 1, 'e_m': 3.369287, 'e_o_k': [0.300686, 0.240549, 0.192439, 0.153951, 0.123161], 'p_i': 20, 'u_i': 4.3569},
        {'id': 2, 'e_m': 10.691170, 'e_o_k': [1.314488, 1.051591, 0.841272], 'p_i': 40, 'u_i': 3.1411},
        {'id': 3, 'e_m': 4.304448, 'e_o_k': [0.437444, 0.349955, 0.279964, 0.223971], 'p_i': 80, 'u_i': 3.1206},
        {'id': 4, 'e_m': 5.060886, 'e_o_k': [0.622240, 0.497792, 0.398234], 'p_i': 20, 'u_i': 4.7030},
        {'id': 5, 'e_m': 1.423450, 'e_o_k': [0.237242, 0.189793], 'p_i': 10, 'u_i': 2.0532},
        {'id': 6, 'e_m': 37.057443, 'e_o_k': [3.307125, 2.645700, 2.116560, 1.693248, 1.354599], 'p_i': 80, 'u_i': 1.9357},
        {'id': 7, 'e_m': 2.358695, 'e_o_k': [0.210497, 0.168398, 0.134718, 0.107775, 0.086220], 'p_i': 40, 'u_i': 4.8494},
    ]
    B_BUDGET = 215.279997
    return processors, tasks, B_BUDGET
