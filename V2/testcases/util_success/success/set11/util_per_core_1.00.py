"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200008, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200008, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.960339, 'e_o_k': [0.199221, 0.159377, 0.127502, 0.102001], 'p_i': 10, 'u_i': 1.8134},
        {'id': 1, 'e_m': 4.578716, 'e_o_k': [0.763119, 0.610495], 'p_i': 20, 'u_i': 3.0607},
        {'id': 2, 'e_m': 13.420227, 'e_o_k': [1.091288, 0.873031, 0.698425, 0.558740, 0.446992, 0.357593], 'p_i': 40, 'u_i': 3.2825},
        {'id': 3, 'e_m': 23.358834, 'e_o_k': [2.084617, 1.667694, 1.334155, 1.067324, 0.853859], 'p_i': 80, 'u_i': 2.2646},
        {'id': 4, 'e_m': 2.890508, 'e_o_k': [0.235047, 0.188037, 0.150430, 0.120344, 0.096275, 0.077020], 'p_i': 10, 'u_i': 4.1633},
        {'id': 5, 'e_m': 2.181643, 'e_o_k': [0.268235, 0.214588, 0.171670], 'p_i': 10, 'u_i': 1.6770},
        {'id': 6, 'e_m': 1.035778, 'e_o_k': [0.105262, 0.084210, 0.067368, 0.053894], 'p_i': 10, 'u_i': 4.7434},
        {'id': 7, 'e_m': 6.734927, 'e_o_k': [0.828065, 0.662452, 0.529961], 'p_i': 20, 'u_i': 4.2977},
    ]
    B_BUDGET = 239.200008
    return processors, tasks, B_BUDGET
