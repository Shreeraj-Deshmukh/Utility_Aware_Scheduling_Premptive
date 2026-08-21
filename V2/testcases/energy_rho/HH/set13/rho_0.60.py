"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 135.423992, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.6, "seed": 1013, "set": 13, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 135.423992, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.6, "seed": 1013, "set": 13, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.112614, 'e_o_k': [0.064615, 0.051692, 0.041353], 'p_i': 10, 'u_i': 4.5768},
        {'id': 1, 'e_m': 0.686888, 'e_o_k': [0.534246, 0.427397], 'p_i': 20, 'u_i': 3.5463},
        {'id': 2, 'e_m': 2.172776, 'e_o_k': [1.689937, 1.351949], 'p_i': 40, 'u_i': 3.4252},
        {'id': 3, 'e_m': 4.314900, 'e_o_k': [2.046362, 1.637089, 1.309672, 1.047737], 'p_i': 80, 'u_i': 1.2792},
        {'id': 4, 'e_m': 0.380745, 'e_o_k': [0.180570, 0.144456, 0.115565, 0.092452], 'p_i': 10, 'u_i': 2.1862},
        {'id': 5, 'e_m': 8.014622, 'e_o_k': [4.598554, 3.678843, 2.943074], 'p_i': 80, 'u_i': 2.5645},
        {'id': 6, 'e_m': 2.193961, 'e_o_k': [1.040496, 0.832397, 0.665918, 0.532734], 'p_i': 10, 'u_i': 2.2998},
        {'id': 7, 'e_m': 23.078811, 'e_o_k': [13.241941, 10.593552, 8.474842], 'p_i': 80, 'u_i': 1.4896},
    ]
    B_BUDGET = 135.423992
    return processors, tasks, B_BUDGET
