"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440005, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440005, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.877100, 'e_o_k': [0.256762, 0.205409, 0.164327, 0.131462, 0.105170], 'p_i': 10, 'u_i': 2.9699},
        {'id': 1, 'e_m': 0.555123, 'e_o_k': [0.068253, 0.054602, 0.043682], 'p_i': 20, 'u_i': 1.6736},
        {'id': 2, 'e_m': 2.046476, 'e_o_k': [0.182634, 0.146107, 0.116886, 0.093509, 0.074807], 'p_i': 40, 'u_i': 2.6796},
        {'id': 3, 'e_m': 21.531834, 'e_o_k': [2.647357, 2.117885, 1.694308], 'p_i': 80, 'u_i': 2.5270},
        {'id': 4, 'e_m': 4.230965, 'e_o_k': [0.429976, 0.343981, 0.275185, 0.220148], 'p_i': 20, 'u_i': 1.9244},
        {'id': 5, 'e_m': 3.083121, 'e_o_k': [0.513853, 0.411083], 'p_i': 10, 'u_i': 4.2011},
        {'id': 6, 'e_m': 1.814334, 'e_o_k': [0.161917, 0.129534, 0.103627, 0.082902, 0.066321], 'p_i': 40, 'u_i': 3.3831},
        {'id': 7, 'e_m': 3.980107, 'e_o_k': [0.355198, 0.284158, 0.227326, 0.181861, 0.145489], 'p_i': 20, 'u_i': 4.9669},
    ]
    B_BUDGET = 167.440005
    return processors, tasks, B_BUDGET
