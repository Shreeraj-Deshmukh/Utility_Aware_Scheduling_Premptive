"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760007, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760007, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.821127, 'e_o_k': [0.083448, 0.066758, 0.053407, 0.042725], 'p_i': 10, 'u_i': 4.0093},
        {'id': 1, 'e_m': 4.511521, 'e_o_k': [0.554695, 0.443756, 0.355005], 'p_i': 20, 'u_i': 1.1110},
        {'id': 2, 'e_m': 1.023645, 'e_o_k': [0.083239, 0.066591, 0.053273, 0.042619, 0.034095, 0.027276], 'p_i': 40, 'u_i': 1.1701},
        {'id': 3, 'e_m': 0.906973, 'e_o_k': [0.111513, 0.089210, 0.071368], 'p_i': 80, 'u_i': 4.4848},
        {'id': 4, 'e_m': 1.873656, 'e_o_k': [0.190412, 0.152330, 0.121864, 0.097491], 'p_i': 20, 'u_i': 3.6888},
        {'id': 5, 'e_m': 0.667279, 'e_o_k': [0.082042, 0.065634, 0.052507], 'p_i': 20, 'u_i': 2.1778},
        {'id': 6, 'e_m': 0.282672, 'e_o_k': [0.047112, 0.037690], 'p_i': 10, 'u_i': 3.8298},
        {'id': 7, 'e_m': 4.002764, 'e_o_k': [0.667127, 0.533702], 'p_i': 40, 'u_i': 2.6902},
    ]
    B_BUDGET = 71.760007
    return processors, tasks, B_BUDGET
