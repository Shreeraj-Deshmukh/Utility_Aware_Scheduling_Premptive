"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.087664, 'e_o_k': [0.339895, 0.203937], 'p_i': 10, 'u_i': 2.8418},
        {'id': 1, 'e_m': 0.391931, 'e_o_k': [0.090058, 0.054035, 0.032421, 0.019452], 'p_i': 20, 'u_i': 1.5566},
        {'id': 2, 'e_m': 13.096144, 'e_o_k': [3.009224, 1.805535, 1.083321, 0.649992], 'p_i': 40, 'u_i': 3.2695},
        {'id': 3, 'e_m': 7.655110, 'e_o_k': [2.392222, 1.435333], 'p_i': 80, 'u_i': 3.8342},
        {'id': 4, 'e_m': 0.303823, 'e_o_k': [0.063738, 0.038243, 0.022946, 0.013768, 0.008261, 0.004956], 'p_i': 20, 'u_i': 4.3734},
        {'id': 5, 'e_m': 0.754717, 'e_o_k': [0.173418, 0.104051, 0.062431, 0.037458], 'p_i': 20, 'u_i': 3.3497},
        {'id': 6, 'e_m': 5.033151, 'e_o_k': [1.156514, 0.693909, 0.416345, 0.249807], 'p_i': 40, 'u_i': 4.2042},
        {'id': 7, 'e_m': 2.791552, 'e_o_k': [0.712131, 0.427278, 0.256367], 'p_i': 40, 'u_i': 1.0373},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
