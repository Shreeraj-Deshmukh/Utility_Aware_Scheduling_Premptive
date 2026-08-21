"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 67.711988, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.6, "seed": 1013, "set": 13, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 67.711988, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.6, "seed": 1013, "set": 13, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.056307, 'e_o_k': [0.032307, 0.025846, 0.020677], 'p_i': 10, 'u_i': 4.5768},
        {'id': 1, 'e_m': 0.343444, 'e_o_k': [0.267123, 0.213699], 'p_i': 20, 'u_i': 3.5463},
        {'id': 2, 'e_m': 1.086388, 'e_o_k': [0.844968, 0.675975], 'p_i': 40, 'u_i': 3.4252},
        {'id': 3, 'e_m': 2.157450, 'e_o_k': [1.023181, 0.818545, 0.654836, 0.523869], 'p_i': 80, 'u_i': 1.2792},
        {'id': 4, 'e_m': 0.190372, 'e_o_k': [0.090285, 0.072228, 0.057782, 0.046226], 'p_i': 10, 'u_i': 2.1862},
        {'id': 5, 'e_m': 4.007311, 'e_o_k': [2.299277, 1.839421, 1.471537], 'p_i': 80, 'u_i': 2.5645},
        {'id': 6, 'e_m': 1.096980, 'e_o_k': [0.520248, 0.416199, 0.332959, 0.266367], 'p_i': 10, 'u_i': 2.2998},
        {'id': 7, 'e_m': 11.539405, 'e_o_k': [6.620970, 5.296776, 4.237421], 'p_i': 80, 'u_i': 1.4896},
    ]
    B_BUDGET = 67.711988
    return processors, tasks, B_BUDGET
