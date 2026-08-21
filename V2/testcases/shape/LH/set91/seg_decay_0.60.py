"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320007, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.320007, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.543832, 'e_o_k': [0.475853, 0.285512], 'p_i': 10, 'u_i': 2.8418},
        {'id': 1, 'e_m': 0.195966, 'e_o_k': [0.126081, 0.075649, 0.045389, 0.027233], 'p_i': 20, 'u_i': 1.5566},
        {'id': 2, 'e_m': 6.548072, 'e_o_k': [4.212914, 2.527748, 1.516649, 0.909989], 'p_i': 40, 'u_i': 3.2695},
        {'id': 3, 'e_m': 3.827555, 'e_o_k': [3.349111, 2.009466], 'p_i': 80, 'u_i': 3.8342},
        {'id': 4, 'e_m': 0.151912, 'e_o_k': [0.089234, 0.053540, 0.032124, 0.019275, 0.011565, 0.006939], 'p_i': 20, 'u_i': 4.3734},
        {'id': 5, 'e_m': 0.377358, 'e_o_k': [0.242786, 0.145671, 0.087403, 0.052442], 'p_i': 20, 'u_i': 3.3497},
        {'id': 6, 'e_m': 2.516575, 'e_o_k': [1.619120, 0.971472, 0.582883, 0.349730], 'p_i': 40, 'u_i': 4.2042},
        {'id': 7, 'e_m': 1.395776, 'e_o_k': [0.996983, 0.598190, 0.358914], 'p_i': 40, 'u_i': 1.0373},
    ]
    B_BUDGET = 88.320007
    return processors, tasks, B_BUDGET
