"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359987, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359987, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.348406, 'e_o_k': [0.031093, 0.024874, 0.019899, 0.015920, 0.012736], 'p_i': 10, 'u_i': 2.2173},
        {'id': 1, 'e_m': 6.689679, 'e_o_k': [0.679845, 0.543876, 0.435101, 0.348081], 'p_i': 20, 'u_i': 3.2312},
        {'id': 2, 'e_m': 8.921197, 'e_o_k': [1.096868, 0.877495, 0.701996], 'p_i': 40, 'u_i': 3.7207},
        {'id': 3, 'e_m': 19.842095, 'e_o_k': [2.439602, 1.951682, 1.561345], 'p_i': 80, 'u_i': 2.0745},
        {'id': 4, 'e_m': 0.026739, 'e_o_k': [0.004456, 0.003565], 'p_i': 10, 'u_i': 4.8505},
        {'id': 5, 'e_m': 1.039087, 'e_o_k': [0.092731, 0.074185, 0.059348, 0.047478, 0.037983], 'p_i': 10, 'u_i': 1.9965},
        {'id': 6, 'e_m': 8.570447, 'e_o_k': [0.764854, 0.611883, 0.489507, 0.391605, 0.313284], 'p_i': 20, 'u_i': 3.3766},
        {'id': 7, 'e_m': 17.961158, 'e_o_k': [1.602911, 1.282329, 1.025863, 0.820691, 0.656553], 'p_i': 80, 'u_i': 1.4786},
    ]
    B_BUDGET = 191.359987
    return processors, tasks, B_BUDGET
