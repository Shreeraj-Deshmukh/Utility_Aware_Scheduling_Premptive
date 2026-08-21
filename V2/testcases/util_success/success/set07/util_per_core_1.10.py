"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120005, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120005, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.315147, 'e_o_k': [0.206611, 0.165289, 0.132231, 0.105785, 0.084628], 'p_i': 10, 'u_i': 4.4317},
        {'id': 1, 'e_m': 5.562723, 'e_o_k': [0.565317, 0.452254, 0.361803, 0.289442], 'p_i': 20, 'u_i': 3.9967},
        {'id': 2, 'e_m': 9.599542, 'e_o_k': [0.856694, 0.685355, 0.548284, 0.438627, 0.350902], 'p_i': 40, 'u_i': 3.7464},
        {'id': 3, 'e_m': 37.185034, 'e_o_k': [4.571930, 3.657544, 2.926035], 'p_i': 80, 'u_i': 2.1384},
        {'id': 4, 'e_m': 2.860778, 'e_o_k': [0.351735, 0.281388, 0.225110], 'p_i': 20, 'u_i': 4.1214},
        {'id': 5, 'e_m': 3.925330, 'e_o_k': [0.654222, 0.523377], 'p_i': 10, 'u_i': 3.7942},
        {'id': 6, 'e_m': 13.145031, 'e_o_k': [1.173105, 0.938484, 0.750787, 0.600630, 0.480504], 'p_i': 80, 'u_i': 2.9007},
        {'id': 7, 'e_m': 11.426520, 'e_o_k': [1.161232, 0.928985, 0.743188, 0.594551], 'p_i': 40, 'u_i': 1.2150},
    ]
    B_BUDGET = 263.120005
    return processors, tasks, B_BUDGET
