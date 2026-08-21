"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359997, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359997, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.096228, 'e_o_k': [0.009779, 0.007823, 0.006259, 0.005007], 'p_i': 10, 'u_i': 2.9445},
        {'id': 1, 'e_m': 3.722840, 'e_o_k': [0.457726, 0.366181, 0.292945], 'p_i': 20, 'u_i': 2.0531},
        {'id': 2, 'e_m': 8.340686, 'e_o_k': [0.847631, 0.678105, 0.542484, 0.433987], 'p_i': 40, 'u_i': 4.9994},
        {'id': 3, 'e_m': 6.143022, 'e_o_k': [0.755290, 0.604232, 0.483385], 'p_i': 80, 'u_i': 2.8114},
        {'id': 4, 'e_m': 1.480711, 'e_o_k': [0.150479, 0.120383, 0.096306, 0.077045], 'p_i': 20, 'u_i': 1.2657},
        {'id': 5, 'e_m': 18.233434, 'e_o_k': [1.482682, 1.186146, 0.948917, 0.759133, 0.607307, 0.485845], 'p_i': 40, 'u_i': 2.4168},
        {'id': 6, 'e_m': 8.200742, 'e_o_k': [0.833409, 0.666727, 0.533382, 0.426705], 'p_i': 80, 'u_i': 4.0307},
        {'id': 7, 'e_m': 38.923967, 'e_o_k': [6.487328, 5.189862], 'p_i': 80, 'u_i': 2.3502},
    ]
    B_BUDGET = 191.359997
    return processors, tasks, B_BUDGET
