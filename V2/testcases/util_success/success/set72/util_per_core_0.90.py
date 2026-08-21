"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.28, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.28, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.518489, 'e_o_k': [0.042162, 0.033729, 0.026984, 0.021587, 0.017269, 0.013816], 'p_i': 10, 'u_i': 2.8095},
        {'id': 1, 'e_m': 3.871584, 'e_o_k': [0.476014, 0.380812, 0.304649], 'p_i': 20, 'u_i': 2.2645},
        {'id': 2, 'e_m': 10.681102, 'e_o_k': [0.953216, 0.762573, 0.610058, 0.488047, 0.390437], 'p_i': 40, 'u_i': 4.9290},
        {'id': 3, 'e_m': 12.350234, 'e_o_k': [1.518471, 1.214777, 0.971822], 'p_i': 80, 'u_i': 2.8289},
        {'id': 4, 'e_m': 5.912854, 'e_o_k': [0.527682, 0.422146, 0.337717, 0.270173, 0.216139], 'p_i': 20, 'u_i': 2.4039},
        {'id': 5, 'e_m': 4.560311, 'e_o_k': [0.406977, 0.325581, 0.260465, 0.208372, 0.166698], 'p_i': 10, 'u_i': 2.7593},
        {'id': 6, 'e_m': 27.732683, 'e_o_k': [2.474954, 1.979963, 1.583970, 1.267176, 1.013741], 'p_i': 80, 'u_i': 4.9185},
        {'id': 7, 'e_m': 2.786726, 'e_o_k': [0.342630, 0.274104, 0.219283], 'p_i': 80, 'u_i': 1.9966},
    ]
    B_BUDGET = 215.280000
    return processors, tasks, B_BUDGET
