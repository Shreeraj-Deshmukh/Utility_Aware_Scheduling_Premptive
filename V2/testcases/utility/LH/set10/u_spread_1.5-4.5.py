"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320013, "H": 80, "J": 31, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 88.320013, "H": 80, "J": 31, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.221612, 'e_o_k': [0.084097, 0.067277, 0.053822, 0.043058, 0.034446, 0.027557], 'p_i': 10, 'u_i': 3.5833},
        {'id': 1, 'e_m': 0.192518, 'e_o_k': [0.080178, 0.064142, 0.051314, 0.041051, 0.032841], 'p_i': 20, 'u_i': 2.9327},
        {'id': 2, 'e_m': 3.593476, 'e_o_k': [1.704223, 1.363378, 1.090703, 0.872562], 'p_i': 40, 'u_i': 3.0558},
        {'id': 3, 'e_m': 10.310356, 'e_o_k': [8.019166, 6.415333], 'p_i': 80, 'u_i': 3.0826},
        {'id': 4, 'e_m': 0.725770, 'e_o_k': [0.275414, 0.220331, 0.176265, 0.141012, 0.112809, 0.090248], 'p_i': 20, 'u_i': 3.7309},
        {'id': 5, 'e_m': 0.673150, 'e_o_k': [0.386234, 0.308987, 0.247189], 'p_i': 10, 'u_i': 1.9318},
        {'id': 6, 'e_m': 1.033969, 'e_o_k': [0.593261, 0.474609, 0.379687], 'p_i': 40, 'u_i': 4.4956},
        {'id': 7, 'e_m': 0.801753, 'e_o_k': [0.623586, 0.498869], 'p_i': 40, 'u_i': 2.0724},
    ]
    B_BUDGET = 88.320013
    return processors, tasks, B_BUDGET
