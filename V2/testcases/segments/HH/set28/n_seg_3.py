"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639999, "H": 80, "J": 43, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639999, "H": 80, "J": 43, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.834237, 'e_o_k': [0.478660, 0.382928, 0.306343], 'p_i': 10, 'u_i': 4.4926},
        {'id': 1, 'e_m': 2.062949, 'e_o_k': [1.183659, 0.946927, 0.757542], 'p_i': 20, 'u_i': 3.2922},
        {'id': 2, 'e_m': 2.169279, 'e_o_k': [1.244668, 0.995734, 0.796588], 'p_i': 40, 'u_i': 3.7450},
        {'id': 3, 'e_m': 13.026985, 'e_o_k': [7.474500, 5.979600, 4.783680], 'p_i': 80, 'u_i': 4.8771},
        {'id': 4, 'e_m': 0.281506, 'e_o_k': [0.161520, 0.129216, 0.103373], 'p_i': 20, 'u_i': 4.0203},
        {'id': 5, 'e_m': 1.211718, 'e_o_k': [0.695248, 0.556198, 0.444959], 'p_i': 10, 'u_i': 3.4418},
        {'id': 6, 'e_m': 1.184948, 'e_o_k': [0.679888, 0.543910, 0.435128], 'p_i': 10, 'u_i': 4.8003},
        {'id': 7, 'e_m': 1.426177, 'e_o_k': [0.818299, 0.654639, 0.523711], 'p_i': 10, 'u_i': 3.9154},
    ]
    B_BUDGET = 176.639999
    return processors, tasks, B_BUDGET
