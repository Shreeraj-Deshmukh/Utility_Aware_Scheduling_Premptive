"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200006, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200006, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.829887, 'e_o_k': [0.508302, 0.406642], 'p_i': 10, 'u_i': 4.8131},
        {'id': 1, 'e_m': 1.807671, 'e_o_k': [0.268871, 0.215096, 0.172077, 0.137662, 0.110129], 'p_i': 20, 'u_i': 1.8577},
        {'id': 2, 'e_m': 1.122762, 'e_o_k': [0.230074, 0.184059, 0.147247], 'p_i': 40, 'u_i': 4.0468},
        {'id': 3, 'e_m': 1.611913, 'e_o_k': [0.239754, 0.191803, 0.153442, 0.122754, 0.098203], 'p_i': 80, 'u_i': 2.5682},
        {'id': 4, 'e_m': 4.641757, 'e_o_k': [0.629087, 0.503270, 0.402616, 0.322093, 0.257674, 0.206139], 'p_i': 80, 'u_i': 1.7800},
        {'id': 5, 'e_m': 0.203879, 'e_o_k': [0.027631, 0.022105, 0.017684, 0.014147, 0.011318, 0.009054], 'p_i': 10, 'u_i': 2.6825},
    ]
    B_BUDGET = 55.200006
    return processors, tasks, B_BUDGET
