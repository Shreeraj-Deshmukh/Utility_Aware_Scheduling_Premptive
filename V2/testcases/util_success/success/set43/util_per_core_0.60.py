"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520005, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520005, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.077461, 'e_o_k': [0.007872, 0.006298, 0.005038, 0.004030], 'p_i': 10, 'u_i': 4.0574},
        {'id': 1, 'e_m': 3.699498, 'e_o_k': [0.330155, 0.264124, 0.211299, 0.169039, 0.135232], 'p_i': 20, 'u_i': 2.7090},
        {'id': 2, 'e_m': 5.621561, 'e_o_k': [0.571297, 0.457037, 0.365630, 0.292504], 'p_i': 40, 'u_i': 3.6072},
        {'id': 3, 'e_m': 6.230685, 'e_o_k': [0.506659, 0.405327, 0.324261, 0.259409, 0.207527, 0.166022], 'p_i': 80, 'u_i': 4.5999},
        {'id': 4, 'e_m': 0.579553, 'e_o_k': [0.058898, 0.047118, 0.037695, 0.030156], 'p_i': 20, 'u_i': 4.5815},
        {'id': 5, 'e_m': 6.572874, 'e_o_k': [0.534484, 0.427587, 0.342070, 0.273656, 0.218925, 0.175140], 'p_i': 20, 'u_i': 4.3913},
        {'id': 6, 'e_m': 2.666723, 'e_o_k': [0.444454, 0.355563], 'p_i': 80, 'u_i': 2.4366},
        {'id': 7, 'e_m': 15.916043, 'e_o_k': [1.294240, 1.035392, 0.828313, 0.662651, 0.530121, 0.424096], 'p_i': 40, 'u_i': 1.2704},
    ]
    B_BUDGET = 143.520005
    return processors, tasks, B_BUDGET
