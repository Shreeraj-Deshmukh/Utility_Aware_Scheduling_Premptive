"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759992, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759992, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.771813, 'e_o_k': [0.144078, 0.115262, 0.092210, 0.073768, 0.059014, 0.047211], 'p_i': 10, 'u_i': 4.5134},
        {'id': 1, 'e_m': 1.363779, 'e_o_k': [0.167678, 0.134142, 0.107314], 'p_i': 20, 'u_i': 4.5874},
        {'id': 2, 'e_m': 1.513800, 'e_o_k': [0.186123, 0.148898, 0.119119], 'p_i': 40, 'u_i': 2.7347},
        {'id': 3, 'e_m': 8.233203, 'e_o_k': [1.012279, 0.809823, 0.647859], 'p_i': 80, 'u_i': 4.9671},
        {'id': 4, 'e_m': 4.079998, 'e_o_k': [0.364112, 0.291290, 0.233032, 0.186425, 0.149140], 'p_i': 80, 'u_i': 4.8761},
        {'id': 5, 'e_m': 0.213076, 'e_o_k': [0.021654, 0.017323, 0.013859, 0.011087], 'p_i': 10, 'u_i': 2.5248},
        {'id': 6, 'e_m': 1.091803, 'e_o_k': [0.181967, 0.145574], 'p_i': 40, 'u_i': 4.9532},
        {'id': 7, 'e_m': 4.570682, 'e_o_k': [0.464500, 0.371600, 0.297280, 0.237824], 'p_i': 40, 'u_i': 2.2979},
    ]
    B_BUDGET = 71.759992
    return processors, tasks, B_BUDGET
