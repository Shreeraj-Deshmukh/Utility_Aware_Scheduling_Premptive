"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200009, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200009, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.207619, 'e_o_k': [0.517330, 0.413864, 0.331091], 'p_i': 10, 'u_i': 4.6145},
        {'id': 1, 'e_m': 4.964125, 'e_o_k': [0.827354, 0.661883], 'p_i': 20, 'u_i': 1.3416},
        {'id': 2, 'e_m': 12.796589, 'e_o_k': [1.142009, 0.913607, 0.730886, 0.584708, 0.467767], 'p_i': 40, 'u_i': 3.7595},
        {'id': 3, 'e_m': 3.255913, 'e_o_k': [0.290568, 0.232454, 0.185964, 0.148771, 0.119017], 'p_i': 80, 'u_i': 4.3540},
        {'id': 4, 'e_m': 13.757284, 'e_o_k': [1.118697, 0.894957, 0.715966, 0.572773, 0.458218, 0.366575], 'p_i': 40, 'u_i': 3.6734},
        {'id': 5, 'e_m': 11.807051, 'e_o_k': [1.451687, 1.161349, 0.929079], 'p_i': 80, 'u_i': 4.6535},
        {'id': 6, 'e_m': 8.427683, 'e_o_k': [0.685311, 0.548249, 0.438599, 0.350879, 0.280703, 0.224563], 'p_i': 80, 'u_i': 4.4620},
        {'id': 7, 'e_m': 3.735520, 'e_o_k': [0.379626, 0.303701, 0.242961, 0.194369], 'p_i': 10, 'u_i': 4.1539},
    ]
    B_BUDGET = 239.200009
    return processors, tasks, B_BUDGET
