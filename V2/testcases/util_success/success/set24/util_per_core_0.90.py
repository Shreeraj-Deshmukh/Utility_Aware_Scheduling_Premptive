"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280007, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280007, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.607806, 'e_o_k': [0.212058, 0.169647, 0.135717, 0.108574, 0.086859, 0.069487], 'p_i': 10, 'u_i': 1.0948},
        {'id': 1, 'e_m': 0.694613, 'e_o_k': [0.061989, 0.049592, 0.039673, 0.031739, 0.025391], 'p_i': 20, 'u_i': 4.2236},
        {'id': 2, 'e_m': 10.830972, 'e_o_k': [1.805162, 1.444130], 'p_i': 40, 'u_i': 4.6411},
        {'id': 3, 'e_m': 25.602454, 'e_o_k': [3.147843, 2.518274, 2.014619], 'p_i': 80, 'u_i': 4.0085},
        {'id': 4, 'e_m': 4.451552, 'e_o_k': [0.547322, 0.437858, 0.350286], 'p_i': 10, 'u_i': 4.7538},
        {'id': 5, 'e_m': 0.407659, 'e_o_k': [0.041429, 0.033143, 0.026514, 0.021212], 'p_i': 20, 'u_i': 2.8454},
        {'id': 6, 'e_m': 3.200485, 'e_o_k': [0.260253, 0.208202, 0.166562, 0.133249, 0.106600, 0.085280], 'p_i': 10, 'u_i': 1.6966},
        {'id': 7, 'e_m': 10.247766, 'e_o_k': [0.914544, 0.731635, 0.585308, 0.468246, 0.374597], 'p_i': 80, 'u_i': 1.2435},
    ]
    B_BUDGET = 215.280007
    return processors, tasks, B_BUDGET
