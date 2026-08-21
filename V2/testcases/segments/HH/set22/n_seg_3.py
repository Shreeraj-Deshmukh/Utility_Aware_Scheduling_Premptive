"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640009, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640009, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.006839, 'e_o_k': [1.151465, 0.921172, 0.736938], 'p_i': 10, 'u_i': 2.9329},
        {'id': 1, 'e_m': 0.143860, 'e_o_k': [0.082543, 0.066034, 0.052827], 'p_i': 20, 'u_i': 4.3550},
        {'id': 2, 'e_m': 4.365284, 'e_o_k': [2.504671, 2.003737, 1.602989], 'p_i': 40, 'u_i': 2.2741},
        {'id': 3, 'e_m': 1.921148, 'e_o_k': [1.102298, 0.881838, 0.705471], 'p_i': 80, 'u_i': 2.5808},
        {'id': 4, 'e_m': 3.369376, 'e_o_k': [1.933248, 1.546599, 1.237279], 'p_i': 40, 'u_i': 4.5356},
        {'id': 5, 'e_m': 1.402420, 'e_o_k': [0.804667, 0.643734, 0.514987], 'p_i': 20, 'u_i': 4.4130},
        {'id': 6, 'e_m': 6.817126, 'e_o_k': [3.911466, 3.129173, 2.503338], 'p_i': 80, 'u_i': 1.1305},
        {'id': 7, 'e_m': 2.194072, 'e_o_k': [1.258894, 1.007115, 0.805692], 'p_i': 10, 'u_i': 4.7707},
    ]
    B_BUDGET = 176.640009
    return processors, tasks, B_BUDGET
