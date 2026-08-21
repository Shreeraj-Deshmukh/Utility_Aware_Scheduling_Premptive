"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519983, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519983, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.340660, 'e_o_k': [0.164835, 0.131868, 0.105495], 'p_i': 10, 'u_i': 4.1325},
        {'id': 1, 'e_m': 0.003077, 'e_o_k': [0.000313, 0.000250, 0.000200, 0.000160], 'p_i': 20, 'u_i': 2.4718},
        {'id': 2, 'e_m': 19.687798, 'e_o_k': [1.600946, 1.280757, 1.024606, 0.819685, 0.655748, 0.524598], 'p_i': 40, 'u_i': 1.1369},
        {'id': 3, 'e_m': 7.025222, 'e_o_k': [0.713945, 0.571156, 0.456925, 0.365540], 'p_i': 80, 'u_i': 2.0116},
        {'id': 4, 'e_m': 0.533033, 'e_o_k': [0.043344, 0.034676, 0.027740, 0.022192, 0.017754, 0.014203], 'p_i': 10, 'u_i': 3.8042},
        {'id': 5, 'e_m': 1.025558, 'e_o_k': [0.104223, 0.083379, 0.066703, 0.053362], 'p_i': 10, 'u_i': 3.9295},
        {'id': 6, 'e_m': 18.113930, 'e_o_k': [2.227123, 1.781698, 1.425358], 'p_i': 80, 'u_i': 2.7392},
        {'id': 7, 'e_m': 2.069733, 'e_o_k': [0.168304, 0.134643, 0.107714, 0.086172, 0.068937, 0.055150], 'p_i': 20, 'u_i': 3.4812},
    ]
    B_BUDGET = 143.519983
    return processors, tasks, B_BUDGET
