"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439995, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439995, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.524939, 'e_o_k': [0.136090, 0.108872, 0.087098, 0.069678, 0.055743], 'p_i': 10, 'u_i': 1.4156},
        {'id': 1, 'e_m': 4.204720, 'e_o_k': [0.700787, 0.560629], 'p_i': 20, 'u_i': 4.7114},
        {'id': 2, 'e_m': 11.117485, 'e_o_k': [0.992160, 0.793728, 0.634982, 0.507986, 0.406389], 'p_i': 40, 'u_i': 3.0006},
        {'id': 3, 'e_m': 15.918905, 'e_o_k': [1.957242, 1.565794, 1.252635], 'p_i': 80, 'u_i': 1.2816},
        {'id': 4, 'e_m': 2.046219, 'e_o_k': [0.207949, 0.166359, 0.133087, 0.106470], 'p_i': 40, 'u_i': 2.2759},
        {'id': 5, 'e_m': 6.089777, 'e_o_k': [0.495200, 0.396160, 0.316928, 0.253543, 0.202834, 0.162267], 'p_i': 20, 'u_i': 1.7983},
        {'id': 6, 'e_m': 0.092824, 'e_o_k': [0.015471, 0.012377], 'p_i': 10, 'u_i': 2.1310},
        {'id': 7, 'e_m': 3.908399, 'e_o_k': [0.317818, 0.254254, 0.203404, 0.162723, 0.130178, 0.104143], 'p_i': 20, 'u_i': 2.4443},
    ]
    B_BUDGET = 167.439995
    return processors, tasks, B_BUDGET
