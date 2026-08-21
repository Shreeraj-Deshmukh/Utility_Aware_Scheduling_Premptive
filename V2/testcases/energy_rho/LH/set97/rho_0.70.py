"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 72.863996, "H": 80, "J": 23, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.7, "seed": 1097, "set": 97, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.70"}
"""

_SPEC = '{"B": 72.863996, "H": 80, "J": 23, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.7, "seed": 1097, "set": 97, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.350656, 'e_o_k': [0.146037, 0.116830, 0.093464, 0.074771, 0.059817], 'p_i': 10, 'u_i': 4.4298},
        {'id': 1, 'e_m': 3.430445, 'e_o_k': [1.968288, 1.574631, 1.259704], 'p_i': 20, 'u_i': 1.5050},
        {'id': 2, 'e_m': 0.207300, 'e_o_k': [0.161233, 0.128986], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 1.714842, 'e_o_k': [0.650744, 0.520596, 0.416476, 0.333181, 0.266545, 0.213236], 'p_i': 80, 'u_i': 4.0993},
        {'id': 4, 'e_m': 0.699429, 'e_o_k': [0.544000, 0.435200], 'p_i': 20, 'u_i': 2.5958},
        {'id': 5, 'e_m': 2.747339, 'e_o_k': [1.576342, 1.261074, 1.008859], 'p_i': 80, 'u_i': 1.3643},
        {'id': 6, 'e_m': 2.551296, 'e_o_k': [0.968160, 0.774528, 0.619623, 0.495698, 0.396558, 0.317247], 'p_i': 40, 'u_i': 1.6218},
        {'id': 7, 'e_m': 2.695881, 'e_o_k': [1.278535, 1.022828, 0.818262, 0.654610], 'p_i': 80, 'u_i': 1.2955},
    ]
    B_BUDGET = 72.863996
    return processors, tasks, B_BUDGET
