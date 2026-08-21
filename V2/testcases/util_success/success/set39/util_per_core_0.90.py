"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279999, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279999, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.130635, 'e_o_k': [0.419780, 0.335824, 0.268659, 0.214927], 'p_i': 10, 'u_i': 2.7515},
        {'id': 1, 'e_m': 7.106802, 'e_o_k': [1.184467, 0.947574], 'p_i': 20, 'u_i': 4.8495},
        {'id': 2, 'e_m': 13.177683, 'e_o_k': [1.339195, 1.071356, 0.857085, 0.685668], 'p_i': 40, 'u_i': 3.9350},
        {'id': 3, 'e_m': 23.800050, 'e_o_k': [3.966675, 3.173340], 'p_i': 80, 'u_i': 4.4741},
        {'id': 4, 'e_m': 4.516764, 'e_o_k': [0.752794, 0.602235], 'p_i': 40, 'u_i': 1.8290},
        {'id': 5, 'e_m': 2.446348, 'e_o_k': [0.407725, 0.326180], 'p_i': 10, 'u_i': 3.8600},
        {'id': 6, 'e_m': 1.816678, 'e_o_k': [0.223362, 0.178690, 0.142952], 'p_i': 80, 'u_i': 4.0344},
        {'id': 7, 'e_m': 0.243913, 'e_o_k': [0.040652, 0.032522], 'p_i': 10, 'u_i': 3.0439},
    ]
    B_BUDGET = 215.279999
    return processors, tasks, B_BUDGET
